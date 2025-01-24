from ocr_module import extract_text_from_image
from search_module import search_google

def main():
    # Step 1: OCR - Extract text from image
    image_path = "coffee_bag.jpg"  # Replace with your test image

    directory = "./Tests/Images"

    results = extract_text_from_image("Tests\Images\coffee_bag_lacabra.jpg")
    if results:
        # Step 2: Search - Use the extracted text as a query
        print("\nPerforming search for extracted text...\n")
        data = search_google(results)
        print(data)

if __name__ == "__main__":
    main()
    print("----------------EXIT-----------------")
