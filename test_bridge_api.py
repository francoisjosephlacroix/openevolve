#!/usr/bin/env python3
import requests
import json

# Test the bridge API directly
url = "http://localhost:8765/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer dummy-key"
}
data = {
    "model": "gemini-2.0-flash-lite",
    "messages": [
        {"role": "user", "content": "Hello, respond with just 'Hi there!'"}
    ],
    "stream": False
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response type: {type(response.text)}")
    print(f"Response content: {response.text}")
    
    # Try to parse as JSON
    try:
        json_response = response.json()
        print(f"JSON type: {type(json_response)}")
        print(f"JSON keys: {json_response.keys() if isinstance(json_response, dict) else 'Not a dict'}")
        
        if isinstance(json_response, dict) and 'choices' in json_response:
            print(f"Choices: {json_response['choices']}")
        
    except Exception as e:
        print(f"JSON parsing error: {e}")
        
except Exception as e:
    print(f"Request error: {e}")
