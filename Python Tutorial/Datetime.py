# ngày

# trả về ngày tháng năm, giờ phút giây và micro giây
import datetime
x = datetime.datetime.now()
print(x)
print("------------------")

# trả về năm và tên của các ngày trong tuần
print(x.year)  # trả về năm
print(x.strftime("%A")) # trả về tên của ngày
print("------------------")


# Tạo đối tượng ngày
x = datetime.datetime(2025, 7, 29)
print(x)
print("------------------")

# phương thức strftime()
# Hiển thị tên của tháng
x = datetime.datetime(2025, 7, 29)
print(x.strftime("%B"))