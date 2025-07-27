# Dictionaries lưu trữ dữ liệu dưới dạng key : values
# Dictionaries được sắp xếp có thứ tự, có thể thay đổi và không cho phép trùng lặp

dict1 = {
    "brand" : "Ford", 
    "model" : "Mustang", 
    "year" : 1964
}
print(dict1)
print("-------------------")

# không cho phép trùng lặp (Nếu có trùng lặp thì sẽ lấy giá trị cuối cùng)
dict2 = {
    "brand" : "Ford", 
    "model" : "Mustang", 
    "year" : 1964, 
    "year" : 2005
}
print(dict2)
print("-------------------")

# Độ dài dict 
print(len(dict2))
print("-------------------")

# dict có thể chứa các mục thuộc bất kỳ kiểu dữ liệu nào
dict3 = {
    "brand" : "Ford", 
    "electric" : False, 
    "year" : 2005, 
    "color" : ["red", "green", "black"]
}
print(dict3, type(dict3))
print("---------------------")


# Sử dụng hàm khởi tạo dict()
dict4 = dict(name = "Nhat", age = 20, country = "Nghe An")
print(dict4)