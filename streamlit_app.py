import streamlit as st
import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
u_c_key = os.getenv("UNIT-CONVERTOR-KEY")

url = "https://api.happi.dev/v1/unit-converter"

params = {  
    "from": "m",
    "to": "m",
    "value": "100"
}

headers = {
    "accept": "application/json",
    "x-happi-token": u_c_key
}


response = requests.get(url, headers=headers)
res = response.json()

unit = {}
a = list()
for i in range(len(res["allowedUnits"])):
    if res["allowedUnits"][i]["measure"] in a:
        continue
    a.append(res["allowedUnits"][i]["measure"])

measure = list(a)  


name = [[] for _ in range(len(measure))]  

n = 0  
for i in range(len(res["allowedUnits"])):
    temp = measure[n]
    
    
    if i > 0 and res["allowedUnits"][i]["measure"] != temp:
        n += 1  
        
    
    name[n].append(res["allowedUnits"][i]["name"])
    unit[res["allowedUnits"][i]["name"]] = res["allowedUnits"][i]["unit"]

options_dict = {}


for i in range(len(measure)):
    options_dict[measure[i]] = name[i]
    







st.title("Simple Option Menu")

option = st.selectbox(
    "Choose an option:",["select"] +
    list(options_dict.keys())
)
if option != "select":
    sub_option1 = st.selectbox(
        f"Choose from:",
        list(options_dict[option]))
    st.write(f"You selected: {option}-{sub_option1}")
    sub_option2 = st.selectbox(
        f"Choose to:",
        list(options_dict[option]))
    st.write(f"You selected: {option}-{sub_option2}")
    st.write("enter value")
    value= st.number_input("Enter a number")
    
    params = {  
    "from": unit[sub_option1],
    "to": unit[sub_option2],
    "value": value
    }
    
    response = requests.get(url, headers=headers, params=params)


    res = response.json()
    print(res)
    st.write(f"conversion from : {sub_option1} to {sub_option2} is {res['result']}")

