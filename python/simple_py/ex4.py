poem = '''When an eel grabs your arm,
And it causes great harm,
That's - a moray!'''

poem_list = (poem.split(' '))

for word in poem_list:
    if word.startswith('m'):
        x = (poem_list.index(word))
        poem_list[x] = word.capitalize()
        poem = ' '.join(poem_list)
        print(poem)