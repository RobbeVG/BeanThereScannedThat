import json

def load_api(file_path):
    with open(file_path, 'r') as file:    
        return json.load(file)

# Define the path to the API keys file
API_KEYS = load_api('./.venv/API.json')