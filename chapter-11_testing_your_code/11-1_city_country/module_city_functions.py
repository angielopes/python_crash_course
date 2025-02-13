def get_city_country(city, country, comma=","):
    """
    Generate a formatted string of a city and country.
    Args:
        city (str): The name of the city.
        country (str): The name of the country.
        comma (str, optional): The separator between city and country. Defaults to ",".
    Returns:
        str: A formatted string in the form 'City, Country'.
    """
    city_country = f"{city}{comma} {country}"
    return city_country.title()
