# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 4
# Description: creates a class Wizard that inherits from Player

# Wizard - a player that uses Magic
# power is based on the number of magic_points they have

from Player import Player


class Wizard(Player):

    # Class Attributes
    Wizard_count = 0

    # Instance methods
    def __init__(self, name_param: str, color_param: str, health_points_param: int, magic_points_param: int):
        """
        Constructs a new Wizard object
        :param name_param:
        :param color_param:
        :param health_points_param:
        :param magic_points_param:
        """
        super().__init__(Player)
        self.name = name_param
        self.color = color_param
        self.health_points = health_points_param
        self.magic_points = magic_points_param
        Wizard.Wizard_count += 1

    def __str__(self):
        """
        Retrieves data about the Wizard when printing
        :return:
        """
        return ('The ' + self.color + self.name + ' wizard has '
                + str(self.health_points) + ' and ' + str(self.magic_points) + ' magic points ')

    def get_magic_points(self):
        """
        Retrieves the Wizard's number of magic_points
        :return:
        """
        return self.magic_points

    def get_power(self):
        """
        Retrieves the power of the Wizard
        :return:
        """
        return self.health_points + self.magic_points
