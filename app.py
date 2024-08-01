
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StrOutputParser

import phi3 as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]= "sk-proj-5e79fZfuHRICGjvyKT3BlbkFJDpnmtoyrCmqtEMT3t4Og"
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]= "lsv2_pt_7f74ccc30c4049a317e3ee1cb0c419_de715cfc36"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="microsoft/Phi-3-mini-128k-instruct")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


