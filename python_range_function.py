#The range() function only works with the integers,
# All three arguments can be positive or negative.
# The step value must not be zero. If a step=0, Python will raise a ValueError exception.

#Use range() to generate a sequence of numbers starting from 9 to 100 divisible by 3.
for i in range(9, 100, 3):
    print(i, end=' ')
#output: 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75 78 81 84 87 90 93 96 99 0

# Generate numbers between 0 to 10
for i in range(10):
    print(i)

#How to use range function in Python
#range(start, stop[, step])
# Numbers from 5 to 20
# start = 10
# stop = 50
# step = 5
for i in range(5, 20, 5):
    print("hello range")
    print(i)




