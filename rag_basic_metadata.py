import os

#from langchain_chroma import Chroma
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings

# Define the directory containing the text files and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
books_dir = os.path.join(current_dir, "books")
db_dir = os.path.join(current_dir, "db")
persistent_dir = os.path.join(db_dir, "chromadb_with_metadata")

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_dir):
    print('Persistent directory does not exist, initializing vector store...')

    # Ensure the books directory exists
    if not os.path.exists(books_dir):
        raise FileNotFoundError(
            f'The directory {books_dir} does not exist, please check the paht.'
        )
    
    # List all text files in the directory
    book_files = [f for f in os.listdir(books_dir) if f.endswith(".txt")]

    # Read the text content from each file and store it with metadata
    documents = []
    for book in book_files:
        file_path = os.path.join(books_dir, book)
        loader = TextLoader(file_path)
        book_docs = loader.load()

        for doc in book_docs:
            # Add metadata to each doc indicating the source
            doc.metadata = {'source': book}
            documents.append(doc)

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print('\n--- Document Chunks Information ---')
    print(f'Number of document chunks: {len(docs)}')

    # Create embeddings
    print('\n--- Creating Embeddings ---')
    embeddings = OllamaEmbeddings(model='llama3.1')
    print('\n--- Finished creating embeddings ---')

    # Create the vectore store and persist it
    """
    Turn off VPN, otherwise 503 ERROR would occur.
    """
    print('\n--- Creating and persisting vectore store ---')
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_dir)
    print('\n--- Finished creating and persisting vectore store ---')
else:
    print('Vectore Store already exists, no need to initialize!')