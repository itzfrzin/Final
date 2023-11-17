
#An empty list to store the pets in
animals=[]
#Make individual pets, and store each one in the list
pet1={
    'animal type': 'peacock',
    'name': 'hany',
    'owner': 'Lily',
    'weight': 30,
    'eats': 'insects'}
animals.append(pet1)

pet2={
    'animal type': 'hen',
    'name': 'duff',
    'owner': 'Hazel',
    'weight': 3,
    'eats': 'Hen Feed',}
animals.append(pet2)

pet3={
    'animal type': 'Cat',
    'name': 'Mia',
    'owner': 'Sara',
    'weight': 10,
    'eats': 'fish',}
animals.append(pet3)

#Display information about each pet
for pet in animals:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

        