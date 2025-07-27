#tạo list rỗng
emptyList = []
print(emptyList)

#tạo ra 1 đối tượng list
emptyList2 = list()
print(emptyList2)

# tạo list có dữ liệu
hoTen = ["Phạm", "Minh", "Nhật", "đẹp", "trai"]
# lấy danh sách ra ở vị trí số 2 và số 0  trong list
print(hoTen[2], hoTen[0])
# lấy phần tử từ vị trí số 1 đến 3 [1:4)
print(hoTen[1:4])
# thêm phần tử vào cuối list
hoTen.append("Quá")
hoTen[len(hoTen):] = ["trời"]
hoTen[len(hoTen):] = ["Nhật"]
# chèn phần tử vào list
hoTen.insert(3, "thật là")
# in ra toàn bộ danh sách
print(hoTen)

# đếm độ dài list
print(len(hoTen))
# đếm số lượng phần tử thỏa điều kiện
print("Đếm Nhật: ", hoTen.count("Nhật"))
print("Đếm Phạm: ", hoTen.count("Phạm"))
print("Đếm Hà: ", hoTen.count("Hà"))

# kiểm tra phần tử có bên trong list: in
if "Nhật" in hoTen:
    hoTen.remove("Nhật")
    print(hoTen)
# xóa phần tử ra khỏi list
hoTen.remove("thật là")
print(hoTen)

# xóa phần tử ra khỏi list bằng vị trí
hoTen.pop(4)
print(hoTen)

# đảo ngược list
hoTen.reverse()
print(hoTen)

# sắp xếp lại theo ABC
hoTen.sort()
print(hoTen)
# sắp xếp lại từ nhỏ đến lớn
numbers = [2, 4, 7, 3, 1, 5, 9, 13]
numbers.sort()
print(numbers)

#sắp xếp ngược
numbers.sort(reverse=True)
print(numbers)

hoTen.sort(reverse=True)
print(hoTen)

# xóa sạch dữ liệu trong list
hoTen.clear()
print(hoTen)
