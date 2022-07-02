#functions that help modify lists
#function "extend" allows a list to be added onto another list/ add them together
lucky_numbers =[4,8,56,32,12,]
friends =["paul", "peter", "john", "beth", "mary"]
friends.extend(lucky_numbers)
print(friends)

#In order to add an element at the end f the list we use "append"

# In oder to sort the list
lucky_numbers =[4,8,56,32,12,]
lucky_numbers.sort()
print(lucky_numbers)

#In oder to delete the last elements use "pop"
lucky_numbers.pop()
print(lucky_numbers)
# to specify the element to delete place the position in the pop
lucky_numbers.pop(2)
print(lucky_numbers)

#method 2- using remove/delete 
del lucky_numbers[2]
print(lucky_numbers)