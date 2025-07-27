# Truy cập các mục

# lấy giá trị của khóa "model" bằng: [] hoặc get()
dict1 = {
    "brand" : "Ford",
    "model": "Mustang", 
    "year" : 2005
}
x = dict1["model"]
y = dict1.get("brand")
print(x)
print(y)
print("--------------------------")

# lấy ra tất cả các key trong dict: keys()
z = dict1.keys()
print(z)
print("--------------------------")

# Thêm 1 mục mới vào dict
dict1["color"] = "white"
print(z)
print("--------------------------")

# Nhận danh sách tất cả các giá trị trong dict: values()
x = dict1.values()
print(x)
print("--------------------------")

# Thay đổi trong dict gốc và thấy rằng danh sách giá trị nhận được cũng cập nhật
dict1["brand"] = "ToYoTa"
print(x)
print("--------------------------")

# Thêm 1 mục mới vào dict gốc và thầy rằng danh sách giá trị nhận được cũng cập nhật
dict1["lit"] = 20
print(x)
print("--------------------------")

# in ra danh sách dưới dạng key : values
danhSach = dict1.items()
print(danhSach)
print("--------------------------")

# Thay đổi trong dict gốc và thấy rằng danh sách các mục nhận được cũng cập nhật
dict1["year"] = 2025
print(danhSach)
print("--------------------------")

# Thêm 1 mục với dict gốc và thấy rằng danh sách mục nhận được cũng cập nhật
dict1["made"] = "VietNam"
print(danhSach)
print("--------------------------")

# Kiểm tra xem khóa có tồn tại không
if "model" in dict1:
    print("YES")
else:
    print("No")