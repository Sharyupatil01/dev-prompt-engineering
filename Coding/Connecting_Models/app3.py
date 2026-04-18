import requests 

url = "http://localhost:11434/api/generate"

data = {
    "model": "phi:latest",
    "prompt":"""
Extract event details.

Example:
Text: John and Mary are attending a wedding on Sunday.
Output:
{
  "name": "wedding",
  "date": "Sunday",
  "participants": ["John", "Mary"]
}

Now do this:

Text: Alice and Bob are going to a science fair on Friday.

Return ONLY JSON:
{
  "name": "",
  "date": "",
  "participants": []
}
""",
    "stream": False
}

response = requests.post(url, json=data)

print(response.json()["response"])


# response :  

#  {
#    "name": "Alice and Bob",
#    "date": "Friday",
#    "participants": []
# }
