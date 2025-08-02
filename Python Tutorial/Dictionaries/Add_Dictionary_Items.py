# Thêm mục mới bằng cách sử dụng 1 key mới và gán 1 giá trị cho nó
dict1 = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
}
print(dict1)
print("--------------------")

dict1["color"] = "red"
print(dict1)

# Thêm 1 mục vào dict bằng cách sử dụng: update()
dict1.update({"made":"VietNam"})
print(dict1)
