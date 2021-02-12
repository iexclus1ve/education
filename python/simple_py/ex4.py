poem = '''When an eel grabs your arm,
And it causes great harm,
That's - a moray!'''
poem_list = poem.split(' ')

print(poem.replace(' m', ' M'))

for word in poem_list:
    if word.startswith('m'):
        x = (poem_list.index(word))
        poem_list[x] = word.capitalize()
        poem = ' '.join(poem_list)
        print(poem)

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

print(questions[0], answers[1])
print(questions[1], answers[2])
print(questions[2], answers[0])


eat1 = 'roast beef'
eat2 = 'ham'
var1 = 'head'
var2 = 'clam'

vars_dict = {'var1': 'head', 'var2': 'clam', 'eat1': 'ham', 'eat2': 'roastbeef'}

poem2 = "\nMy kitty cat likes %s,\n\
My kitty cat likes %s,\n\
My kitty cat fell on his %s\n\
And now thinks he's a %s." %(eat1, eat2, var1, var2)

print(poem2)

poem2a = "\nMy kitty cat likes {0[eat1]},\n\
My kitty cat likes {0[eat2]}\n\
My kitty cat fell on his {0[var1]}\n\
And now thinks he's a {0[var2]}".format(vars_dict)

print(poem2a)

poem2b = f"\nMy kitty cat likes {eat1 =}\n\
My kitty cat likes {eat2 =},\n\
My kitty cat fell on his {var1}\n\
And now thinks he's a {var2.upper()}."

print(poem2b)