import langchain
from langchain.llms import OpenAI


client=OpenAI()


# zero shot prompting
prompt="can you tell me total number of country in aisa? can you give me top 10 contry name?"

# print(client.predict(prompt).strip())


# 👉👉👉👉👉 Prompt Tamplates

from langchain.prompts import PromptTemplate

prompt_template_name=PromptTemplate(
    input_variables=["country"],
    template="can you tell me the capital of {country}?"
)

prompt1=prompt_template_name.format(country="Bangladesh")

# Other way

another_way_prompt=PromptTemplate.from_template("what is a good name for a compnay that makes a {product}")
prompt2=another_way_prompt.format(product="toys")

# print(client.predict(prompt2).strip())


# 👉👉👉👉👉 Agents
# we use agent in langchain for calling any third party tool

prompt3="who won the recent cricket world cup?"
# print(client.predict(prompt3).strip())    # it can not give the current result

############## For extracting real time information i am going to use serp api

serpapi_key="4ee960be876c532a4e4c6e2069857f161715265a13a9223f403673210e3bd417"

from langchain.llms import OpenAI
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.agents import initialize_agent

client=OpenAI()

tool=load_tools(["serpapi"],serpapi_api_key=serpapi_key,llm=client)

agent=initialize_agent(tool,client,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

# output=agent.run("can you tell who won the cricket worldcup recently?")
# print(output) #The Australian Men's Cricket Team won the 2023 Cricket World Cup.

######################## so in the term of agent. at first create the tool then initiate it with agent

########################### 👉👉👉👉👉👉 Chain ############################################################

prompt=PromptTemplate.from_template("what is a good name for a company that makes {product}")

from langchain.chains import LLMChain

chain=LLMChain(llm=client,prompt=prompt)

print(chain.run("Book"))