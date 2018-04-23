import random

file1 = open('animals.txt','r')
file2 = open('first_names.txt','r')
file3 = open('adjectives.txt','r')

animals = []
names = []
adjectives = []
test = ['yes', 'no', 'maybe', 'so']

for animal in file1.readlines():
    animal = animal.rstrip()
    animals.append(animal)

for name in file2.readlines():
    name = name.rstrip()
    names.append(name)

for adjective in file3.readlines():
    adjective = adjective.rstrip()
    adjective = adjective.capitalize()
    adjectives.append(adjective)

short_animals = []
short_names = []
short_adjectives = []
for x in animals:
    if len(x) < 7:
        short_animals.append(x)

for x in names:
    if len(x) < 7:
        short_names.append(x)

for x in adjectives:
    if len(x) < 7:
        short_adjectives.append(x)


def get_random(list):
    for i in range(len(list)):
        random_num = random.randrange(len(list) - 1)
        random_num = random_num + 1 if random_num >= i else random_num
    return random_num

print(len(short_names))
print(len(short_adjectives))
print(len(short_animals))

print(short_names[get_random(short_names)]+"The"+short_adjectives[get_random(short_adjectives)]+short_animals[get_random(short_animals)])
