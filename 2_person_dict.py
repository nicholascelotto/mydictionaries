person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

#print(person)

# print out the name of the second child

list_of_children = person['children']
print(list_of_children[1])

# Alternatively not using a variable
print(person['children'][1])



# print out the name of the cat
dict_of_pets = person['pets']
print(dict_of_pets['cat'])

# Alternatively not using a variable
print(person['pets']['cat'])


# use a loop to print out the names of each child
for child in person['children']:
    print(child)



# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for pet, name in person['pets'].items():
    print(f"The name of the pet is: {pet} and the name of the pet is {name}")
