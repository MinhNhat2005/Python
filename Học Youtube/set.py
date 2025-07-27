# tạo set mới
monHoc = {"toán", "lý", "hóa"}
print(monHoc)

# Duyệt các phần tử bên trong set
for x in monHoc:
    print(x)

# thêm mới phần tử vào trong set
monHoc.add("lich su")
print(monHoc)

# thêm nhiều phần tử
hocThem = {"văn", "Anh", "công nghệ thông tin"}
monHoc.update(hocThem)
print(monHoc)


# thêm list vào SET
hocPhuDao = ["võ thuật", "múa", "võ thuật"]
print(hocPhuDao)
monHoc.update(hocPhuDao)
print(monHoc)

# xóa phần tử
monHoc.remove("lich su")  # remove nếu phần tử không tồn tại thì báo lỗi
print(monHoc)

monHoc.discard("Anh")
print(monHoc)

monHoc.discard("nhat") # discard nếu phần tử không tồn tại thì khong báo lỗi
print(monHoc)

# loại bỏ phần tử cuối cùng bằng pop()
monHoc.pop()
print(monHoc)

# làm rỗng tập hợp bằng clear()
monHoc.clear()
print(monHoc)

# xóa bỏ tập hợp bằng del
del monHoc
print(monHoc)