# example 1
# print changes the case to upper then checks whether the it is lower case
phrase ="alinda is very cool"
print(phrase.upper().islower())

# to get the length of the string
phrase ="alinda is very cool"
print(len(phrase))

#inorder to access a specific character based on it's value we use "[]"
phrase ="alinda is very cool"
print(phrase[7])

#index function helps us locate a specific character or string
phrase ="alinda is very cool"
print(phrase.index("very"))

# replace function uses parametres
phrase ="alinda is very cool"
print(phrase.replace("alinda", "mbona"))

#working with numbers
# %is read as mode and it returns the remainder as the answer
print(23%5)

#to convert a number to a string. In order to cocatenate a number and a string I have to convert it.
my_num =5
print(str(my_num)+ " this is my lucky munber")

# "abs"- absolute value
my_num = -5
print(abs(my_num))

# "pow"- same a number to the power of another number i.e 2^4
print(pow(4, 3))

# "max"- returns the highest vale of the list. "min"- deos the opposite
print(max(14, 33,  67))

# "round"- rounds the value
print(round(4.3))

#in order to use several math functions we can import math library
from math import*
print(sqrt(100))

#Getting input from users
name= input("Enter your name: ")
age= input("Enter your age: ")
print("Agandi " + name+ " olilota. Your age is "+ age)

# example2 NB: "int" is used for only whole numbers. WE can use"float for decimal numbers
num1 = input("What is your number: ")
num2 = input("What is your other number: ")
result = int(num1) + int(num2)
print(result)

#mad libs game with python
color = input("Enter a color")
plural_noun = input("Enter a plural noun")
celebrity = input("Enter a celebrity")

print("Roses are " +color)
print(plural_noun+ " are blue")
print("I love " +celebrity)

#Lists- we use "[]"
friends = ["Kevin","Karen","Karol","Oscar", "Jim"]
# we can use negatives to access the position of the value backwards
print(friends[-1])
# [1:]- helps us access the position of the value 1 and those after that
print(friends[1:4])