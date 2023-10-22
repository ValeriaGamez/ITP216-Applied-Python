# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Lab 6
# Description:
# This is just a task-list based lab to get you comfortable working with comprehensions and generators.



# 1. Write a comprehension which creates a list (called sevens) consisting of all multiples of seven from 1 to
# 1000. For context: this list should be 142 items long.
sevens = [i for i in range(1,1001) if i % 7 == 0]


print(len(sevens))
print(sevens)
# 2. Write a comprehension which creates a dictionary (called birdos) consisting of the following content
# (paired currently by index):
names = ['Great potoo', 'Smew', 'Tundra bean goose', 'Southern pied babbler']
genus_and_species = ['Nyctibius grandis', 'Mergellus albellus', 'Anser serrirostris', 'Turdoides bicolor']

birdos = {name: genus for name, genus in zip(names, genus_and_species)}
print(birdos)

# 3. Write a generator expression which creates a generator (called square_gen) which will yield two values:
# a number and its square. You can test it by running the following code:
square_gen = ((i, i*i) for i in range(1, 4))
for number, square in square_gen:
    print(number, 'squared:', square)




