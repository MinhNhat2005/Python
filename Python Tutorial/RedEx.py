# biểu thức chính quy

# mô đun RedEx
# kiểm tra chuỗi có bắt đầu với "The" và kết thúc bằng "Spain"
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! we have a match")
else:
    print("No match")
print("---------------------")

# Hàm findaill(): Hàm trả về 1 danh sách chưa tất cả các kết quả trùng khớp
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
   # Nếu không tìm thấy kết quả phù hợp thì trả về 1 danh sách trống
x = re.findall("Portugal", txt)
print(x)
print("---------------------")

# Hàm search(): 
   # tìm kiếm ký tự khoảng trắng đầu tiên  trong chuỗi
x = re.search("\s", txt)
print("The first white character is located in position:", x.start())
   # Nếu không có kết quả trùng khớp thì giá trị trả về None
x = re.search("Portugal", txt)
print(x)
print("---------------------")

# Hàm split(): trả về một danh sách trong đó chuỗi đã được tách ra
x = re.split("\s", txt)
print(x)
   # Chỉ định số lần xuất hiện bằng cách chỉ địnhu tham số
x = re.split("\s", txt, 2)
print(x)
print("---------------------")

# Hàm sub(): thay thế các kết quả phù hợp bằng văn bản đã chọn
  # Thay thế mọi ký tự khoảng trắng bằng số 9
x = re.sub("\s", "9", txt)
print(x)
  # Kiểm soát số lần thay thế bằng cách chỉ định tham số
x = re.sub("\s", "9", txt, 2)
print(x)
print("---------------------")

# Đối tượng phù hợp
  # Thực hiện tìm kiếm sẽ trả về đối tượng phù hợp
x = re.search("ai", txt)
print(x)
print("---------------------")

# Đối tượng span trả về 1 bộ chứa các vị trí bắt đầu và kết thúc của một tìm kiếm
 # in vị trí bắt dầu và kết thúc của lần xuất hiện khoảng trắng đầu tiên bắt đầu bằng chữ hoa"S"
x = re.search(r"\bS\w+", txt)
print(x.span())

 # in chuỗi được truyền vào hàm
x = re.search(r"\sS\w+", txt)
print(x.string)

 # in ra chuỗi có kết quả trùng khớp
x = re.search(r"\bS\w+", txt)
print(x.group())