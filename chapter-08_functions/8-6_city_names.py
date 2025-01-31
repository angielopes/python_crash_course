"""Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned."""


def city_country(city, country):
    """Returns a formatted city and country"""
    formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()


location = city_country("bangkok", "thailand")
print(location)
location = city_country("tokyo", "japan")
print(location)
location = city_country("new york", "usa")
print(location)
