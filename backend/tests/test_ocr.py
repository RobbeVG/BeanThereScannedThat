from src import ocr_module

def test_ocr():
    results = ocr_module.extract_text_from_image("Tests\Images\coffee_bag_lacabra.jpg")
    print(results)