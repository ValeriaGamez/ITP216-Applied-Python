# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 5
# prints information about athletets

# absolute import
import athlete
#print('In Main: the script\'s __name__ is', __name__)


def main():
    boxer1 = athlete.Boxer('Mary Berry', '1935/03/24', 'UK', ['Gold(2012)', 'Gold(2016)'], 'Light Flyweight')
    swimmer1 = athlete.Swimmer('Dave Thomas', '1932/07/02', 'USA', ['Silver(1992)', 'Gold(1995)'], ['freestyle', 'breaststroke'])
    print(boxer1)
    print(swimmer1)


if __name__ == '__main__':  # only run main if running this file directly and not importing it
    main()
