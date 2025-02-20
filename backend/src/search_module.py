from googlesearch import search, SearchResult
from bs4 import BeautifulSoup
import requests, re, json
from typing import Any, Dict
from coffee_data import CoffeeData

def contains_keywords(tag, keyword: list[str]) -> bool:
    if tag.string and any(k in tag.string for k in keyword):
        return True
    if tag.has_attr('class') and any(k in tag['class'] for k in keyword):
        return True
    if tag.has_attr('id') and any(k in tag['id'] for k in keyword):
        return True
    return False

def contains_keyword(tag, keyword: str) -> bool:
    if tag.string and keyword in tag.string:
        return True
    if tag.has_attr('class') and keyword in tag['class']:
        return True
    if tag.has_attr('id') and keyword in tag['id']:
        return True
    return False

def cleanupSoup(soup: BeautifulSoup) -> None:
    tags = soup.find_all([
        'header',  # Site headers
        'footer',  # Footers
        'nav',  # Navigation menus
        'script',  # JavaScript scripts
        'style',  # CSS styles
        'aside',  # Sidebars (often contain ads or links)
        'noscript',  # Fallback content for users without JS
        'iframe',  # Embedded content (often ads or external sites)
        'form',  # Search forms or login forms
        'button',  # Interactive buttons, usually not relevant
        'svg',  # Icons and vector graphics
        'input',  # User input fields (login boxes, search bars)
        'select',  # Dropdowns (e.g., language switchers)
        'textarea',  # Comment sections or text inputs
        'ins',  # Often used for ads
        'embed',  # Embedded media, often irrelevant
        'object',  # Flash content or plugins
        'meta',  # Meta tags (usually not relevant)
        ])
    for tag in tags:
        tag.decompose()
    print(f"Removed irrelevant {len(tags)} sections")

def concatTextLanguages(data_fields: dict, languages = ['en', 'nl']) -> None:
    for field, details in data_fields.items():
        combined_keywords = []
        for lang in languages:
            if lang in details['patterns']['text']:
                combined_keywords.extend(details['patterns']['text'][lang])
        data_fields[field]['patterns']['text'] = combined_keywords

def extract_field_text_of_html(text: str, field: str | list[str] = None) -> str:
    extracted_text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    if field:
        if type(field) == list:
            for text in field:
                extracted_text = re.sub(re.escape(text) + r'\W+', '', extracted_text, flags=re.IGNORECASE) # Remove field parameter until text
        else:
            extracted_text = re.sub(re.escape(field) + r'\W+', '', extracted_text, flags=re.IGNORECASE) # Remove field parameter until text
    return extracted_text

def search_coffee_parameters_online(query: str, amount_hits: int = 3) -> CoffeeData:
    # Get Parameter list
    with open('src/parameters.json', 'r') as file:
        parameters = json.load(file)

    data_fields = parameters['dataFields']
    html_class_names_regexes = parameters['HTMLclassNamesRegexes']
    concatTextLanguages(data_fields)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    google_search_results = search(query, num_results=amount_hits)

    scraping_results = {}

    for url in google_search_results:
        print(f"Extracting data from {url}")

        html_body = requests.get(url, headers=headers)
        # Remove headers and footers from the HTML body
        soup = BeautifulSoup(html_body.text, 'html.parser')
        # Remove irrelevant sections
        cleanupSoup(soup)

        # Get if possible the title and the discription tag from the soup
        # Otherwise it is an empty list
        specific_tags = {}
        for field, regex in html_class_names_regexes.items():
            specific_tags[field] = soup.find_all(attrs={"class": re.compile(regex, re.IGNORECASE)})

        coffee_data = CoffeeData({})

        for field_name, details in data_fields.items():
            keywords = details['patterns']['text']
            found = False
            for source in details['sources']:
                extracted_text = ""
                if source in specific_tags:
                    for tag in specific_tags[source]:
                        if contains_keywords(tag, keywords):
                            extracted_text = extract_field_text_of_html(tag.get_text().strip(), field_name)
                            # if 'regex' in details['patterns']:
                            #     if re.match(details['patterns']['regex'], extracted_text):
                            #         coffee_data.variables[field] = extracted_text
                            #         found = True
                            #         break
                            # else:

                        else:
                            if tag.string:
                                extracted_text = tag.string
                                found = True
                                break
                elif source == "text":
                    match = soup.find(string=re.compile(r'\b' + '|'.join(map(re.escape, keywords)) + r'\b', re.IGNORECASE))
                    if match:
                        extracted_text = extract_field_text_of_html(match.strip(), keywords)
                    # if 'regex' in details['patterns']:
                    #     if re.match(details['patterns']['regex'], extracted_text):
                    #         coffee_data.variables[field] = extracted_text
                    #         found = True
                    #         break
                    # else:
                        found = True
                else:
                    print("No source available to search for parameter")
                
                if found:
                    coffee_data.variables[field_name] = extracted_text.strip()

                    break
        scraping_results[url] = coffee_data

    return scraping_results

# Example usage
if __name__ == "__main__":
    query = "Andy coffee filter Colombia Jairo Arcila"
    results = search_coffee_parameters_online(query)
    for url, result in results.items():
        print(f"Extracted from: {url} \n {result}")