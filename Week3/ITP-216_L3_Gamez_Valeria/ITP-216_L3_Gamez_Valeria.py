# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Lab 3
# Description: Program reads the contents of csv into variables.
# It prints all the data out.

def file_read_header(file_name):
    """
    Description: Retrieves first line from a text file
    :param file_name:
    :return: first line of the file(string)
    Side Effects:
    """
    f_in = open(file_name, 'r')
    headers = f_in.readline()
    f_in.close()
    return headers


def file_read_data(file_name: str) -> list[str]:
    """
    Description: Retrieves all data from text file except first line
    :param file_name:
    :return: list with all data from file
    """
    f_in = open(file_name, 'r')
    f_in.readline()
    data: list[str] = []
    for line in f_in:
        line = line.strip()
        if line: # if the string is non empty len(line)>0
            data.append(line)
    f_in.close()
    return data


def main():
    """ Loads file contents into two variables by calling their functions.
        Then prints the header row and iterates through and prints the rest of the data """
    print('Header:')
    headers = file_read_header('oscar_age_female.csv')
    print('\t' + headers)
    print('Data:')
    data = file_read_data('oscar_age_female.csv')
    for line in data:
        print('\t' + line)


if __name__ == '__main__':
    main()
