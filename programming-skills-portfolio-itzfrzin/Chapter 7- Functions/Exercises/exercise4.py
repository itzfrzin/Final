"""Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message."""

##Large shirt
def make_shirt(size='large', message='I love Python'):
    print("\nI am gonna make a " + size + " t-shirt.")
    print('It will be printed as,"' + message + '"')
make_shirt()

##Medium shirt
make_shirt (size='medium')

##Small shirt
make_shirt('small','I love Python')