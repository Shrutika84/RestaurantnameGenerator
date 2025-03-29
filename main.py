from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
# Load local LLM via Ollama
llm = Ollama(model="mistral")  # or "llama2", etc.

# Prompt the model
response = llm.invoke("Suggest a fancy name for an Indian restaurant")
print("Restaurant Name:", response)
