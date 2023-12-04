import pandas as pd
import numpy as np
import random

adj = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']

noun = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase():
    adjective = random.choice(adj)
    nouns = random.choice(noun)
    return adjective + ' ' + nouns

# print(random_phrase())


def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

# print(random_float(3, 7))


def random_bowling_score():
    return random.randint(0, 300)

# print(random_bowling_score())


def silly_tuple():
    return (random_phrase(), round(random_float(1, 5), 1),
            random_bowling_score())

# print(silly_tuple())


def silly_tuple_list(num_tuples):
    res = []
    for _ in range(num_tuples):
        res.append(silly_tuple())
    return res

# print(silly_tuple_list(2))

# mod 1 part 3 ---------------------------------------------------------------


d = np.array([[4, 1], [7, 3], [2, 7], [5, 6], [7, 5],
              [4, 8], [3, 2], [0, 6], [6, 2], [8, 9]])
df = pd.DataFrame(d)


def train_test_split(df, frac):
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1)
    return train, test

# print(train_test_split(df, 0.8))


addys = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785',
                                  '8394 Kim Meadow\nDarrenville, AK 27389',
                                  '379 Cain Plaza\nJosephburgh, WY 06332',
                                  '5303 Tina Hill\nAudreychester, VA 97036']})


def addy_split(addys):
    df = pd.DataFrame()

    line1 = []
    city = []
    state = []
    zipcode = []

    for addy in addys['address']:
        line_1, line_2 = addy.split('\n')
        line1.append(line_1)
        city_bit, next_bit = line_2.split(',')
        city.append(city_bit)
        state.append(next_bit.split()[0])
        zipcode.append(next_bit.split()[1])

    df['street'] = line1
    df['city'] = city
    df['state'] = state
    df['zip'] = zipcode
    return df

# print(addy_split(addys))
