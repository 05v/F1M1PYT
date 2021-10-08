import time
list1 = ["12", "worden", "True", "False", "444"]

print("Sorted the list:")
list1.sort()
print(list1)
print("")

time.sleep(2)
print("Appended the list with 'Text':")
list1.append("Text")
print(list1)
print("")

time.sleep(2)
print("Popped the list 3 times:")
list1.pop()
list1.pop()
list1.pop()
print(list1)
print("")