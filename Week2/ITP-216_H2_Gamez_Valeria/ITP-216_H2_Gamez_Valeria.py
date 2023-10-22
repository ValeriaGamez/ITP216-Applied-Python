# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 2
# Description:
# asks the user if they want to see their pets or add a pet

def main():
    # your code goes here
    cats_names = ('Cassandra', 'Sir Whiskington', 'Truck')  # tuple
    dogs_names = {'Barkey McBarkface', 'Leeloo Dallas', 'Taro'}  # dict
    parrots_names = ['Squawk', 'Squawk 2: the Squawkquel', 'Larry']  # list
    names = ['peter', 'paul', 'mary']
    animal_types = ('cat', 'cat', 'hamster')

    # create directory to hold all animal types
    animals_dict = {'cat': list(cats_names), 'dog': dogs_names, 'parrot': parrots_names}

    for i in range(len(animal_types)):
        if animal_types[i] not in animals_dict:
            animals_dict[animal_types[i]] = [names[i]]
        else:
            animals_dict[animal_types[i]].append(names[i])

    # for k, v in animals_dict.items():
    # print(k, ":", v)

    # create new list with just cats, it updates cats
    cats = animals_dict.get('cat')
    animals_count = 0

    input("Hi", )
    while True:
        print("Please choose from the following options:")
        print("1. See all your pets' names.")
        print("2. Add a pet.")
        print("3. Exit")
        choice = input("What would you like to do? (1, 2, 3): ")

        if choice == "1":
            # print all pets

            # Iterate through the dictionary and its lists
            for key, value in animals_dict.items():
                animals_count += len(value)
            print("You have", animals_count, "pets")

            # iterate to print key and value
            for key, value in animals_dict.items():
                print(key, ":", value)

            animals_count = 0
        elif choice == "2":
            # add pet
            new_animal = (input("What kind of animal is this?: ")).strip()
            new_name = (input("What is the name of the " + new_animal + "? ")).strip()

            if new_animal not in animals_dict:
                animals_dict[new_animal] = [new_name]
            else:
                animals_dict[new_animal].append(new_name)

            print("Great!", new_name, "the", new_animal, "is now added to your pets.")
        elif choice == "3":
            # exit
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again...")


if __name__ == '__main__':
    main()
