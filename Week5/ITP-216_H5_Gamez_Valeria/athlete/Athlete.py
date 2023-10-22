# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 5
# Description:
# parent class Athlete

class Athlete:
    athlete_count = 0

    def __init__(self, name_param: str, dob_param: str, origin_param: str, medals_param: list):
        """
        Constructs a new Athlete object,
        Assigns parameters to instance attributes,
        Increases athlete_count by 1
        :param name_param:
        :param dob_param:
        :param origin_param:
        :param medals_param:
        """
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        Athlete.athlete_count += 1

    # Getters for all four instance attributes
    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_origin(self):
        return self.origin

    def get_medals(self):
        return self.medals

    def add_medal(self, medal_param: str):
        """
        Adds a new medal to the medal list
        :param medal_param:
        :return: 0
        """
        self.medals.append(medal_param)
