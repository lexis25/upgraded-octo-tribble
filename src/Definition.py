# hausaufgabe 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

# hausaufgabe 9.2
def get_odds():
    count = 0
    for number in range(10):
        if number % 2 != 0:
            count += 1
            if count == 3:
                yield number

print(get_odds())