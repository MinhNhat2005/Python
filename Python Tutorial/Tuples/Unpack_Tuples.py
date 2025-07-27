# Đóng gói 1 tuple
fruits = ("apple", "banana", "cherry")

# Giải nén 1 bộ
(green, yellow, red) = fruits

print(green) 
print(yellow)
print(red)
print("------------------------")

# Nếu số lượng biến nhỏ hơn số lượng giá trị thì dùng * vào 1 biến thì nó sẽ lưu dưới dạng danh sách
fruits = ("apple", "banana", "cherry", "strawberry", "grape")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
print("------------------------")

# Nếu dấu * được gắn cho biến khác không phải là biến cuối cùng thì python sẽ gán các giá trị cho biến cho đến khi số lượng giá trị còn lại khớp với giá trị của biến
fruits = ("apple", "banana", "cherry", "strawberry", "grape")
(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)