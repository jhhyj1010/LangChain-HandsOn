from typing import Any
from langchain_chroma import Chroma
# from langchain_community.embeddings import OllamaEmbeddings # deprecated
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_classic import hub
# from langchain_community.llms import Ollama # deprecated
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
# from langchain_ollama import ChatOllama
import urllib3

urllib3.disable_warnings()

# loading the vectorstore
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=OllamaEmbeddings(model="llama3.1"))

# loading the Llama3.1 model
# llm = Ollama(model="llama3.1", base_url="http://localhost:11434/") # depreacated
# llm = ChatOllama(model="llama3.1")
llm = OllamaLLM(model="llama3.1")

# using the vectorstore as the retriever
retriever = vectorstore.as_retriever()

# formating the docs
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# loading the QA chain from langchain hub
rag_prompt = hub.pull("rlm/rag-prompt")

# creating the QA chain
qa_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough[Any]()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

# running the QA chain in a loop until the user types "exit"
while True:
    question = input("Question: ")
    if question.lower() == "exit":
        break
    answer = qa_chain.invoke(question)

    print(f"\nAnswer: {answer}\n")

