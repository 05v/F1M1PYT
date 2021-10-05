import random

def randomWord():
    word = input("Enter a word: ")
    print(random.shuffle(word))

print(randomWord())