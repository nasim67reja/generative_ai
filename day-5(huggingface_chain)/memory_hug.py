from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI


client = OpenAI()


# zero shot prompting
prompt = "can you tell me total number of country in aisa? can you give me top 10 contry name?"

# print(client.invoke(prompt))


# Chain 🖐🖐🖐🖐🖐🖐🖐🖐🖐


prompt = PromptTemplate.from_template(
    "what is a good name for a company that makes {product}")

chain = LLMChain(llm=client, prompt=prompt)

# print(chain.invoke("Football"))
# output = chain.invoke("Football")
# print(output)


# 3########### simple sequential chain

prompt_template_name = PromptTemplate(
    input_variables=["startup_name"],
    template="I want to start a startup for {startup-name} , suggest me a good name for this"
)

name_chain = LLMChain(llm=client, prompt=prompt_template_name)

# out = name_chain.invoke("ai")
# print(out)

prompt_template_items = PromptTemplate(
    input_variables=["name"],
    template="suggest some strategies for {name}"
)


strategies_chain = LLMChain(llm=client, prompt=prompt_template_items)


chain = SimpleSequentialChain(chains=[name_chain, strategies_chain])


print(chain.invoke("artifical intelligence"))
