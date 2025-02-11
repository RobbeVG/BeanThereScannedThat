import pytest

from src.search_module import search_coffee_parameters_online

@pytest.mark.parametrize("query", [
    (["Andy", "Colombia", "Filter", "Jairo Arcila"]),
    (["Cross Roast", "finca el recuerdo"])
])

def test_search_function(query):
    print('\n' + query[0])
    results = search_coffee_parameters_online(query)

    for i, result in enumerate(results, 1):
        print(f"Result {i}: {result}")
    assert i == 3

