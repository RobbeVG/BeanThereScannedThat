import requests

from src import api_getmodule

def test_load_api():
    assert isinstance(api_getmodule.load_api('./.venv/API.json'), dict, 
                      "API keys is not loaded as a dictionary.")