# match giống swith case


while True:

 day = int(input("Nhập vào thứ trong tuần: "))
 match day:
    case 2:
        print("Monday")
        break
    case 3:
        print("Tuesday")
        break
    case 4:
        print("Wednesday")
        break
    case 5:
        print("Thursday")
        break
    case 6:
        print("Friday")
        break
    case 7:
        print("Saturday")
        break
    case 8:
        print("Sunday")
        break
    case _:   # để giá trị _ vào case cuối cùng để nếu người dùng nhập không có kết quả nào thì nó sẽ là trường hợp mặc định
        print("Giá trị không hợp lệ, vui lòng nhập lại") 
print("---------------------------")


# kết hợp các giá trị
# Sử dụng ký tự | như toán tử hoặc
day = int(input("Nhập vào thứ trong tuần: "))
match day:
    case 1 | 2 | 3 | 4| 5:
        print("Today is weekday")
    case 6 | 7:
        print("Today is weekends")
    case _:
        print("Nhập sai")


# có thể them các câu lệnh điều kiện if vào
day = int(input("Nhập vào ngày: "))
month = int(input("Nhập vào tháng: "))
match day:
    case 1 | 2 | 3 | 4 | 5 if month == month:
        print(f"A weekday in month {month}")
    case 6 | 7 if month == month:
        print(f"A weekends in month {month}")
    case _:
        print("No match")
    