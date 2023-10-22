def outer(n):
    outer_func_variable = 5
    def inner_one():
        return 'I\'m number one'

    def inner_two():
        return 'I\'m number two'
    if n == 1:
        return inner_one
    elif n == 2:
        return inner_two


def main():
    first = outer(1)   # first = inner_one (function reference)
    second = outer(2)  # second = inner_two (function reference)
    # print(first())     # calls first, which points to inner_one
    # print(second())
    print(outer(1)())  # outer(1) returns/becomes -> inner_one function object/pointer/reference
    print(dir(outer))


if __name__ == '__main__':
    main()
