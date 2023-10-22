# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 5
# Description:
# Represents a boxer athlete

# Relative import
from .Athlete import Athlete


class Swimmer(Athlete):

    swimmer_count = 0

    def __init__(self, name_param: str, dob_param: str, origin_param: str, medals_param: list, strokes_param: list):
        super().__init__(str(Athlete), dob_param, origin_param, medals_param)
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        self.strokes = strokes_param
        Swimmer.swimmer_count += 1

    def __str__(self):
        return (self.name + 'is a swimmer from ' + self.origin + ' born on ' + self.dob + '.' + self.name + ' knows ' +
                str(self.strokes) + ', and has won ' + str(len(self.medals)) + ' medals: ' + str(self.medals))

    def get_strokes(self):
        """
        Retrieves the strokes attribute
        :return:
        """
        return self.strokes

    def add_stroke(self, stroke_param):
        """
        adds a new stoke to the swimmers repertoire, checks to make sure the stroke is not already in the list
        :param stroke_param:
        :return:
        """
        if stroke_param not in self.strokes:
            self.strokes.append(stroke_param)
