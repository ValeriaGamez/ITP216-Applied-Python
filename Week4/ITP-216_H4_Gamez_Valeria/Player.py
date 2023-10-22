# Valeria Gamez
# vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 4
# Description: Creates a Player class

# Class Player
import random


class Player:
    # Class Attributes
    # 1. Player_count
    Player_count = 0
    # a. The number of Players created.
    # Instance Attributes
    # 1. self.name
    # a. The name of the Player (string)
    # 2. self.health_points
    # a. The number of health_points the Player has (int)
    # 3. self.color
    # a. The color of the Player’s clothes (String)
    # Instance Methods
    # 1. __init__()
    # a. Description: Constructs a new Player object
    # b. Parameters: 3
    # i. name_param (String)
    # ii. color_param (String)
    # iii. health_points_param (int)
    # c. Returns 0
    # d. Assigns parameters to instance attributes. Increases Player Player_count by 1.

    def __init__(self, name_param=None, health_points_param=None, color_param=None):
        self.name = name_param
        self.health_points = health_points_param
        self.color = color_param

    # 2. __str__()
    # a. Description: Returns a string representation of the Player object to be used to print out the Player for human
    # consumption.
    # b. Parameters: None
    # c. Returns a string representation of the Player object
    # d. Should show the current state / value of each attribute.
    def __str__(self):
        return ("I'm a Player and my name is: " + self.name + " and I have "
                + str(self.health_points) + " health points and my clothes are colored: "
                + self.color)

    # 3. get_name()
    # a. Description: Retrieves Player name.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.name instance attribute
    def get_name(self):
        return self.name

    # 4. get_color()
    # a. Description: Retrieves Player color.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.color instance attribute
    def get_color(self):
        return self.color

    # 5. get_health_points()
    # a. Description: Retrieves Player health_points.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.health_points instance attribute
    def get_health_points(self):
        return self.health_points

    # 6. set_color()
    # a. Description: Changes Player color.
    # b. Parameters: 1
    # i. A color (String)
    # c. Returns: 0
    def set_color(self, new_color):
        self.color = new_color

    # 7. lose_fight()
    # a. Description: Player potentially loses health_points.
    # b. Parameters: 0
    # c. Returns: 0
    # d. Based on the number of existing health_points, randomly generate a number and lose that number of
    # health_points. update self.health_points instance attribute.
    def lose_fight(self):
        rand_num_hp_to_lose = min(random.randint(1, self.health_points), random.randint(1, 20))
        self.health_points = self.health_points - rand_num_hp_to_lose

# 8. main()
# a. Description: a main function that calls all of the above methods
# b. Parameters: 0
# c. Returns: 0
# d. Creates an object of class Player and calls all of its methods.


def main():
    player1 = Player('Greg the Wizard', 100, 'Trojan Red')
    print(player1)  # calls __str__()
    player1.get_name()
    print('before fight:', player1.get_health_points())
    player1.lose_fight()
    print('after fight:', player1.get_health_points())


if __name__ == '__main__':
    main()
