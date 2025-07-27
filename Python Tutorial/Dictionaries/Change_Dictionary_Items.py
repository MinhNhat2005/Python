# Thay đổi giá trị
  # thay đổi giá trị bằng cách gọi tên key của nó 

dict1 = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
}
print(dict1)
print("-------------------------")

# thay đổi giá trị
dict1["year"] = 2005
print(dict1)
print("-------------------------")

# Cập nhật giá trị
dict1.update({"year": 2025})
print(dict1)