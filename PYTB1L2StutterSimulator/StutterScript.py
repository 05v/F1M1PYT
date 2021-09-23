word = input("Enter a sentance to stutter: ")

def stutter(word):
    if len(word) > 3:
     print (word[0:2]+ "... " + word[0:2]+ "... " + word)

stutter(word)