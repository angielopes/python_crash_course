from module_city_functions import get_city_country


def test_city_country():
    """
    Test the get_city_country function to ensure it correctly formats
    city and country names.
    This test checks if the function get_city_country, when given the
    city "São Paulo" and the country "Brasil", returns the formatted
    string "São Paulo, Brasil".
    """

    formatted_city_country_name = get_city_country("São Paulo", "Brasil")
    assert formatted_city_country_name == "São Paulo, Brasil"
