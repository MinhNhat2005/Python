# String f
 # Tạo 1 chuỗi
txt = f"The price is 49 dollars"
print(txt)
print("--------------------")

# Trình dữ chỗ
price = 100
txt = f"the price is {price} dollars"
print(txt)
print("--------------------")


# hiển thị giá với 2 chữ số thập phân
price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)
print("--------------------")

# Định dạng giá trị trực tiếp mà không cần giữ trong biến
txt = f"the price is {95:.3f} dollars"
print(txt)
print("--------------------")

# Thực hiện các phép toán trong trình dữ chỗ
x = f"the price is {20*59} dollars"
print(x)
print("--------------------")

# Thực hiện các phép toán trên các biến
price = 60
tax = 0.25
txt = f"the price is {price + (price*tax)} dollars"
print(txt)
print("--------------------")

# thực hiện các câu lệnh bên trong trình dữ chỗ
price = 51
txt = f"It is very {'Expensive' if price>50 else "cheap"}"
print(txt)
print("--------------------")

# Thực thi các chức năng trong trình dữ chỗ
    # đổi giá trị thành chữ hoa
fruits = "apple"
txt = f"I love {fruits.upper()}"
print(txt)
print("--------------------")

# Tự tạo hàm riêng
def myconverter(x):
    return x*0.3048
txt =f"the plane is flying at a {myconverter(30000)} meter altitude"
print(txt)
print("--------------------")

# CÁC CÔNG CỤ SỬA ĐỔI KHÁC
 # sử dụng dấu phẩy làm dấu phân cách nghìn
price = 59000
txt = f"the price is {price:,} dollars"
print(txt)
print("--------------------")

# Định dạng chuỗi
price = 49
txt = "the price is {} dollars"
print(txt.format(price))
print("--------------------")

# Định dạng giá sẽ hiển thị dưới dạng số có 2 chữ số thập phân
txt = "the price is {:.2f} dollars"
print(txt.format(price))
print("--------------------")

# Nhiều giá trị
quantity = 3
itemno = 567
price = 24
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))
print("--------------------")

# Chỉ số mục
quantity = 3
itemno = 567
price = 24
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))
print("--------------------")

# Tham chiếu đến cùng 1 giá trị nhiều lần 
age = 20
name = "Nhat"
txt = "His name is {1}. {1} is {0} year old"
print(txt.format(age, name))
print("--------------------")

# Chỉ mục được đặt tên
myorder = "T have a {carname}, it is a {model}"
print(myorder.format(carname = "Ford", model = "Mustang"))