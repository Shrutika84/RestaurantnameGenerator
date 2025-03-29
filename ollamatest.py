import requests

# Set the model and prompt
model = "llama2"
prompt = "Suggest a fancy name for an Indian restaurant."

# Send the request to local Ollama server
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": model,
        "prompt": prompt,
        "stream": False
    }
)

# Parse and print the response
result = response.json()
print("🍽️ Restaurant Name Suggestion:", result["response"])