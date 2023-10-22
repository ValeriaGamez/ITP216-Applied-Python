# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 5
# Description: __init__ file


__all__ = ['Athlete', 'Boxer', 'Swimmer']  # The modules that get imported when import *
from .Swimmer import Swimmer
from .Boxer import Boxer

# if __name__ == '__main__':
#     print('This is the athlete package __init__ file. Why are you running it?')
