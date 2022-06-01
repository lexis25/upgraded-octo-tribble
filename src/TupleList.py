# hausaufgabe 7.1
yeas_list = [1983, 1984, 1985, 1986, 1987, 1988]

# hausaufgabe 7.2
print(yeas_list[3])

# hausaufgabe 7.3
print(yeas_list[-1])

# hausaufgabe 7.4
things = ['mozzarella', 'cinderella', 'salmonella']

# hausaufgabe 7.5
things[1] = 'Cinderella'

# hausaufgabe 7.6
cheese = things[0].upper()
del things[0]
things.append(cheese)

# hausaufgabe 7.7
index = things.index('salmonella')
del things[index]
print(things)

# hausaufgabe 7.8
surprise = ['Groucho', 'Chico', 'Harpo']

# hausaufgabe 7.9
name = surprise.pop(-1)
pre = name[::-1].lower()
name = pre[0].upper() + pre[1:]
surprise.insert(3, name)
print(surprise)

# hausaufgabe 7.10
even = []
for number in range(10):
    if number % 2 == 0:
        even.append(number)
del even[0]
print(even)