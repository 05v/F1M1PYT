import time
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

run = True
while run:
    clearConsole()

    factory = ["Banana", "Apple"]
    distribution = []
    shop = []

    print("Factory:", factory)
    print ("Distribution:", distribution)
    print("Shop:", shop)
    time.sleep(2)
    clearConsole()

    distribution = factory.copy()

    while len(factory) > 0:
        factory.pop()

    print("Factory:", factory)
    print ("Distribution:", distribution)
    print("Shop:", shop)
    time.sleep(2)
    clearConsole()

    shop = distribution.copy()

    while len(distribution) > 0:
        distribution.pop()


    print("Factory:", factory)
    print ("Distribution:", distribution)
    print("Shop:", shop)
    time.sleep(2)
    clearConsole()

    YNinput = input("Run again Y/N: ")
    if YNinput == "Y" or YNinput == "y":
        run = True
    elif YNinput == "N" or YNinput == "n":
        run = False
    else:
        print("That's not an option, try again...")