# chữ HOA
a = "hello, world"
print(a.upper())  # dùng để chuyển tất cả các chữ trong chuỗi thành chữ hoa: upper()

# chữ thường
a = "Hello World"
print(a.lower())  # phương thức trả về chuỗi bằng chữ thường: lower()

# xóa khoảng trắng
a = " Hello World " 
print(a.strip())     # phương thức loại bỏ bất kỳ khoảng trắng nào từ đầu hoặc cuối: strip()

# thay thế chuỗi
a = "Hello World"
print(a.replace("Hello","Thế"))
print(a.replace("Hello World", "Xin chào")) # thay ký tự có trong chuỗi bằng ký tự khác 
print(a.replace("l", "i"))

# Tách chuỗi
a = "Hello World"
print(a.split(" "))    # chia chuỗi thành 2 chuỗi con phân biệt nhau bởi khoảng trắng

b = "Phạm, Minh, Nhật"
print(b.split(","))   # chia chuỗi thành 3 chuỗi con phân biệt nhau bởi dấu phẩy
