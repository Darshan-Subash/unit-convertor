# import streamlit as st
# import pandas as pd
import os
# from io import BytesIO
# import numpy as np
from dotenv import load_dotenv, find_dotenv


import google.generativeai as genai

from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv(find_dotenv())
google_api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-pro-exp",
    temperature=0.7,
    google_api_key=google_api_key
)




# genai.configure(api_key=google_api_key)
messages = [
    (
        "system",
        "the user will give you city and your job is to tell about where it is located and about the wheather there.",
    ),
    ("human", "karachi"),
]
print(llm.invoke("what is the wheter in khi"))
# print(ai_msg.content)
# Convert generator to list
# model = genai.GenerativeModel("gemini-2.0-pro-exp")

# # Generate content
# response = model.generate_content("whats the whether in karahi")

# print(response.text)

