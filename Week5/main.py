# from Fish import Red, Blue
import Fish

print('In Main: the script\'s __name__ is', __name__)

def main():
    red1 = Fish.Red('red1')
    blue1 = Fish.Blue('blue1')
    print(red1)
    print(blue1)

if __name__ == '__main__':  # only run main if running this file directly and not importing it
    main()