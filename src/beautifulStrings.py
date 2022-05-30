#hausaufgabe 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
song = song[0:65] + "" + (song[-6].upper() + song[-5:])
print(song)

#hausaufgabe 5.2
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

#hauseaufgabe 5.3
'My kitty cat likes %s,' %'roast beef'
'My kitty cat likes %s,' %'ham'
'My kitty cat fell on his %s' %'head'
'And now thinks he\'s a %s' %'clam.'
