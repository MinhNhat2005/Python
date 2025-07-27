gioiTinh = ("nam", "nữ")
lophoc = (1,2,3,4,5,6,7,8,9,10,11,12)
traiCay = ("táo","chuối", "táo", "cam", "mân","dưa hấu")

print(gioiTinh)
print(lophoc[2:10])
for x in traiCay:
    print(x)

# cộng typle
print(gioiTinh+lophoc)
print(gioiTinh+gioiTinh)

# nhân typle

print(gioiTinh*2)
print(2*lophoc)

#kiểm tra 1 phần tử có nằm trong typle không

print("táo" in traiCay) # có thì trả về giá trị true
print("14" in lophoc)  # không có thì trả về giá trị false


# kiểm tra số lượng phần tử của typle

print(len(lophoc))
print(len(traiCay))

# đếm số lần xuất hiện của phần tử bất kỳ
print(traiCay.count("táo"))
print(lophoc.count(12))

# tìm Min, Max, tính Sum
print(min(lophoc))
print(max(lophoc))
print("sum =",sum(lophoc))

print(max(traiCay))

listTC = sorted(traiCay)
print(listTC)