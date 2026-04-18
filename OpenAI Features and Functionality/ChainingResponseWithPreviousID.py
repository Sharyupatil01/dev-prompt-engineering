#Chaining Responses Using Previous ID 

from openai import OpenAI

model="xyz"

client=OpenAI(
    api_key="abc"
)

response=client.responses.create(
    model=model,
    input="Tell me a joke",
)
# chaining responses using previous id of response 

second_response=client.responses.create(
    model=model,
    previous_response_id=response.id,
    input=[
        {
            "role":"user",
            "content":"tell me why this joke is funny ? "
        }
    ]
)

print(second_response.output_text)

