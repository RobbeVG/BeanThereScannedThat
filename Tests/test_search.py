import pytest
from src.search_module import search_google

@pytest.mark.parametrize("query, expected", [
    ("test", ["test result 1", "test result 2"]),
    ("example", ["example result 1", "example result 2"]),
    ("sample", ["sample result 1", "sample result 2"]),
])

def test_search_function(query, expected):
    assert search_google(query) == expected
