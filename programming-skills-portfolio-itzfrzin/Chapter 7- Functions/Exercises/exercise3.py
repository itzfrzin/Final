"""Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments."""

def make_shirt(size,message):
    print("\nI am going to make a " + size + " t-shirt")
    print('It will be printed as,"' + message + '"')
make_shirt('Large', 'Cool Vibes Only')

##2nd Function
make_shirt (message="Green Land", size='Medium')


