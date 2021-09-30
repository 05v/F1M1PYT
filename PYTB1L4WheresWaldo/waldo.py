import random

people = ["Waldo", "Jackson", "Ray", "Eric", "Vaughn", "Jesse", "Herbert", "Robert", "Rodrigo", "Elija", "Sasha", "Nathaniel", "Ellie", "Allison", "Jeremiah", "Paula", "Alisha", "Tory", "Troy", "Faye"]
random.shuffle(people)

count=0

i = 0

while(people[i] != "Waldo"):
    count +=1
    print ([i])
    i += 1
    
print("Waldo zit op plaats ", i)