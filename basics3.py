# to reverse the order of the list we use "reverse" i.e lucky_numbers.reverse(). The same applies for copy i.e "lucky_numbers= numbers.copy()"
#tuples is a another kind of data type that you can store multiple pieces of information. Tuples are imputable thus it can not be modified.
coordinates =(4,5)
print(coordinates[1])
# a list of tuples
coordinates =[(4,5), (6,9)]
print(coordinates[1])
# Use of functions. To write a function we use "def"
# indenting is important for code in a function to indicate that it's inside the function.
def greetings():
    print("Bonjour mon amie")
greetings()
#parameters are a piece of information that we give to the function
def greetings(name,age):
    print("Bonjour "+name+ " mon amie"+ " J'ai "+ str(age)+ " ans")
greetings("Timothee", 12)
greetings("Deja",21)

#return key allows python to bring back information from a function 
# NOTE:no code can come after the return statement
def cube(num):
    return num*num*num
result= cube(4)  
print(result)

# If statements
is_male = False
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("you're neither male or tall")
# We can use "and" operator though both functions have to either true or false
is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall")
else:
    print("you're either not male or tall")
# the "elsif" function helps add another condition
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("you're  not male and not tall")

# If statements(2) and comparison. We can use"==", "!" compare strings too
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(4,5,8))

#building a basic calculator
num1=float(input("Enter first number:"))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
if op=="+":
    print(num1 +num2)
elif op =="-":
    print(num1-num2)
elif op =="/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Error")

# Using dictionaries
monthConversions ={
"Jan": "January",
 "Feb": "February",
 "Mar": "March",
 "Apr": "April",
 }    

print(monthConversions["Feb"])

# while looops- a structure in python that allows us execute a block of code multiple times

i=1
while i<=10:
    print(i)
    #i=i+1
    i+=1
print("Done with loop")

#Building a guessing game
secret_word ="beauty"
#variable to store the user's guess
guess = ""
# keeps track of the number of the times the user has guessed
guess_count =0
#number of times the user has guessed
guess_limit =3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
     guess=input("Enter guess: ")
     guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOOSE!")
else:
    print("You win!")