from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

load_dotenv()

# Create a LLM model
model = OllamaLLM(model='llama3.1')

# PART 1: Create a ChatPromptTemplate using a template string
template = "Tell me a joke about {topic}"
prompt_template = ChatPromptTemplate.from_template(template)
print("----------Prompt from Template----------")
prompt = prompt_template.invoke({"topic": "dogs"})
result = model.invoke(prompt)
print(result)

# PART 2: Prompt with Multiple Placeholders
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} story about a {animal}.
Assistant: """
prompt_template = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_template.invoke({"adjective": "funny", "animal": "panda"})
print(prompt)
result = model.invoke(prompt)
print(result)

# PART 3: Prompt with System and Human Messages (using tuples)
print(">>> Part 3")
messages = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {joke_count} jokes.")
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print(prompt)
result = model.invoke(prompt)
print(result)