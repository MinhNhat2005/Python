# ký tự đầu tiên có chỉ mục là 0
# Cắt chuỗi
b = "Hello, World"
print(b[2:5])  # chỉ lấy từ 2 đến 4 giống như [2:5)

# cắt từ đầu
b = "Hello, World"
print(b[:5])  # lấy vị trí đầu tiên là 0 đến vị trí thứ 4

# cắt đến cuối
b = "Hello, World"
print(b[5:])  # lấy từ chỉ mục số 5 đến cuối cùng

b = "Hello, World"
print(b[-9: -2])  # vị trí cuối cùng trong chuỗi có chỉ mục là 0 và đếm ngược lại về phía trước (-9:-2]