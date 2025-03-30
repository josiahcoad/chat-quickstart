# Adding storage
### Retrieving and storing documents can be thought of as another tool

- You can either include relevant storage in the system prompt or you can use a tool to retrieve it when necessary.
- We've created a demo for the llm.txt method
- There's at least two ways to include relevant storage in the system prompt

1. "llm.txt" (March 20, 2024: https://youtu.be/fk2WEVZfheI)
   1. Method
      1. When you injest a document, generate a summary for it and create a "table of contents" with the doc name and the summary
      2. feed the entire "table of contents" of the documents into the system prompt of the llm so it knows what documents are available
      3. Then it can use a tool to retrieve the most relevant document when needed
   2. Pros:
      1. Dead simple to implement
      2. More interpretable/manageable (ie you can inspect the table of contents and know what documents are available and could allow users to update the summaries themselves)
   3. Cons:
      1. Assumes your documents are fairly already "indexed" ie a single document is generall about a single topic
      2. Assumes your documents are not too long (because the llm will try to load the entire document into the context window)
      3. If you have too many documents, the system prompt will get too long and cost / content length could be an issue
2. R.A.G. (Retrieval Augmented Generation)
   1. Method
      1. When injesting your documents, split the document into manageable chunks and embed each chunk.
      2. Then when relevant information is needed, use a tool to retrieve the most relevant chunks and include them in the context window of the llm.
   2. Pros:
      1. Good if you have a lot of documents or documents
      2. Handles arbitarily long or about a lot of different topics
   3. Cons:
      1. Theres a lot of hyperparamaters to tune (chunk size, chunking method, etc)
      2. More infra to manage (eg a vector database)



## More on interacting with storage
**"Document" Loaders**
- Documents are anything that have "page_content" and "metadata"
- https://python.langchain.com/docs/integrations/document_loaders/

**"Document" Store**
- https://python.langchain.com/docs/integrations/vectorstores/

**"Document" Chunkers**
- https://python.langchain.com/docs/concepts/text_splitters
