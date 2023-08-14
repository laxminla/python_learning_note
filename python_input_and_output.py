#Exercise 1: Accept numbers from a user
#Write a program to accept two numbers from the user and calculate multiplication

# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))
# result = num1 * num2 * num3
# print("Multiplication is", result)

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
string1 = "Name"
string2 = "Is"
string3 = "James"
print(string1 + "**" + string2 + "**" +string3)

print('My', 'name', 'is', 'James', sep='**')

# Exercise3: Convert Decimal number to octal using print()output formating
num = 8
print('%o' % num)

#Exercise 4: Display float number with 2 decimal places using print()
num = 458.541315
print('%.2f' % num)


#Exercise 5: Accept a list of 5 float numbers as an input from the user
numbers = []
for i in range(0,5):
    print("Enter number at location", i, ":")
    #accept float number from user
    item = float(input())
    #add it to the list
    numbers.append(item)

print("User List:", numbers)

