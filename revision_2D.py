two_dimensional_list = [
    ["Name", "Subject", "Marks"],
    ["JohnVallal", "Chinese", 80],
    ["Mary", "English", 75]
]

for row in two_dimensional_list:
    for col in row:
        print (col, end="\t\t")
    print()