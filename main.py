# from openai import OpenAI

# client = OpenAI()

# print(
#     client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": "What are the main differences between REST and GraphQL?"}],
#     ).choices[0].message.content
# )

# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(model="gpt-4o-mini")

# prompt = input("Enter your prompt: ")

# response = llm.invoke(prompt)
# print("\nResponse:\n", response.content)

# SECURE THIS KEY!
# from langchain_openai import OpenAI
# from langchain_core.prompts import PromptTemplate

# llm = OpenAI()  # uses OPENAI_API_KEY from env

# prompt = PromptTemplate(
#     template="Write a very short {language} function that will {task}",
#     input_variables=["language", "task"],
# )

# chain = prompt | llm  # LCEL (LangChain Expression Language)

# result = chain.invoke({
#     "language": "python",
#     "task": "return a list of numbers",
# })

# print(result)


import argparse
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# ----------------------------
# Argument parsing
# ----------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# ----------------------------
# LLM (API key via env variable)
# ----------------------------
llm = OpenAI()  # uses OPENAI_API_KEY from environment

# ----------------------------
# Prompt template
# ----------------------------
code_prompt = PromptTemplate(
    input_variables=["task", "language"],
    template="Write a very short {language} function that will {task}",
)

test_prompt = PromptTemplate(
    input_variables=["language", "code"],
    template="Write test code for the following {language} code:\n{code}"
)

# ----------------------------
# Chain (LCEL style)
# ----------------------------
code_chain = code_prompt | llm
test_chain = test_prompt | llm

# ----------------------------
# Invoke chain
# ----------------------------
def sequential_chain(inputs: dict):
    # Step 1: Generate code
    code = code_chain.invoke({
        "language": inputs["language"],
        "task": inputs["task"],
    })

    # Step 2: Generate tests using generated code
    test = test_chain.invoke({
        "language": inputs["language"],
        "code": code,
    })

    return {
        "code": code,
        "test": test,
    }

# ----------------------------
# Invoke chain
# ----------------------------
result = sequential_chain({
    "language": args.language,
    "task": args.task,
})

print("\nCODE:\n", result["code"])
print("\nTESTS:\n", result["test"])
