"""
 xây dựng bộ từ điển có các chức năng ( người dùng lựa chọn chức năng thông qua menu):
 1. Thêm 1 từ vựng mới( kèm nghĩa của từ vựng)
 2. Tra cứu nghĩa của 1 từ
 3. cập nhật ý nghĩa cho 1 từ
 4. cho phép người dùng xóa đi 1 từ vựng 
 5. cho phép người dùng xóa toàn bộ từ vựng
 6. cho phép người dùng in ra toàn bộ từ vựng
 7. cho phép người dùng in ra toàn bộ từ điển theo cấu trúc: "TỪ VỰNG" : "Ý NGHĨA"
 8. kết thúc chương trình

"""
# khai báo dictionary trống
tu_dien = {}
print(tu_dien)

# vòng lặp
while True:
    print("========= TỪ ĐIỂN ANH-VIỆT=========")
    print("Vui lòng lựa chọn chức năng:")
    print("1. Thêm 1 từ vựng mới( kèm nghĩa của từ vựng)")
    print("2. Tra cứu nghĩa của 1 từ")
    print("3. cập nhật ý nghĩa cho 1 từ")
    print("4. cho phép người dùng xóa đi 1 từ vựng")
    print("5. cho phép người dùng xóa toàn bộ từ vựng")
    print("6. cho phép người dùng in ra toàn bộ từ vựng")
    print("7. cho phép người dùng in ra toàn bộ từ điển theo cấu trúc: TỪ VỰNG : Ý NGHĨA")
    print("8. kết thúc chương trình")

    lua_chon = int(input("Mời bạn chọn chức năng :"))
    if lua_chon ==1:
        tu_vung = input("Mời bạn nhập vào 1 từ vựng :")
        if tu_vung in tu_dien:
              print("⚠️ Từ vựng đã tồn tại trong từ điển!")
        else:
              y_nghia = input("Mời bạn nhập vào 1 ý nghĩa :")
              tu_dien[tu_vung] = y_nghia
              print("✅ Đã thêm từ vựng mới thành công!")
        print(tu_dien)

    elif lua_chon ==2:
         tu_vung = input("Mời bạn nhập vào 1 từ vựng cần tra cứu :")
         if tu_vung in tu_dien:
            print(f"👉 Nghĩa của '{tu_vung}' là: {y_nghia}")
         else:
            print("Không tìm thấy nghĩa của từ!")

    elif lua_chon ==3:
        tu_vung = input("Mời bạn nhập vào 1 từ vựng cần cập nhật ý ngĩa :")
        if tu_vung in tu_dien:
             y_nghia = input("Mời bạn nhập vào ý ngĩa :")
             tu_dien.update({tu_vung: y_nghia})
             print("ý nghĩa đã được cập nhật thành công!")
        else:
             print("không tìm thấy từ vựng!")
    
    elif lua_chon ==4:
        tu_vung = input("Mời bạn nhập vào 1 từ vựng cần xóa :")
        if tu_vung in tu_dien:
             tu_dien.pop(tu_vung)
             print("Đã xóa từ vựng thành công!")
        else:
             print("Không thể xóa từ vựng!")

    elif lua_chon==5:
         if len(tu_dien)== 0:
              print("không có từ điển nào!")
         else:
              tu_dien.clear()
              print("Xóa thành công toàn bộ từ điển!")
    elif lua_chon ==6:
         for x in tu_dien:
              print(x)

    elif lua_chon ==7:
         if len(tu_dien)==0:
              print("Không có từ điển nào!")
              break
         else:
             for x,y in tu_dien.items():
              print(x, y)

    elif lua_chon ==8:
         print("Chào tạm biệt!")
         break
