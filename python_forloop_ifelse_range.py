#Control flow statements: Use the if-else statements in Python for conditional decision-making
# for loop: To iterate over a sequence of elements such as list, string.
# range() function: Using a for loop with range(), we can repeat an action a specific number of times
# while loop: To repeat a block of code repeatedly, as long as the condition is true.
# Break and Continue: To alter the loop’s execution in a certain manner.
# Nested loop: loop inside a loop is known as a nested loop

#Exercise 1: Print First 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i+=1

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("number pattern ")
row = 5
for i in range(1, row + 1, 1):
    #run inner loop i +1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    #empty line after each row
    print(" ")

#Exercise 3: Calculate the sum of all numbers from 1 to a given number
    #For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
 #use for loop and range function
# #create variable for sum
# s = 0
# n = int(input("Enter number "))
# for i in range(1, n + 1, 1):
#     #add current number to sum variable
#     s += i
# print("\n")
# print("sum is: ", s)

# #using the built-in function
# n = int(input("Enter number"))
# #pass range of number to sum()function
# x = sum(range(1, n+1))
# print("Sum is :", x)

#Exercise 4: Write a program to print multiplication table of a given number
n = 2
for i in range(1, 11, 1):
    p = n * i
print(p)

#Exercise 5: Display numbers from a list using loop
    # The number must be divisible by five
    # If the number is greater than 150, then skip it and move to the next number
    # If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)


#Exercise 6: Count the total number of digits in a number
num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)

#Exercise 7: Print the following pattern
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print()

#Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
    print(item)

#Exercise 9: Display numbers from -10 to -1 using for loop
for num in range(-10, 0, 1):
    print(num)

#Exercise 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")

#Exercise 11: Write a program to display all prime numbers within a range
#range
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end, 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
