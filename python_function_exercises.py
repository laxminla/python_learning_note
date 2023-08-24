#Exercise 1: Create a function in Python
def two_args(a,b):
    print("a and b are two arguments of the function")

    x = a*b
    print("x value is: ",x)
two_args(5,10)

#Exercise 2: Create a function with variable length of arguments
def func1(*args):
    for i in args:
        print(i)
func1(20,30,20)
func1(80,100)

#Exercise 3: Return multiple values from a function
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
res = calculation(40, 10)
print("result: ",res)

#next solution
def calculation(a,b):
    return a + b, a - b
add, sub = calculation(40, 10)
print(add, sub)

#Exercise 4: Create a function with a default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)
show_employee("Ben", 12000)
show_employee("Jessa")

def describe_students(name, age):
   print("name: ", name, "age: ", age)
describe_students("Maya", '14')
describe_students("Saya", '13')

#Exercise 5: Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

# outer function
def outer_fun(a, b):
    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 20)
print(result)


#Exercise 6: Create a recursive function
def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(15)
print(res)

#Exercise 7: Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name, age)
display_student("Emma", 17)
show_student = display_student
show_student("Sita", 8)


#Exercise 8: Generate a Python list of all the even numbers between 4 to 30
print("even numbers between4 to 30 are: ",list(range(4, 30,2)))

#Exercise 9: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
print("largest number from the list is: ", max(x))