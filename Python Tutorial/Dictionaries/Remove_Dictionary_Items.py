# Xóa các mục

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(dict1)
print("---------------------")

 # xóa mục có key được chỉ định: pop()
dict1.pop("model")
print(dict1)
print("---------------------")

# Loại bỏ phần mục cuối cùng: popitem()
dict1.popitem()
print(dict1)
print("---------------------")

# Loại bỏ mục có tên khóa: del
del dict1["brand"]
print(dict1)
print("---------------------")

# xóa hoàn toàn dict: del
dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del dict2
print("---------------------")

# làm trống dict: clear()
dict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict3.clear()
print(dict3)

