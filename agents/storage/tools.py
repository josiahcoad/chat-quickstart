import json

from langchain.chat_models import init_chat_model
from langchain_core.documents import Document
from langchain_core.tools import tool

storage = {}
llm = init_chat_model(model="gpt-4o-mini", temperature=0)


@tool
def add_to_storage(name: str, content: str, metadata: dict[str, str]) -> str:
    """Store a document for later retrieval.

    Args:
    ----
        name: The name of the document to store (can be a url or document title)
        content: The content of the document to store
        metadata: Extra metadata about the document such as author, source_url, etc.

    """
    summary: str = llm.invoke(
        f"Summarize the content of this doc in one sentence:\n\n{content}",
    ).content  # type: ignore[assignment]
    metadata["summary"] = summary
    document = Document(content, metadata=metadata)
    storage[name] = document
    return f"Saved document: {name}"


@tool
def get_from_storage(doc_names: list[str]) -> str:
    """Get the documents from storage for the given names.

    Args:
    ----
        doc_names: The names of the documents to get.

    """
    docs = [storage[name] for name in doc_names]
    return _format_documents(docs)


def _format_documents(docs: list[Document]) -> str:
    return "\n\n----------------------\n\n".join(
        [f"{json.dumps(x.metadata, indent=2)}\n{x.page_content}" for x in docs],
    )


def get_storage_index() -> str:
    """Get the index of the knowledge base.

    Returns
    -------
        A string representation of the knowledge base index.

    """
    return "\n".join(
        [f"-{name}: {doc.metadata['summary']}" for name, doc in storage.items()],
    )
