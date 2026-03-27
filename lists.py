"""my_list = [1,"python",True,"python",3.12]

empty = []

my_list.append("new_item")
my_list.extend([3,2,1])
my_list.insert(0,"inserted")

print(my_list)

print(my_list.pop())
print(my_list)

my_list.remove("python")


del my_list[0]
print(my_list)

"""

"""numbers = [1,2,3,4,5]
squares = []

for i in numbers:
    if i%2 == 0:
        squares.append(i**2)

print(squares)


squares_comprehension = [i**2 for i in numbers if i%2 == 0]
print(squares_comprehension)
"""

import copy

words = ["apple", "banana","cherry","a"]

words.sort(key=len)
print(words)

list_b = words.copy()
list_b.append(1)

print(words)