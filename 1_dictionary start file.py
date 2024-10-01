import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


# dictionaries : keys have to be unique


print()
print('*****  start section 1 - print dictionary ********')
print()


print(phonebook)
print(len(phonebook))

mydict = {} # creates an empty dictionary to be able to add to
# prints: {}

mydictionary = dict(m=8, n=9)
# prints: {'m': 8, 'n': 9}

print(mydictionary)
print(mydict)



print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'chris'

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")

# python is very case sensitive
# key error = didn't find a match


print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()

# append a dictionary

print(phonebook)
phonebook['Joe'] = '555-0123'
phonebook['Chris'] = '555-4444'
print(phonebook)

# if the key already exists, it will update the value, if it doesn't exist then it will add it
# can't actually change the key

# this example adds Joe's number and adds Joe, and updates Chris' number


print()
print('*****  end section 3 ********')
print()




print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


print(phonebook)
del phonebook['Chris']
print(phonebook)

# del allows us to delete not only just the key but the value


print()
print('*****  end section 4 ********')
print()




print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for key in phonebook:
    print(f"the name is {key} and the phone number is {phonebook[key]}")
    # the {phonebook[key]} prints the value, not the key


for value in phonebook.values():
    print(value)

# .values() is useful for dictionaries - iterates through the values (in this case, the phone numbers not the names)


for item in phonebook.items():
    print(item)

# .items() gives us tuples


for k,v in phonebook.items():
    print(f"the name is {k} and the phone number is {v}")


print()
print('*****  end section 5 ********')
print()



print()
print('*****  start section 6 - using get and clear ********')
print()


#phone = phonebook['chris']
#print(phone)
phone = phonebook.get('chris', '555-0000') # option of a default (after ,)
print(phone)


print(phonebook)
phonebook.clear() # clears out your dictionary and makes it have nothing inside it
print(phonebook)



print()
print('*****  end section 6 ********')
print()




print()
print('*****  start section 7 - using pop method ********')
print()


phone = phonebook.pop('Chris', 'not found')
print(phone)
print(phonebook)



print()
print('*****  end section 7 ********')
print()





print()
print('*****  start section 8 - using popitem ********')
print()



a = phonebook.popitem()
print(a)
print(phonebook)

# pops out last element of dictionary - no randomness to it



print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()


list_of_keys = list(phonebook) #keys are alway default (midterm multiple choice)
random_key = random.choice(list_of_keys)
phone = phonebook[random_key]
print(f"The key is {random_key} and the phone number is {phone}")


phone = phonebook[random.choice(list(phonebook))]
print(phone)



print()
print('*****  end section 9 ********')
print()






