import os

from dotenv import load_dotenv, find_dotenv


import google.generativeai as genai

from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv(find_dotenv())
google_api_key = os.getenv("GOOGLE_API_KEY")


def get_completion(prompt, model="gemini-2.0-pro-exp"):
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-pro-exp",
    temperature=0.7,
    google_api_key=google_api_key
)
    response = llm.invoke(prompt)
    return response.content


customer_review = """
your product is terrible! i dont know
how you were able to get this to the market
i dont want this, actually no one should want this
seriously give me my money back
"""
prompt = f"""
rewrite the {customer_review} message in polite tone
"""
print(get_completion(prompt=prompt))



# messages = [
#     (
#         "system",
#         "the user will give you city and your job is to tell about where it is located and about the wheather there.",
#     ),
#     ("human", "karachi"),
# ]
# print(llm.invoke("what is the wheter in khi"))

