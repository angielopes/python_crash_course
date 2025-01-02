"""Think of things you could store in a list.
For example, you could make a list of mountains, rivers, countries, cities, languages,
or anything else you'd like.
Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once."""

montains = ["Everest", "Kilimanjaro", "Aconcágua", "Denali", "Mont Blanc"]
rivers = ["Amazonas", "Nilo", "Yangtzé", "Mississipi", "Ganges"]
countries = ["Brasil", "Japão", "Alemanha", "Canadá", "Austrália"]
cities = ["São Paulo", "Tóqui", "Paris", "Nova York", "Cidade do Cabo"]
languages = ["Português", "Inglês", "Espanhol", "Mandarim", "Árabe"]

# Acessando elementos de uma lista
my_country = countries[0]
print(f"Eu moro no {my_country}")

# Modificando elementos da lista
cities[3] = "Buenos Aires"
print(f"\nLista após substituir Nova York por Buenos Aires:")
print(cities)

# Adicionando elementos à lista

# Append()
languages.append("Francês")
print("\nLista após adicionar francês ao final da lista:")
print(languages)

# Insert()
rivers.insert(1, "Río Negro Province")
print("\nLista após a inserção do Río Negro Province na posição 1:")
print(rivers)

# Removendo elementos das listas

# Del
del languages[4]
print("\nLista de linguagens após a remoção do Árabe:")
print(languages)

# Pop() para remoção do último item
popped_countries = countries.pop()
print(f"\nLista após a remoção da {popped_countries}")
print(countries)

# Pop() para remoção de qualquer posição
my_language = languages.pop(0)
print(f"\nEu falo {my_language}.")
print("Lista de linguagens atualizada:")
print(languages)

# Remove()
removed_montain = "Denali"
montains.remove(removed_montain)
print(f"\nLista após a remoção da montanha {removed_montain}:")
print(montains)

# Organinando uma Lista

# Sort()
rivers.sort()
print("\nLista de rios em ordem alfabética permanente:")
print(rivers)

# Sort() com reverse
cities.sort(reverse=True)
print("\nLista de cidades em ordem alfabética mas de trás pra frente:")
print(cities)

# Sorted()
print(f"\nLista de linguagens na ordem original:\n{languages}")
print("Lista com sorted (temporária):")
print(sorted(languages))
print(
    f"Novamente, a lista original para demonstrar que a lista não mudou permanentemente:\n{languages}"
)

# Reverse()
print(f"\nLista de monstanhas original:\n{montains}")
montains.reverse()
print(f"Lista de montanhas após reverse (permanente):\n{montains}")

# Encontrando o tamanho da lista
for places in montains, rivers, countries, cities, languages:
    print(f"\nTamanho da lista {places}: {len(places)}")
