from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_community.chat_message_histories import ChatMessageHistory, FileChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

# ----------------------------
# LLM
# ----------------------------
chat = ChatOpenAI(model="gpt-4o-mini")

# ----------------------------
# In-memory chat history (conversation buffer)
# ----------------------------
store = {}

def get_session_history(session_id: str):
    return FileChatMessageHistory(
        file_path="messages.json"
    )

# ----------------------------
# Prompt with memory placeholder
# ----------------------------
prompt = ChatPromptTemplate(
    messages=[
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ]
)

# ----------------------------
# Chain
# ----------------------------
chain = prompt | chat

# ----------------------------
# Attach conversation buffer memory
# ----------------------------
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="content",
    history_messages_key="history",
)

print("Type 'exit' to quit")

# ----------------------------
# Chat loop
# ----------------------------
while True:
    content = input(">> ")

    if content.lower() in {"exit", "quit"}:
        break

    response = chain_with_memory.invoke(
        {"content": content},
        config={"configurable": {"session_id": "default"}}
    )

    print("AI:", response.content)
