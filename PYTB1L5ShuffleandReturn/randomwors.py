
import random

def randomWord(original):
    randomised = ''.join(random.sample(original, len(original)))
    print("\n")
    print(randomised)


print("Enter a word: \n")
randomWord(input())

print("Enter a 2nd word: \n ")
randomWord(input())

print("Enter a 3rd word: \n")
randomWord(input())
