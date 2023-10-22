# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 5
# Description:
# Represents a boxer athlete

# Relative import
from .Athlete import Athlete


class Boxer(Athlete):
    boxer_count = 0

    def __init__(self, name_param, dob_param: str, origin_param: str, medals_param: list, weight_class_param: str):
        """
        Constructs new Boxer Object
        Assigns params to instance atts
        Inc boxer_count by 1
        :param name_param:
        :param dob_param:
        :param origin_param:
        :param medals_param:
        :param weight_class_param:
        """
        super().__init__(str(Athlete), dob_param, origin_param, medals_param)
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        self.weight_class = weight_class_param
        self.record = [0, 0]
        Boxer.boxer_count += 1

    def __str__(self):
        """
        retrieves data about boxer when printing
        :return: str about boxer
        """
        return (self.name + ' is a ' + self.weight_class + ' boxer from ' + self.origin + ' born on ' + self.dob + '. ' +
                self.name + ' has a ' + str(self.record[0]) + '-' + str(self.record[1]) + ' record, and has won ' + str(len(self.medals)) +
                ' medals: ' + str(self.medals))

    def set_weight_class(self, weight_class_param):
        """
        sets weight class attribute
        :param weight_class_param:
        :return:
        """
        self.weight_class = weight_class_param

    def win_fight(self):
        """
        adds one to the wins of the boxer's records
        :return:
        """
        self.record[0] += 1

    def lose_fight(self):
        """
        adds one to the loses of the boxer's record, then checks to see if boxer needs to retire after 10 losses
        :return: A message about the number of fights left before retirement, or 'This boxer has retired.'
        """
        self.record[1] += 1
        if self.record[1] >= 10:
            return 'This boxer has retired'
