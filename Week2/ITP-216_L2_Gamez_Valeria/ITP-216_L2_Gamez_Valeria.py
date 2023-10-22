# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section:
# Lab 2
# Description: This program converts a sentence to various data types and displays them.

from collections import Counter


def count_occurrence_manual(input_str: str) -> dict:
    # manually convert to dictionary
    print("Dictionary:")
    my_dict = {}
    for c in input_str:
        if c not in my_dict:
            my_dict[c] = 1  # this is the first time seeing this letter
        else:
            my_dict[c] = my_dict[c] + 1  # add one to whatever was already there


def count_occurrence_slicker(input_str: str) -> dict:
    my_dict = {}
    for c in input_str:
        my_dict[c] = my_dict.setdefault(c, 0) + 1
        # setdefault-> returns the value at that key if its there, otherwise it sets it to 1
    return my_dict


def count_occurrence_slickest(input_str: str) -> dict:
    return Counter(input_str)


def main():
    # your code goes here
    # Get input
    user_input = input("Please enter an input to be converted:")
    print("String:", end=" ")
    for c in user_input:
        print(c, end=",")

    print()
    user_list = list(user_input)
    print("List:", end=" ")
    for c in user_list:
        print(c, end=",")

    print()
    user_tuple = tuple(user_list)
    print("Tuple:", end=" ")
    for c in user_tuple:
        print(c, end=",")

    print()
    user_set = set(user_input)
    print("Set:", end=" ")
    for c in user_set:
        print(c, end=",")

    print()
    print("Dictionary:")
    my_dict = count_occurrence_slickest(user_input)

    print(my_dict)
    for k, v in my_dict.items():
        print("\t" + k, ":", v)


if __name__ == '__main__':
    main()
