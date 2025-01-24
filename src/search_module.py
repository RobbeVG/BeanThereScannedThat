import json, os, requests, re
from serpapi import GoogleSearch



def search_google(query):

    # Define the URL and headers
    url = "https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Define the parameters
    params = {
        "q": " ".join(query)
    }

    # Send the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the search results from the HTML response
        results = re.findall(r'<h3 class="zBAuLc"><div class="BVG0Nb"><div class="s3v9rd">(.*?)</div></div></h3>', response.text)
        return results
    else:
        print(f"Error: {response.status_code}")
        return None



# Example usage:
if __name__ == "__main__":



    directory = "./Tests"

    responsesdir = directory + "/Responses"
    for filename in os.listdir(responsesdir):
        if filename.endswith(".json"):
            print(f"Processing response: {filename}")
            with open(os.path.join(responsesdir, filename), 'r') as file: 
                data = json.load(file)
            

            query = extract_query(data)
            print(query)
    #         result = search_google(query)
    #         if result:
    #             print(f"Results: {result}")
    #         else:
    #             print("No results returned.")


    print(search_google("Python programming"))
