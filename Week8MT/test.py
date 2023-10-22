class Dessert:
    def __init__(self, name_param):
        self.name = name_param

    def __str__(self):
        return ('The dessert is ' + self.name)

    def get_name(self):
        return self.name

    def set_name(self, ice_cream_param):
        self.name = ice_cream_param.name


class IceCream(Dessert):


    def __init__(self):
        super().__init__(Dessert)
        self.name = 'ice cream'
        self.flavor = 'Vanilla'

    def __str__(self):
        return ('The dessert is ' + self.name + ' and the flavor is ' + self.flavor)

    def get_flavor(self):
        return self.flavor

    def set_flavor(self, flavor_param: str):
        self.flavor = flavor_param


def main():
    dessert = Dessert('lollipop')
    print(dessert)
    print(dessert.get_name())
    print()
    ice_cream1 = IceCream()
    print(ice_cream1)
    print(ice_cream1.get_flavor())
    ice_cream1.set_flavor('chocolate')
    print(ice_cream1.get_flavor())


    dessert.set_name(ice_cream1)
    print('new name for dessert is:', dessert.get_name())


if __name__ == '__main__':
    main()

