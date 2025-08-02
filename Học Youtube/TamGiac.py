import math
# xác định tam giác
print("Chương trình xác định tam giác và tính chu vi, diện tích tam giác!")
xA = float(input("Nhập vào tọa độ xA:"))
yA = float(input("Nhập vào tọa độ yA:"))
xB = float(input("Nhập vào tọa độ xB:"))
yB = float(input("Nhập vào tọa độ yB:"))
xC = float(input("Nhập vào tọa độ xC:"))
yC = float(input("Nhập vào tọa độ yC:"))

AB = math.sqrt((xB-xA)**2 + (yB-yA)**2)
AC = math.sqrt((xC-xA)**2 + (yC-yA)**2)
BC = math.sqrt((xC-xB)**2 + (yC-yB)**2)
print("AB =", AB)
print("AC=", AC)
print("BC =", BC)

if AB+AC>BC and AB+BC>AC and AC+BC>AC:
    #tính chu vi 
    cv = AB+BC+AC
    print("Chu vi tam giác là: ", cv)
    p=cv/2
    #tính diện tích
    s= math.sqrt(p*(p-AB)*(p-AC)*(p-BC))
    print("Diện tích tam giác là: ",s)
    if AB==BC==AC:
        print("Đây là tam giác đều")
    elif AB==BC or AB==AC or BC==AC:
        print("Đây là tam giác cân")
    elif AB**2 + AC**2 == BC**2 or  AB**2 + BC**2 == AC**2 or BC**2 + AC**2 == AB**2:
        print("Đây là tam giác vuông")
    elif AB**2 + AC**2 < BC**2 or  AB**2 + BC**2 < AC**2 or BC**2 + AC**2 < AB**2:
        print("Đây là tam giác tù")
    elif AB**2 + AC**2 > BC**2 or  AB**2 + BC**2 > AC**2 or BC**2 + AC**2 > AB**2:
        print("Đây là tam giác nhọn")

else:
    print("Đây không phải là tam giác!")