# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 3
# Description:
# Program reads data from csv file into variables
# and calculates Robert Deniro's average Rotten
# and makes a list with all the movies rated above avg.

def file_reader(file_name):
    """
   Description: Retrieves the entire contents of a text file.
   :param file_name: string
   :return: 2, header from file (list), All data from file(list)
   """
    f_in = open(file_name)
    header_line = f_in.readline().strip().split(',')  # entire str with all headers, each header is an item in a list

    data = []  # create empty string list for rest of data

    for line in f_in:
        line = line.strip()  # delete trailing and leading whitespace in each line
        if line:  # if line is not empty
            data.append(str(line).split(','))  # every item separated by a comma becomes an item in list
    f_in.close()
    return header_line, data


def calculate_mean(scores: list[int]):
    """
   Description: Calculates the average value of a collection of scores
   :param scores: (list)
   :return: the mean score(float)
   """
    suma = 0
    for score in scores:
        suma += float(score)  # add all scores
    mean_score = suma/len(scores)  # divide by number of scores

    return mean_score


def find_movies_above_score(data, mean_score: float):
    """
    Description: from an initial list, retrieves a list of all the movies with scores above a certain value
    :param data:
    :param mean_score:
    :return: A collection of all movies
    - in the format of [year, score, title]
    - with a score above the given score(list)
    """
    above_avg = []
    for movie in data:  # iterate through all data
        if len(movie) >= 2:
            if int(movie[1]) >= mean_score:
                above_avg.append(movie)  # add movie to the new list with only the ones above average
    return above_avg


def main():
    """
   Loads the contents of the file into two variables,
   and then analyzes that data and presents the results on the console.
   """
    print('I love Robert Deniro!')

    headers, data = file_reader('deniro.csv')

    scores = []  # Create array for just the scores to pass as parameter to calculate mean_scores
    for movie in data:
        if len(movie) >= 2:  # if there are more than 2 elements in movie[]
            scores.append(int(movie[1]))

    avg = calculate_mean(scores)
    above_avg = find_movies_above_score(data, avg)

    print('The average Rotten Tomatoes score for his movies is', avg)
    print('Of', len(data), 'movies,', len(above_avg), 'are above average')
    print('Here they are:')

    for header in range(len(headers)):
        print('\t ' + headers[header].strip('"').replace('"', ' '), end=' ')

    print()
    for movie in above_avg:
        if len(movie) >= 2:
            if len(movie) == 4:  # if there are four "columns"
                print('\t ' + str(int(movie[0])) + '\t    ' + str(int(movie[1])) + '\t    ' +
                      movie[2].strip().replace('"', '') + movie[3].strip().replace('"', ''))
            elif len(movie) >= 2:
                print('\t ' + str(int(movie[0])) + '\t    ' + str(int(movie[1])) + '\t    ' +
                      movie[2].strip().replace('"', ''))


if __name__ == '__main__':
    main()
