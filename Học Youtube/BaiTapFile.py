
# mở file vidu1.txt chế độ đọc
f = open("SQLite.py", "x", encoding="utf-8")

# lấy danh sách sinh viên từ file vidu1.txt
with open("vidu1.txt", "r", encoding="utf_8"):
    danhSach = f.read()
    print(danhSach)

# viết nội dung vào file
with open("vidu1.txt", "w", encoding="utf_8") as f:
    f.write("Danh sách sinh viên \n")
    f.write("Nguyễn Thị Thùy Tiến \n")
    f.write("Nguyễn Thị Thùy Tiên \n")
    f.write("Phạm Minh Nhật \n")

# ghi đè nội dung vào file
with open("vidu1.txt", "a", encoding="utf_8") as f:
    f.write("Phạm Thị Hà")
    

with open("vidu1.txt", "r", encoding="utf_8") as f:
    doc = f.readline()
    print(doc)