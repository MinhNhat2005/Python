sinhVien = {
    "hoVaTen" : "Phạm Minh Nhật",
    "maLop" : "23SE4",
    "diemTrungBinh": "9.0"
}
print(sinhVien)
print(sinhVien["hoVaTen"])

# sử dụng get() để lấy giá trị 
print(sinhVien.get("maLop"))

# cập nhật/ thay đổi giá trị 
sinhVien["diemTrungBinh"]= "10.0"
print(sinhVien)
sinhVien.update({"maLop": "23SE4"})
print(sinhVien)

# thêm cặp giá trị 
sinhVien["namHoc"] = 2025
print(sinhVien)

sinhVien.update({"Quê quán" : "Nghệ An"})
print(sinhVien)

# xóa các mục
sinhVien.pop("namHoc")  # xóa chỉ mục
print(sinhVien)

sinhVien.popitem() # xóa cặp giá trị cuối cùng 
print(sinhVien)

del sinhVien["diemTrungBinh"] # xóa chỉ mục
print(sinhVien)

"""sinhVien.clear()  # xóa tất cả
print(sinhVien)"""

# in tất cả các tên khóa trong từ điển
for x in sinhVien:
    print(x)

# Duyệt các giá trị
for x in sinhVien.values():
    print(x)

# Duyệt các khóa
for x in sinhVien.keys():
    print(x)

# Duyệt các cặp khóa giá trị 
for x, y in sinhVien.items():
    print(x, y)

print(sinhVien)