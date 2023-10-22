flavors = ["mint chocolate chip", 'coffe', 'french vanilla', 'strawberry',
           'green tea', 'chocolate chip cookie dough', 'chocolate chip fudge brownie', 'butter pecan']

choco = []
for flavor in flavors:
    if 'chocolate' in flavor:
        choco.append(flavor + ' is the best!')

print(choco)

def tag_best(flavor_param: str):
    return flavor_param + ' is the best!'

def has_choco(flavor_param: str):
    return 'chocolate' in flavor_param




print(choco)
