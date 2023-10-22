class Student:
    def __init__(self, name_param, ID_param):
        self.name = name_param
        self.ID = ID_param

def main():
    grace = Student("Grace", 65859)

    print(type(grace))

if __name__ == '__main__':
    main()