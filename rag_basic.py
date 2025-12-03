import os
from typing import reveal_type

from langchain_community.document_loaders.base_o365 import CHUNK_SIZE
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'books', 'odyssey.txt')
persistent_dir = os.path.join(current_dir, 'db', 'chroma_db1')

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_dir):
    print('Persistent directory does not exist. Initializing vector store...')

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'The file {file_path} does not exist, please check')
    
    # Read the text content from the file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split the document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print('\n--- Document Chunks Information ---')
    print(f'Number of document chunks: {len(docs)}')
    print(f'Sample chunk: \n {docs[0].page_content}\n')

    # Create embeddings
    print('\n--- Creating Embeddings ---')
    # embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
    embeddings = OllamaEmbeddings(model='llama3.1')
    print('\n--- Finished creating embeddings ---')

    # Create the vector store and persist it automatically
    print('\n--- Creating Vector Store ---')
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_dir)
    print('\n--- Finished creating vector store ---')
else:
    print('Vector store already exists, no need to initialize.')


# Load the existing vector store with the embedding function
embeddings = OllamaEmbeddings(model='llama3.1')
db = Chroma(persist_directory=persistent_dir, embedding_function=embeddings)

# Define user question
query = "who is odysseus"

# Retrieve relevant documents based on the query
retriever = db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"k": 3, "score_threshold": 0.2})
relevant_docs = retriever.invoke(query)

# Display the relevant results with metadata
print('\n--- Relevant Documents ---')
for i, doc in enumerate(relevant_docs, 1):
    print(f'Document: {i}:\n{doc.page_content}\n')
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")
