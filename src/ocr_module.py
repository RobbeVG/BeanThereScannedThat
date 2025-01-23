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

def print_results(results):
    print("Image analysis results:")
    print(" Read:")
    if results.read is not None:
        for line in results.read.blocks[0].lines:
            print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
            for word in line.words:
                print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")

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
            visual_features=[VisualFeatures.READ])

        

        return results 
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None

if __name__ == "__main__":
    directory = "./Tests/Images"
    print("Loaded API Keys:", API_KEYS)

    results = extract_text_from_image("Tests\Images\coffee_bag_lacabra.jpg")
    if results:
        print_results(results)

    # Test the OCR module
    # for filename in os.listdir(directory):
    #     if filename.endswith(".jpg" or ".png" or ".jpeg"):
    #         test_image = filename
    #         extract_text_from_image(os.path.join(directory, test_image))
    print("----------------EXIT-----------------")
