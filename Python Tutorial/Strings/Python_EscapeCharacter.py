# ký tự thoát
# Ký tự thoát là dấu gạch chéo ngược theo sau là ký tự bạn muốn chèn.\
x = "My name is \"Nhật\""
print(x)

# 1 gạch chéo ngược là ký tự thoát
txt = 'It\'s alright'
print(txt)

# 2 gạch chéo ngược thì khi in ra chỉ còn 1 cái
txt = "This will insert one \\ (backslash)"
print(txt)

# \n xuống dòng
x = "Hello \nWorld"
print(x)

# \t thụt vào 
x = "\tPhạm Nhật"
print(x)

# \b xóa ký tự phía trước (backspace)
x = "Minh \bNhật"
print(x)

# \r quay đầu dòng (đưa con trỏ về đầu dòng có nghĩa là chữ Nhật sẽ đè lên chữ Minh và viết tiếp những ký tự tiếp theo)
x = "Minht \rNhật"
print(x)