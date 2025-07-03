data = {
    "Name" : "Let us C",
    "Author" : "Yashwant Kanetkar",
    "Price" : 340,
    "Publication" : "BBA Publication",
}

print("Loop to display keys : ")
for i in data:
    print(i)

print("Loop to display values : ")
for i in data.values():
    print(i)

print("Loop display both key and values : ")
for i, j in data.items():
    print(i, " : ", j)
    