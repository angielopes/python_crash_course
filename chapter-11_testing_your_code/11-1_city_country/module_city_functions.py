def get_city_country(city, country):
    """
    Generate a formatted string of the form 'City, Country'.
    Args:
        city (str): The name of the city.
        country (str): The name of the country.
    Returns:
        str: A string formatted as 'City, Country' with title case.
    """

    city_country = f"{city}, {country}"
    return city_country.title()
