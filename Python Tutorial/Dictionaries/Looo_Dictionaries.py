dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(dict1)
print("----------------------")

# in tất cả các khóa của dict
for x in dict1:
    print(x)
print("----------------------")
for x in dict1.keys():
    print(x)
print("----------------------")

# in ra tất cả các giá trị của dict
for x in dict1:
    print(dict1[x])
print("----------------------")
for x in dict1.values():
    print(x)
print("----------------------")

# In ra cả key và values: items()
for x, y in dict1.items():
    print(str(x)+" : "+str(y))