"""A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

their meanings as values.

* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

each word-meaning pair in your output."""


Subject={
    'Operator': 'Operators are used to perform operations on variables and values.',
    'String': 'A series of characters.',
    'Loop': 'Work through a collection of items, one at a time.',
    'Dictionary': "A collection of key-value pairs.",
    'Tuple':'Tuples are used to store multiple items in a single variable.',}
Program='Operator'
print("\n" + Program.title() + ":" + Subject[Program])
Program='String'
print("\n" + Program.title() + ":" + Subject[Program])
Program= 'Loop'
print("\n" + Program.title() + ":" + Subject[Program])
Program= 'Dictionary'
print("\n" + Program.title() + ":" + Subject[Program])
Program= 'Tuple'
print("\n" + Program.title() + ":" + Subject[Program])



