import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader

load_dotenv()
api_key = os.getenv('key')
model = "openai/gpt-oss-120b"
deepseek = ChatGroq(api_key=api_key,model_name = model)



##use passer to filter this thing

parser = StrOutputParser()

deepseek_chain = deepseek | parser #chains it with parser and will go throught the parser and snage the content

##print(deepseek_chain.invoke('Hello there'))

#load in data

loader = TextLoader('data_final.txt',encoding='utf-8')
document = loader.load()
#print(document)

context = " ".join([doc.page_content for doc in document])

template = """
You are a helpful assistant.
Answer the user's question based on the context provided.
Provide clear and concise information.
Respond Appropriately.
do not make up data. 
If you do not know and it is outside your scope apologise to the user that you cannot answer.

context:{context}
question:{question}
"""
k=1

print(deepseek_chain.invoke("Hi!"))

while(k==1): 
    question = input("reply : ")
    
    if question.lower() == "quit":
        
        break
    
    final_template = template.format(context = context, question = question)

    answer = deepseek_chain.invoke(final_template)

    print("\n",answer,"\n")
    
    
#reme
    