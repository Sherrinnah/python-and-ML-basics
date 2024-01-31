#siz = {'firstname':'melyn', 'city':'Nairobi', 'age':'twenty-three'}
#print(f"My sister's first name is: \n{siz['firstname'].title()}")
#print(f"My sister's last name is: {siz.get('lastname','No last name given').title()}")
#location=siz['city'].title()
#print(f"She lives in {location}")
#print(f"She is {siz['age']} years old!")
#for f, s in siz.items():
#    print(f"My sister's {f} is {s.title()}.")
#for f in sorted(siz.keys()):
#    print (f)


#dog1 = {'kind': 'husky', 'owner': 'dorothy'}
#dog2 = {'kind': 'corgi', 'owner': 'brady'}
#dog3 = {'kind': 'german shepherd', 'owner': 'max'}

#dogs = [dog1, dog2, dog3]

#for dog in dogs:
#    print(f"\nThis dog is a {dog['kind']}")
#    print(f"The dog's owner is {dog['owner'].title()}")
#favourite_numbers = {'Anne':[1, 3, 5], 'Jeanne':[10], 'Alvin':[2, 4], 'Jill': [7,12]}
#for name, numbers in favourite_numbers.items():
#    if len(numbers) < 2:
#        print(f"This is {name.title()}'s favourite number:")
#        for number in numbers:
#            print(f"\t{number}")
#
#    elif len(numbers) >= 2:
#        print(f"These are {name.title()}'s favourite numbers:")
#        for number in numbers:
#            print(f"\t{number} ")
cities = {'Nairobi':
        {'country': 'kenya',
         'population': '6 million',
         'fact':'The name hails from Maasai language'},
        'Lagos': 
        {'country': 'nigeria',
         'population': '22 million',
         'fact':'It has houses on land reclaimed from the sea'} }
for city, trait in cities.items():
    print(f"These are facts about {city}")
    print(f"\tIt is located in {trait['country'].title()}.")
    print(f"\tIts population is {trait['population'].title()}.")
    print(f"\tOne fact about it is: {trait['fact']}.")