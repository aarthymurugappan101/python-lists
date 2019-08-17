oneDimensionalList = ["hello", 23, True]
twoDimensionalList = [
    ["hello", 33, False], 
    ["bye", 59, True],
    ["bye", 59, True],
    ["bye", 59, True],
    ["bye", 59, True],
    ["bye", 59, True],
]

students = [
    ["Name", "Maths", "English", "Science"],
    ["Benny", 23, 54, 76],
    ["Sunny", 23, 66, 8],
    ["Johnny", 33, 2, 6]
]

for student in students:
    for detail in student:
        print(detail, end="\t") # / <- slash \ <- back slash
    print("")