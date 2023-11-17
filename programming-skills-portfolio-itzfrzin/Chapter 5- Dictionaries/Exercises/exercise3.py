"""Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output."""


Program={
'loop': 'Work through a collection of items, one at a time.',
'dictionary': "A collection of key-value pairs.",
'key': 'The first item in a key-value pair in a dictionary.',
'value': 'An item associated with a key in a dictionary.',
'conditional test': 'A comparison between two values.',
'float': 'A numerical value with a decimal component.',
'boolean expression': 'An expression that evaluates to True or False.',
'string': 'A series of characters.',
'comment': 'A note in a program that the Python interpreter ignores.',
'list': 'A collection of items in a particular order.',}
for word, definition in Program.items():
    print("\n" + word.title() + ": " + definition)

    


    