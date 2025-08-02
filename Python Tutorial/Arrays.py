# Mảng

cars = ["Ford", "ToYoTa", "BMW"]
#  lấy ra giá trị đầu tiên của mảng
x = cars[0]
print(x)
print("-----------------")
# thay thế giá trị cho mục của mảng
cars[0] = "Madaz"
print(cars)
print(len(cars))
print("-----------------")

# lặp qua tất cả các phần tử của mảng
for x in cars:
    print(x)
print("-----------------")

# Thêm phần tử vào mảng
cars.append("Honda")
print(cars)
print("-----------------")

# Xóa phần tử mảng
cars.pop(1)
print(cars)
print("-----------------")

cars.remove("BMW")
print(cars)

# Đảo ngược thứ tự các mục trong mảng
cars.reverse()
print(cars)