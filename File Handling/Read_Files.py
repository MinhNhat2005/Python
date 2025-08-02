# mở file
f = open("test.py")
# đọc file
print(f.read())
print("------------------")

# mở tệp ở 1 vị trí khác
f = open(r"D:\Bài Tập Python\Python Tutorial\Arrays.py", "r", encoding="utf-8") 
print(f.read())
print("------------------")

# Sử dụng từ khóa with
with open("test.py") as f:
    print(f.read())
print("------------------")


# Đóng file
f = open("test.py")
print(f.readline())
f.close()
print("------------------")

# chỉ đọc các phần của file
  # trả về 5 ký tự đầu tiên của file
with open("test.py") as f:
    print(f.read(5))
print("------------------")

# Đọc dòng (Đọc 1 dòng của file)
f = open("test.py")
print(f.readline())
print("------------------")

  # đọc 2 dòng đầu tiên của file
f = open("test.py")
print(f.readline())
print(f.readline())
print("------------------")

# lặp qua từng dòng của file
with open("test.py") as f:
    for x in f:
        print(x)