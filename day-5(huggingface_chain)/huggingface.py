import os
from langchain_openai import OpenAI
# from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub

llm = OpenAI()

prompt = PromptTemplate.from_template(
    "I want company to make a company for {product}.Now i want some name")


# prompt3 = prompt.format(product="toys")
# chain = LLMChain(llm=llm, prompt=prompt)

# print(chain.invoke("toys")["text"])


# 👉👉👉👉 ___________###################### Hugging Face_____________________##################

# 3################################################################################################


os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"


chain = LLMChain(llm=HuggingFaceHub(
    repo_id='vennify/t5-base-grammar-correction', model_kwargs={'temperature': 0.2}), prompt=prompt)

# print("using the vennify/t5-base-grammar-correction model \n")
# print(chain.invoke("toys"))


chain2 = LLMChain(llm=HuggingFaceHub(repo_id='facebook/mbart-large-50',
                  model_kwargs={'temperature': 0.5}), prompt=prompt)

print(chain2.invoke("toys"))
