from openai import OpenAI
client=OpenAI()
response=client.responses.create(
    model="chatgpt-4o-latest",
    input="Explain Binary Search Algorithm in 6 Major Points with Example",
)
print(response.output_text)

# Require OPENAI_API_KEY 
