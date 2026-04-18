from openai import OpenAI
model="xyz"
client=OpenAI(
    api_key="abc"
)

history=[
    {
        "role":"user",
        "content":"tell me a joke"
    }
]

response=client.responses.create(
    model=model,
    input=history,
    store=False # Store the response in the database false- its wont store 
)
print(response.output_text)


#update the message history with assisant response / message 

history+=[
    {
        "role":el.role,
        "content":el.content
    }
    for el in response.output
]

# Ask for another joke 

history.append({
    "role":"user",
    "content":"tell me another joke"
})

# Calling for another joke 

response=client.responses.create(
    model=model,
    input=history,
    store=False
)
print("Second Joke" , response.output_text)
