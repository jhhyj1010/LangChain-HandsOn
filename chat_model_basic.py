from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

# Load envroinment variables from .env
load_dotenv()

# Create a ChatOpenAI model
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatOllama(model="llama3.1")  # , base_url="http://localhost:11434")

# Invoke the model with a message
result = llm.invoke("What is 10 times 99")
print("full result is: \n", result)
print("Content only: \n", result.content)
