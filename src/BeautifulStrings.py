# hausaufgabe 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
song = song[0:65] + "" + (song[-6].upper() + song[-5:])
print(song)

# hausaufgabe 5.2
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

print(questions[0] + ' ' + answers[1])
print(questions[1] + ' ' + answers[2])
print(questions[2] + ' ' + answers[0])

# hauseaufgabe 5.3
'My kitty cat likes %s,' % 'roast beef'
'My kitty cat likes %s,' % 'ham'
'My kitty cat fell on his %s' % 'head'
'And now thinks he\'s a %s' % 'clam.'

# hauseaufgabe 5.4 - 5.5
salutation = 'client'
name = 'Morty'
product = 'egg cutter'
verbed = 'heavy'
room = 'kitchen'
animals = 'a lion'
amount = 'one'
percent = '35'
spokesman = 'mr. Greed'
jobTitle = 'Universal Mind cp.'

letter = """Dear {} {},
Thank you for your letter. We are sorry that our {}
{} in your {}. Please note that it should never
be used in a {}, especially near any {}.
Send us your receipt and {} for shipping and handling.
We will send you another {} that, in our tests,
is {}% less likely to have {}.
Thank you for your support.
Sincerely,
{}
{}"""

print(letter.format(salutation, name, product, verbed, room, room, animals,amount, product, percent, verbed, spokesman,jobTitle))
