# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 4
# Description: creates a class Barbarian that inherits from Player

# Barbarian - a player that uses Rage
# Their power is based on the number of rage_points they have
import random

from Player import Player


class Barbarian(Player):
    # class attributes
    Barbarian_count = 0

    def __init__(self, name_param: str, color_param: str, health_points_param: int, rage_points_param: int):
        """
        Constructs new Barbarian object
        :param name_param:
        :param color_param:
        :param health_points_param:
        :param rage_points_param:
        """
        super().__init__(Player)
        self.name = name_param
        self.color = color_param
        self.health_points = health_points_param
        self.rage_points = rage_points_param

    def __str__(self):
        return ('The ' + self.color + ' ' + self.name + ' barbarian has '
                + str(self.health_points) + ' health points and ' + str(self.rage_points) + ' rage points')

    def get_rage_points(self):
        """
        retrieves Barbarian rage points count
        :return:
        """
        return self.rage_points

    def get_power(self):
        """
        retrieves power of the Barbarian
        :return:
        """
        return self.health_points + self.rage_points

    def lose_fight(self):
        """
        Barbarian potentially loses health_points and rage_points.
        Based on the number of existing rage_points, randomly generate a number
        and lose that number of rage points, update self.rage_points instance attribute
        :return:
        """
        super().lose_fight()
        rand_num_rp_to_lose = min(random.randint(1, self.rage_points), random.randint(1, 20))
        self.rage_points = self.rage_points - rand_num_rp_to_lose
