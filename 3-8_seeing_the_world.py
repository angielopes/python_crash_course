"""Think of at least five places in the world you'd like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order. OK
• Print your list in its original order. Don't worry about printing the list neatly;
just print it as a raw Python list. OK
• Use sorted() to print your list in alphabetical order without modifying the actual list. OK
• Show that your list is still in its original order by printing it. OK
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. O1K
• Show that your list is still in its original order by printing it again. OK
• Use reverse() to change the order of your list. Print the list to show that its order has changed. OK
• Use reverse() to change the order of your list again. Print the list to show it's back to its original order. OK
• Use sort() to change your list so it's stored in alphabetical order.
Print the list to show that its order has been changed. OK
• Use sort() to change your list so it's stored in reverse-alphabetical order.
Print the list to show that its order has changed. OK"""

places = ["Argentina", "Peru", "Japan", "China", "France"]  # Lista original

print("Lista com sorted (Ordem alfabética e temporária):")
print(sorted(places))

print("Lista com sorted mas com reverse:")
print(sorted(places, reverse=True))

print("Lista com reverse:")
places.reverse()
print(places)

print("Lista com reverse para voltar à ordem orignial:")
places.reverse()
print(places)

print("Lista com sort (Ordem alfabética e permanente)")
places.sort()
print(places)

print("Lista com sort e reverse (Ordem alfabética reversa e permanente:)")
places.reverse()
print(places)
