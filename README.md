It is a conversational chatbot and it is developed using OpenApi, streamlit for frontend, Pinecone for word embeddings.

Output :

![Screenshot 2024-06-13 235901](https://github.com/AddankiKavya630/Conversatinal_Chatbot/assets/114296045/d8502a72-11a1-42c7-b7d1-8623827fd43c)

Approach 

Setting Up the Environment :

	First need to set up our development environment with the necessary libraries and tools API keys and Databse ID.
	And the requirements.txt file contains 
 
•	Streamlit

•	streamlit_chat

•	langchain

•	sentence_transformers

•	openai

•	pinecone-client

Document Indexing 

	It involves loading the documents from a directory, Splitting documents, Creating embeddings and Storing embeddings in Pinecone
Building the Chatbot Application with Streamlit

The main part of our task is to build the chatbot application itself. We use Streamlit to create a seamless interactive interface for the chatbot.
•	Session State Initialisation

•	ConversationBufferWindowMemory

•	PromptTemplate Construction


Creating the User Interface :

•	ChatOpenAI Initialisation

•	ConversationChain Setup

•	Generating Responses


Refining Queries with OpenAI :

	It is used to take the user's query and refine it to ensure it's optimal for providing a relevant answer. It can be implemented by Finding Matches in Pinecone Index and Tracking the Conversation


