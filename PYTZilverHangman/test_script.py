import random

def choose_word():
    with open('word_list.txt', 'r') as whole_list:
        list_full = [line.strip() for line in whole_list]
    random_word = random.choice(list_full)
    print(random_word)

def scramble_word():
    len_word = print(len(choose_word))
    print(len_word)
    
scramble_word()