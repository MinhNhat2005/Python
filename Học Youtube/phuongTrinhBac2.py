import math

print("Giải phương trình bậc 2! y= ax^2 + bx + c =0")
a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))
c = float(input("Nhập vào hệ số c: "))
delta = (b**2)-4*a*c
print("delta= ",delta)
if a==0:
    print("không phải phương trình bậc 2!")
elif delta<0:
    print("Phương trình vô nghiệm!")
elif delta == 0:
    x = -b/(2*a)
    print("Phương trình có nghiệm kép :x= ", x)
else:
    x1 = (-b+ math.sqrt(delta))/(2*a)
    x2 = (-b- math.sqrt(delta))/(2*a)
    print("Phương trình có 2 nghiệm phân biệt x1 và x2")
    print("x1= ",x1)
    print("x2= ",x2)