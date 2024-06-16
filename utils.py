from sentence_transformers import SentenceTransformer 
import pinecone
import openai
import streamlit as st
from pinecone import Pinecone,ServerlessSpec
import os
from openai import OpenAI


PINECONE_API_KEY ='cbd9b169-6412-4ca6-af35-e527fe0259ae'
OPENAI_API_KEY = "sk-proj-c5DxpbUpLDB8d3raI9kQT3BlbkFJh7VZhtncEC87cxY5I37m"

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

openai.api_key = ""
model = SentenceTransformer('all-MiniLM-L6-v2')


pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "langchain-chatbot"
spec = ServerlessSpec(
    cloud="aws", 
    region="us-east-1"
)

# Create the index
if index_name not in [index_info["name"] for index_info in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=1536,  # Example dimension, adjust to your needs
        metric='dotproduct',
        spec=spec
    )

# Connect to the index
index = pc.Index(index_name)



def find_match(input):
    input_em = model.encode(input).tolist()
    print("input_em\n\n",input_em)
    result = index.query(
    vector=input_em,  # the query vector
    top_k=2,          # number of top results to fetch
    include_metadata=True  # include metadata in results
    )

    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']

def query_refiner(conversation, query):

    client = OpenAI()

    
    response  = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:"}])

    
    return response.choices[0].message.content

def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
    return conversation_string