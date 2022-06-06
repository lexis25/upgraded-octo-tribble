# hausaufgabe 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']


# print(good())


# hausaufgabe 9.2
def get_odds():
    count = 0
    for number in range(10):
        if number % 2 != 0:
            count += 1
            if count == 3:
                return number


print(get_odds())

# hausaufgabe 9.3
def test():
    def start_test():
        print('start')
    start_test()
    print('end')

test()

# hausaufgabe 9.4 (p/s i hate Bill Lubanovich MZFK(((( )
class OopsException(Exception):
    pass
numbers = [1,2]
for index in numbers:
    if index == 3:
        print('Caught.an.oops')
        raise OopsException(index)

try:
    raise OopsException(3)
except OopsException as exc:
    print(exc)