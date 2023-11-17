"""Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches."""

## Pastrami not available
sandwich_orders=['Pastrami','Potato', 'Cheese', 'Tuna', 'Chicken']
finished_sandwiches=[]
print("I'm so sorry, Pastrami is not available.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I have made a " + sandwich + " sandwich.")
