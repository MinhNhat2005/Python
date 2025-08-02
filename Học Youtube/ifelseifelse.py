# câu lệnh rẽ nhánh if else if else
x= int(input("Nhập vào số nguyên: "))
if x>0:
    print(x, "là số dương!")
else:
    if x==0:
        print(x, "không là số dương cũng không là số âm!") 
    else:
        print(x, "là số âm!")   

# ví dụ 2
y= float(input("Nhập vào số y: "))
if y>=9:
    print("xếp loại: Xuất sắc")
elif y>=8:
    print("xếp loại: giỏi")
elif y>=7:
    print("xếp loại:  khá")
elif y>=5:
    print("xếp loại: trung bình")
else:
   print("xếp loại: yếu")

 