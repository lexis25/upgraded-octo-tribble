# hausaufgabe 6.1
_list = [3, 2, 1, 0]
for number in _list:
    print(number)

# hausaufgabe 6.2
guess_me = 7
number = 1
while number <= guess_me:
    if number < guess_me:
        print('too low')
    if number == guess_me:
        print('found it')
        break
    if number > guess_me:
        print('oops')
        break
    number += 1

# hausaufgabe 6.3
guess_me = 5
for number in range(guess_me, 10):
    if number < guess_me:
        print('too low')
    if number == guess_me:
        print('found it')
        break
    if number > guess_me:
        print('oops')
        break
