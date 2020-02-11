import math

Users = {
    'Sarah': {
        'comedy': 3,
        'thriller': 4,
        'drama': 4,
        'horror': 1,
        'melodrama': 4
    },
    'Bob': {
        'comedy': 4,
        'thriller': 3,
        'drama': 5,
        'horror': 1,
        'melodrama': 5
    },
    'John': {
        'comedy': 2,
        'thriller': 5,
        'drama': 1,
        'horror': 3,
        'melodrama': 1
    }
}


def pythagorean_formula(a, b):
    """
    Pythagorean formula for finding the length
       _________________________
    |/(a1 - a2)^2 + (b1 - b2)^2
    """
    c = math.pow(a['comedy'] - b['comedy'], 2) + \
        math.pow(a['thriller'] - b['thriller'], 2) + \
        math.pow(a['drama'] - b['drama'], 2) + \
        math.pow(a['horror'] - b['horror'], 2) + \
        math.pow(a['melodrama'] - b['melodrama'], 2)

    return math.sqrt(c)


Sarah_Bob = pythagorean_formula(Users['Sarah'], Users['Bob'])
Sarah_John = pythagorean_formula(Users['Sarah'], Users['John'])
John_Bob = pythagorean_formula(Users['John'], Users['Bob'])

print(Sarah_Bob)  # 2.0 It follows that Sarah is Bob's nearest neighbor and back
print(Sarah_John)  # 4.9
print(John_Bob)  # 6.7
