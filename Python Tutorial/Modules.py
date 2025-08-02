""" Mô đun:
+ Mô đun giống như 1 thư viện mã
+ 1 tệp chứa một tập hợp các hàm để đưa vào ứng dụng
"""
 # Tạo 1 mô đun
# lưa đoạn mã dưới đây vào tệp có tên mymodule.py
"""
def greeting(name):
    print("Hello, "+name)
"""
import mymodule

mymodule.greeting("Nhat")
print("----------")

a = mymodule.person1
print(a)
print("----------")

# Tạo bí danh cho modun 
import mymodule as mx
a = mx.person1["Họ"]
print(a)
print("----------")

# mô đun tích hợp (có sẵn trong python): platform
import platform
x = platform.system()
print(x)
print("----------")

# Hàm dir(): liệt kê tất cả các tên hàm (hoặc tên biến trong modun)
import platform
x = dir(platform)
print(x)
print("----------")

# Nhập từ mô đun (chỉ nhập từ điển person1 từ modun)
from mymodule import person1
print(person1["Năm"])