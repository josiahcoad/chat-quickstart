import json

from langchain_core.documents import Document
from langchain_core.tools import tool


class Storage:
    """Storage for the agent to use and query for RAG
    Should we tell the agent what kind of data is stored or should it just always query?
    """

    def __init__(self):
        self.store = []

    # pylint: disable=unused-argument
    def add(self, document: Document) -> None:
        # TODO: chunk then injest into a vector database
        self.store.append(document)

    # pylint: disable=unused-argument
    def search(self, query: str, count: int = 5) -> list[Document]:
        # TODO: query the vector database
        return self.store


storage = Storage()


@tool
def add_to_storage(content: str, metadata: dict[str, str]) -> None:
    """Store a document for later retrieval
    metadata is arbitrary metadata about the document such as title and source_url
    """
    document = Document(content, metadata=metadata)
    storage.add(document)


@tool
def search_storage(query: str) -> str:
    """Search for relevant documents in the storage"""
    documents = storage.search(query)
    formatted = "\n\n----------------------\n\n".join(
        [f"{json.dumps(x.metadata, indent=2)}\n{x.page_content}" for x in documents],
    )
    return formatted
