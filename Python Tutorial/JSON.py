# JSON
import json

# Chuyển đổi từ JSON sang python: json.loads()
# some JSON:
x = '{"name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)

# the result is a python dictionary
print(y["age"])
print("=------------------=")

# chuyển từ python sang JSON
x = {
    "tên" : "Nhật",
    "Tuổi": 20,
    "Quê": "Nghệ An"
}
# chuyển qua JSON
y = json.dumps(x)
print(y)
print(type(y))
print("=------------------=")

"""
Bạn có thể chuyển đổi các đối tượng Python thuộc các loại sau thành chuỗi JSON:

dict
list
tuple
string
int
float
True
False
None
"""

# chuyển đổi các đối tượng python thành chuỗi JSON và in giá trị
print(json.dumps({"Name":"John","age":30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("Apple", "Banana")))
print(json.dumps("Hello"))
print(json.dumps(42))
print(json.dumps(232.12))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("=------------------=")

# Chuyển đổi 1 đối tượng python chứ tất cả các kiểu dữ liệu hợp pháp
x = {
    "Name": "John",
    "age" : 30,
    "Married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model":"BMW 230", "mpg": 27.5},
        {"model":"Ford Edge", "mpg": 23.1}
    ]
}
print(json.dumps(x))
print("=------------------=")

# Định dạng kết quả
# Sử dụng tham số để xác định con số sốt thụt lề: indent
print(json.dumps(x, indent=4))
print("=------------------=")

# Sử dụng tham số để thay đổi dấu phân cách mặc định: separators
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print("=------------------=")

# đặt hàng kết quả
# sử dụng tha số để chỉ định nếu kết quả có nên được sắp xếp hay không: sort_keys
print(json.dumps(x, indent= 5, sort_keys=True))