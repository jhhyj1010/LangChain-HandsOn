from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_ollama import OllamaLLM

load_dotenv()

# Create a model of Ollama
model = OllamaLLM(model='llama3.1')

# Define prompt templates 
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {joke_count} jokes.template_format=")
])

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()

# Run the chain
result = chain.invoke({"topic": "bears", "joke_count": 2})
print(result)