# Pseudo code
# take user input, store as num1
# take user input, store as num2
#
# list variable to be declared
#
# use a while loop to loop it 100 times
#   if the index number is even
#       append num2 to list
#   else
#       append num1 to list
# print out the list

num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))

storage = [] # This is initilization to empty list

index = 0
while index < 100:
    if index % 2 == 0:
        storage.append(num2)
    else:
        storage.append(num1)
    index += 1
print (storage)