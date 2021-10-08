
wordfull = "Hallo ik ben een string en ik wordt opgegeten"


#pak alle characters in de string behalve de laatste en sla deze op in ss

i = 1

while len(wordfull) > 0:
    word_1 = wordfull[0:len(wordfull) - i]
    print(word_1)
    i += 1
    if len(word_1) == 0:
        exit()