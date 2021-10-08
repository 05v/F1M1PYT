import time

stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"] 

strings = []
integers = []
floats = []
booleans = []
    
# Print alleen de strings van stuff
for stringlist in stuff:
    if(type(stringlist) == str):
        strings = stringlist
        print(strings)

time.sleep(1)
print("\n")

# Print alleen de integers van stuff
for intlist in stuff:
    if(type(intlist) == int):
        integers = intlist
        print(integers)
        
time.sleep(1)
print("\n")

# Print alleen de floats van stuff
for floatlist in stuff:
    if(type(floatlist) == float):
        floats = floatlist
        print(floats)
        
time.sleep(1)
print("\n")

# Print alleen de booleans van stuff
for boollist in stuff:
    if(type(boollist) == bool):
        booleans = boollist
        print(booleans)