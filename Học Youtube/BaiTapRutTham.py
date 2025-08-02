# Quay số trúng thưởng

import random

# khai báo set rỗng
thung_phieu = set()
print(type(thung_phieu))
# vòng lặp
while True:
    print("========Menu========")
    print("Vui lòng lựa chọn chứ năng:")
    print("1 - Thêm một số điện thoại vào thùng phiếu dự thưởng!")
    print("2 - xóa một số điện thoại khỏi thùng phiếu dự thưởng!")
    print("3 - Quay số trúng thưởng!")
    print("4 - Thoát")

    lua_chon = int(input("Lựa chọn :"))
    if lua_chon==1:
        sdt = input("Nhập vào số điện thoại dự thưởng :")
        if sdt in thung_phieu:
            print("Số điện thoại đã tồn tại!")
        else:
            thung_phieu.add(sdt)
            print("Đã thêm số điện thoại thành công!")
    elif lua_chon==2:
        sdt = input("Nhập vào số điện thoại cần xóa :")
        if sdt in thung_phieu:
            thung_phieu.discard(sdt)
            print("✅ Đã xóa số điện thoại khỏi thùng.")
        else:
            print("❌ Không tìm thấy số điẹn thoại trong thùng!")
    elif lua_chon==3:
        if len(thung_phieu) ==0:
            print("⚠️ Thùng đang trống, không thể quay số!")
        else:
            trung_thuong = random.choice(list(thung_phieu))
            print("🎉 Số điện thoại trúng thưởng là:", trung_thuong)
    elif lua_chon ==4:
         print("👋 Tạm biệt!")
         break
    else:
          print("⚠️ Lựa chọn không hợp lệ, vui lòng chọn lại!")
   

    


