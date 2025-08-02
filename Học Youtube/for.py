sum=0
for i in range(1000):
    if i%2==0:

        print(i)
        sum+=i
print("sum= ",sum)

tong =0
# vòng lặp for có bước tăng tùy chỉnh
for a in range(0, 20, 3):
    print(a)
    tong+=a
print("tong= ",tong)

# vòng lặp for duyệt các phần tử của list
hoTen = ["Phạm", "Minh", "Nhật"]
for ten in hoTen:
    print(ten)

# vòng lặp for duyệt các phần tử theo vị trí
for i in range(len(hoTen)):
    print(hoTen[i])
