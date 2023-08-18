#Title function
str1 = "welcome to my home"
print(str1.title())

#capitalize function
print(str1.capitalize())

#isalnum method returns true if string is alphaneumeric (space % , . returns false)
str1 = "My salary is 7000"
print(str1.isalnum())

strOne = str("pynative")
strTwo = "pynative"
print(strOne == strTwo)
print(strOne is strTwo)

str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub, 4))

str1 = 'Welcome'
print(str1*2)

str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])


#Write a program to create a new string made of an input string’s first, middle, and last character
str1 = 'James'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)

#Exercise 2: Write a program to create a new string made of the middle three characters of an input string.
def get_middle_three_chars(str1):
    print("original string is", str1)
    #get middle index
    mi = int(len(str1)/2)

    #Use string slicing to get the middle three characters starting from the middle index to the next two character
    res = str1[mi -1:mi + 2]
    print("Middle there chars are:",res)

get_middle_three_chars("JohnDipPeta")
get_middle_three_chars("JasonAy")


def length_of_the_string(name):
    print("first  name ", name)

    res = int(len(name))
    print("length of the string: ", res)

length_of_the_string("Bimla")
length_of_the_string("JayNarayan")


def first_three_letter(str1):
    print("all leters from string: ",str1)
    res = str1[0:3]
    print("first 3 letters from strng1: ", res)
first_three_letter("Hello")
first_three_letter("Monkey")

def last_three_letters(str1):
    print("Original string is: ", str1)
    result = str1[-3:]
    print("Last three leters from the string is: ",result)
last_three_letters("Hello")
last_three_letters("Darling")

#Exercise 3: Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
def append_middle(s1, s2):
    print("Original strings are: ", s1, s2)

    mi = int(len(s1)/2)
#get character from 0 to the middle index number from s1
    x = s1[:mi:]
    #concatenate
    x = x+s2

#append remaining character from s1
    x = x + s1[mi:]
    print("after appending new string in middle: ", x)

append_middle("Hello", "Hi")
append_middle("Dipson", "Dipsiya")

#Exercise 4: Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

def get_first_middle_last_character_from_string(s1, s2):
    print("Original strings are : ", s1, s2)

    #Get first character from each string
    first_char = s1[0] + s2[0]
    #get middle character from both string
    middle_char = s1[int(len(s1)/2):int(len(s1)/2) +1] + s2[int(len(s2)/2):int(len(s2)/2) +1]


    #get last character from both string
    last_char = s1[-1] + s2[-1]

    #add all
    result = first_char + middle_char + last_char
    print("mix string is: ", result)

get_first_middle_last_character_from_string("America", "Japan")


#Arrange string characters such that lowercase letters should come first

def lowercase_letter_come_first(str1):
    print("original word: ", str1)
    lower = []
    upper = []
    for char in str1:
        if char.islower():
            #add lowercase character to string
            lower.append(char)
        else:
            upper.append(char)
    sorted_str = ''.join(lower+upper)
    print("sorted string: ", sorted_str)

lowercase_letter_come_first("PYnAtive")

##Arrange string characters such that uppercase letters should come first

def get_uppercase_letter_first(str1):
    print("Original String: ", str1)
    lowercase = []
    uppercase = []
    for char in str1:
        if char.islower():
            lowercase.append(char)
        else:
            uppercase.append(char)
    result = ''.join(uppercase+lowercase)
    print("result string: ", result)
get_uppercase_letter_first("pyNatiVE")


def change_into_uppercase(str1):
    print("original string: ",str1)
    result = str1.upper()
    print("result; ",result)

change_into_uppercase("hello")

#Count all letters, digits, and special symbols from a given string
def count_all_letter_digit_and_symbols(str1):
  print("Original string: ", str1)
  char_count = 0
  digit_count = 0
  symbol_count = 0
  for char in str1:
      if char.isalpha():
          char_count += 1
      elif char.isdigit():
          digit_count += 1
      else:
          symbol_count +=1
  print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

print("total counts of chars, digits, and symbols\n")
count_all_letter_digit_and_symbols("P@yn2at&#i5ve")





