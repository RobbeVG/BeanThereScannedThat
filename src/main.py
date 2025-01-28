from ocr_module import extract_text_from_image
from search_module import search_google
import os

def main():
    # Step 1: OCR - Extract text from image
    image_path = "coffee_bag_lacabra.jpg"  # Replace with your test image

    directory = "./Tests/Images"

    results = extract_text_from_image(os.path.join(directory, image_path))
    if results:
        # Step 2: Search - Use the extracted text as a query
        print("\nPerforming search for extracted text...\n")
        data = search_google(results)
        print(data)

if __name__ == "__main__":
    main()
    print(r"----------------EXIT-----------------")
