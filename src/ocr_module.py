from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import os, json

def load_api(file_path):
    with open(file_path, 'r') as file:    
        return json.load(file)




# Define the path to the API keys file
API_KEYS_FILE_PATH = './.venv/API.json'
API_KEYS = load_api(API_KEYS_FILE_PATH)

def extract_text_from_image(image_path):
    """
    Extracts text from the given image using Azure Computer Vision OCR.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    dict: The JSON response from the Azure OCR API containing the extracted text.
    """
    try:
        client = ImageAnalysisClient(endpoint=API_KEYS['CVAzure']['endpoint'], credential=AzureKeyCredential(API_KEYS['CVAzure']['key']))
        # Set the API key

        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        results = client.analyze(
            image_data, 
            visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ])

        def extract_text_from_(result):
            """
            Extracts the query from the OCR results.
            """
            query = []
            for block in result["readResult"]["blocks"]:
                for line in block["lines"]:
                    text = line.text.lower()
                    query.append(text) 
            return query
        
        return extract_text_from_(results) 
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    directory = "./Tests"

    # Test the OCR module
    # results = extract_text_from_image("Tests\Images\coffee_bag_lacabra.jpg")
    # if results:
    #     print(results)

    # Test the OCR module > Save responses to JSON files
    imagedir = directory + "/Images"
    for filename in os.listdir(imagedir):
        if filename.endswith(".jpg" or ".png" or ".jpeg"):
            print(f"Processing image: {filename}")
            results = extract_text_from_image(os.path.join(imagedir, filename))
            if results:
                responsedir = directory + "/Responses"
                with open(os.path.join(responsedir, os.path.splitext(filename)[0] + ".json"), "w") as outfile:
                    json.dump(results, outfile, ensure_ascii=False, indent=4)
                print("Results written to response file.")
            else:
                print("No results returned.")
    print("----------------EXIT-----------------")
