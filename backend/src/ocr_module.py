from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from src.api_getmodule import API_KEYS
import os, json

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
        
        return extract_text_from_(results) 
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None