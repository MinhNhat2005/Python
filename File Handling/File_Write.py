# Viết file
"""Để ghi vào một tệp hiện có, bạn phải thêm một tham số vào hàm:open()

"a" - Thêm - sẽ thêm vào cuối tệp

"w" - Viết - sẽ ghi đè lên bất kỳ nội dung hiện có nào
"""
with open("test.py", "a")as f:
    f.write("print('Now file has more content!')")

with open("test.py") as f:
    print(f.read())
print("-------------------")

# ghi đè nội dung hiện có
with open("test.py", "w") as f:
    f.write("woop! I hava deleted the content!")

with open("test.py") as f:
    print(f.read())
print("-------------------")


# Tạo 1 file mới
"""
"x" - Tạo - sẽ tạo một tệp, trả về lỗi nếu tệp tồn tại

"a" - Append - sẽ tạo một tệp nếu tệp được chỉ định không tồn tại

"w" - Write - sẽ tạo một tệp nếu tệp được chỉ định không tồn tại
"""
f = open("demofile.py", "w")

