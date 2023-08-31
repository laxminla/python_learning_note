#Exercise 1: Reverse a list in Python
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
#solution 2 using negative slicing
list2 = [60, 70, 20, 41, 28]
list2 = list2[::-1]
print(list2)

# Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

#Exercise 3: Turn every item of a list into its squre
numbers = [1, 2, 3, 4, 5, 6, 7]
#result list
res = []
for i in numbers:
    res.append(i*i)
print(res)

#Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x+y for x in list1 for y in list2]
print(res)

#Exercise 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x,y)

#Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma"]
res = list(filter(None, list1))
print(res)

#Exercise 7: Add new item to list after a specified item
#Write a program to add item 7000 after 6000 in the following Python List
# output [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

list1[2][2].append(7000)
print(list1)

#Exercise 8: Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#indexing
# understand indexing
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']
#sub list to add
sub_list = ["h", "i", "j"]

#solution
list1[2][1][2].extend(sub_list)
print(list1)

#Exercise 9: Replace list’s item with new value if found
#You have given a Python list. Write a program to find value 20 in the list,
# and if it is present, replace it with 200.
# Only update the first occurrence of an item.

list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(25)
list1[index] = 200
print(list1)

#Exercise 10: Remove all occurrences of a specific item from a list.
#Given a Python list, write a program to remove all occurrences of item 20.
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)






