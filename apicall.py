import json
import requests
import openai

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODk3ZDkyMjMtYjcwNS00YmNmLWI2YzYtODFhYmNmZWViOGE5IiwidHlwZSI6ImFwaV90b2tlbiJ9.r2DUDE4W2aBItzrgGoUSzYREh4yqTsQpLaGjDkAL10c"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Mouli"
}



def take(query):
    payload["text"]=query
   # print(payload)
    response=requests.post(url,json=payload,headers=headers)
    #print(response.text)
    result=json.loads(response.text)
    print(result['openai']['generated_text'])
take("How are you...")    
