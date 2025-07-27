# cộng chuỗi
a = "nhat"
b = "Minh"
c = a+b
print(c,type(a))


# tạo chuỗi nhiều dòng
chuoi_nhieu_dong = """
dòng 1
dòng 2
dòng 3
dòng 4"""
print(chuoi_nhieu_dong)


# lặp lại chuỗi
chep_phat= "Em hua lam bai tap day du \n"
chep_phat_10 = chep_phat*10
print(chep_phat_10)

# kiểm tra chuỗi có thuộc chuỗi khác
chuoi_1 = "xin chào Phạm Minh Nhật"
chuoi_2 = "Phạm Minh Nhật"
chuoi_3 = "Nghệ An"
if chuoi_2 in chuoi_1:
    print("Chuỗi 2 là chuỗi con của chuỗi 1")
else:
    print("Chuỗi 2 là khong la chuỗi con của chuỗi 1")

if chuoi_3 in chuoi_1:
    print("Chuỗi 3 là chuỗi con của chuỗi 1")
else:
    print("Chuỗi 3 là khong la chuỗi con của chuỗi 1")

# viết hoa chữ đầu của chuỗi

s = "hôm nay trời đẹp quá!"
s = str.capitalize(s)
print(s)


# viết hoa toàn bộ chuỗi
s = s.upper()
print(s)



# viết thường toàn bộ chuỗi
s=s.lower()
print(s)

# đếm số lượng chuỗi con
s = "Lập trình python là xu hướng hiện nay!"
print(s.find("xú")) # trả về -1 néu không tìm thấy
print(s.find("python")) # trả về đúng vị trí L là vị trí số 0 và đếm tiếp kể cả dấu cách
print(s.count("python")) # đếm số lần xuất hiện chữ python
print(len(s)) # độ dài chuỗi

# thay thế 
s = "Lập trình python là xu hướng hiện nay!"
s =s.replace("python", "PYTHON")
print(s)

# cắt chuỗi thành 1 list
s = "Lập trình python. là xu hướng hiện nay!"
list1= s.split(" ")
print(list1)

list2=s.split(".")
print(list2)

# lấy chuỗi con
print(s[0:10])