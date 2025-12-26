#ChatPromptTemplate #HumanMessagePromptTemplate

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

# # Initialize LLM
# llm = ChatOpenAI(model="gpt-4o-mini")

# # Create chat prompt template
# prompt = ChatPromptTemplate(
#     messages=[
#         HumanMessagePromptTemplate.from_template("{content}")
#     ]
# )

# print("Type 'exit' to quit")

# while True:
#     content = input(">> ")

#     if content.lower() in {"exit", "quit"}:
#         break

#     print(f"You entered: {content}")

#     # Create chain
#     chain = prompt | llm

#     # Invoke chain
#     response = chain.invoke({"content": content})

#     print("AI:", response.content)


    #Implementing a chat chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

# Initialize chat model
chat = ChatOpenAI(model="gpt-4o-mini")

# Create chat prompt
prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# Create chain using LCEL
chain = prompt | chat

print("Type 'exit' to quit")

while True:
    content = input(">> ")

    if content.lower() in {"exit", "quit"}:
        break

    response = chain.invoke({"content": content})

    print(response.content)
