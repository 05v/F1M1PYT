
list = ["Geld", "12", "True", "Banaan", "777"]

inputlist = input("What do you want to print, ALL , WORDS , NUMBERS, TRUEFALSE: ")
if inputlist == "ALL":
    print(list)


elif inputlist == "WORDS":
    words = []
    for item in list:
        for subitem in item.split():
            if not (subitem.isdigit()) or not ("True") or not "False":
                words.append(subitem)
    print(words)


elif inputlist == "NUMBERS":
    numbers = []
    for item in list:
        for subitem in item.split():
            if(subitem.isdigit()):
                numbers.append(subitem)
    print(numbers)


elif inputlist == "TRUEFALSE":

    for i in list:
        if (i == "True" or i == "False"):
            print(i)
