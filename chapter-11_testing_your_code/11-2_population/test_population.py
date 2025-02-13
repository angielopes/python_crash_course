from module_population import get_city_country_population


def test_city_country():
    """
    Test the function get_city_country_population to ensure it correctly formats
    the city and country names into a single string.
    The function should take two arguments: a city name and a country name, and
    return a string in the format "City, Country".
    This test specifically checks if the function correctly formats the city
    "São Paulo" and the country "Brasil" into the string "São Paulo, Brasil".
    """
    formatted_city_country = get_city_country_population("São Paulo", "Brasil")
    assert formatted_city_country == "São Paulo, Brasil"


def test_city_country_population():
    """
    Test the get_city_country_population function to ensure it correctly formats
    the city, country, and population into a single string.
    The function should return a string in the format:
    "City, Country - Population population".

    Example:
        São Paulo, Brasil - Population 11000000
    This test checks if the function correctly handles the input:
        city: "São Paulo"
        country: "Brasil"
        population: 11_000_000
    """
    formatted_city_country_population = get_city_country_population(
        "São Paulo", "Brasil", population=11_000_000
    )
    assert (
        formatted_city_country_population == "São Paulo, Brasil - Population 11000000"
    )
