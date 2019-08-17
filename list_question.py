'''
Create a List that stores Integers. The program will repeatedly receive input from keyboard and add it to the List until the user enters N.

After retrieval is done, sort the items in the List and print out the elements which are in sorted order. Also print out the sum of the items and whether it is Even or Odd.
'''

usrInput = input("Enter an integer or N to exit:")
mylist = []
while usrInput != "N":
    mylist.append(int(usrInput))
    usrInput = input("Enter an integer or N to exit:")
    mylist.sort()
print(mylist)
total = 0
for x in mylist:
    total+=x

if total % 2 == 0:
    print(total,"Even")
else:
    print(total,"Odd")

