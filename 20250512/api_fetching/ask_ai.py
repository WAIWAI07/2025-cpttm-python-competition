def ask_ai(prompt):
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
                    "text": prompt
                },
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

    # Check if the response code is 200 (OK)
    if response.status_code == 200:
        # Print the response
        return data["choices"][0]["message"]["content"]
    else:
        # Print the error message
        return f"Error: {response.status_code} - {data.get('error', 'Unknown error')}"

if __name__ == "__main__":
    # Example usage
    prompt = input("Enter your prompt: ")
    response = ask_ai(prompt)
    print("AI >", response)