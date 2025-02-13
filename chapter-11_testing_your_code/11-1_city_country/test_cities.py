from module_city_functions import get_city_country


def test_city_country():
    formatted_city_country_name = get_city_country("São Paulo", "Brasil")
    assert formatted_city_country_name == "São Paulo, Brasil"
