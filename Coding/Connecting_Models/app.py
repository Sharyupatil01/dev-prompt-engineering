import requests 

url="http://localhost:11434/api/generate"

data={
    "model":"phi:latest",
    "prompt":"Explain Binary Search Algorithm in 6 Major Points with Example",
    "stream":False
}

response=requests.post(url,json=data)

print(response.json()["response"])


# Response : 
#  Certainly! Prompt engineering involves designing or programming computer systems to respond in a human-like way by creating prompts that are designed to mimic natural language and understand context. 
# This can be achieved using natural language processing (NLP) techniques, such as sentiment analysis, intent recognition, and understanding of common phrases and idioms. 
# By implementing these technologies, the computer system is able to respond to user input in a more intuitive and human-like way, which can improve the overall user experience. For example, chatbots are an application of prompt engineering that are designed to engage with users in a conversational manner.