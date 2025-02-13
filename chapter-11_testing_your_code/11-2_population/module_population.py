def get_city_country_population(city, country, population=None):
    """
    Generate a formatted string representing a city, country, and optionally its population.
    Args:
        city (str): The name of the city.
        country (str): The name of the country.
        population (int, optional): The population of the city. Defaults to None.
    Returns:
        str: A formatted string in the form "City, Country - population Population" if population is provided,
             otherwise "City, Country".
    """
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()
