# This script fetches data from a public API and prints the response.
import requests

# Set the token and URL for the API request

# Read the token from a file
with open("api_token_key.txt", "r") as file:
    token = file.read().strip()

url = "https://openrouter.ai/api/v1/chat/completions"

# Set the headers for the request
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Set the messages for the request
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What's in this image?"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                }
            }
        ]
    }
]

# Make the API request
payload = {
    "model": "google/gemini-2.0-flash-001",
    "messages": messages
}

response = requests.post(url, headers=headers, json=payload)

data = response.json()

# Print the response
if response.status_code == 200:
    print("Response:", data)