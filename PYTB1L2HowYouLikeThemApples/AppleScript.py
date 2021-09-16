import math

trees_total = 333
tree_sun = 146
trees_sun = (trees_total / 3 * 1)
tree_shadow = (146 / 100 * 80)
trees_shadow = (trees_total / 3 * 2)
total_apples = (tree_shadow * trees_shadow + trees_sun)
apples_each_total = (total_apples / 4)
apples_each = math.trunc(apples_each_total)

print("")
print("")
print("Iedereen krijgt", apples_each, "appels.")
print("")
print("")