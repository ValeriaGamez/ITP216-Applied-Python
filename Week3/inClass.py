def flower(num_petals, color='red'):
    print('I love', color, 'flowers with', num_petals, 'petals!')
    return color * num_petals


flower(num_petals=6, color='green')
flower(7)
flower(num_petals=8, color='blue')

