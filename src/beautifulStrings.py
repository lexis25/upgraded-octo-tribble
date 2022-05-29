#hausaufgabe 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
song = song[0:65] + "" + (song[-6].upper() + song[-5:])
print(song)