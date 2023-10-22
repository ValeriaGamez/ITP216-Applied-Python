print('In Fish: the script\'s __name__ is', __name__)

class Red:
    def __init__(self, name_param):
        self.name = name_param

    def __str__(self):
        return 'I\'m a Red fish and my name is ' + self.name

    def crazy_biz_logic_method(self, a, b, c):
        return a + b + c

class Blue:
    def __init__(self, name_param):
        self.name = name_param

    def __str__(self):
        return 'I\'m a Blue fish and my name is: ' + self.name

def main():
    print('here is some unit tests for Fish:')
    red1 = Red('red1') # calls __init__()
    blue1 = Blue('blue1')
    print(red1) # calls __str__()
    input1 = [0, 0, 0]
    red1.crazy_biz_logic_method(input1[0], input1[1], input1[2])
    input2 = [1, 1, 1]
    red1.crazy_biz_logic_method(input2[0], input2[1], input2[2])


if __name__ == '__main__':
    main()
