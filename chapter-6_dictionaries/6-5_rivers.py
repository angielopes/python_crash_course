"""Make a dictionary containing three major rivers and the country each river runs through.
One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary."""

rivers = {"amazon": "brazil", "nile": "egypt", "yangtze": "china"}

print("Three biggest rivers in the world.")
for river, country in rivers.items():
    if river == "amazon":
        print(
            f"""\n{river.capitalize()}, located in {country.capitalize()}, is the longest river in the world, stretching 6,568 km.
It is also the river with the largest water volume on the planet,
with a discharge of 209,000 cubic meters per second."""
        )
    elif river == "nile":
        print(
            f"""\nThe second longest river in the world is the {river.capitalize()}, measuring 6,650 km.
It flows through a dozen countries in Africa but is most famously associated with {country.capitalize()}."""
        )
    else:
        print(
            f"""\nThe third longest river in the world is the {river.capitalize()}, spanning 6,300 km.
It runs almost entirely through the territory of {country.capitalize()} in a west-to-east direction."""
        )
