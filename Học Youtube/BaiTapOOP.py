# xây dựng class Ngay, thuộc tính gồm có: ngày , tháng , năm
# xây dựng các phương thức : + cho biết đó là ngày thứ bao nhiêu trong năm
#                            + Staticmethod: cho biết tháng đó có bao nhiêu ngày

class Ngay:
    # Constructor
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    # xác định số ngày của tháng
    @staticmethod
    def soNgayCuaThang(thang, nam):
        if thang in [1,3,5,7,8,10,12]:
            return 31
        elif thang in [4,6,9,11]:
            return 30
        elif thang ==2:
            return 29 if (nam% 400 ==0 or (nam%4 ==0 and nam%100!=0)) else 28
        else:
            raise ValueError("Tháng phải trong khoảng 1–12")
             

    def ngayTrongNam(self):
        giaTriNgayTrongNam =0
        # tính tổng số lượng ngày của những tháng trước
        for x in range(1, self.thang):
            giaTriNgayTrongNam += self.soNgayCuaThang(x, self.nam)

        # cộng thêm số ngày của tháng hiện tại
        giaTriNgayTrongNam += self.ngay
        return giaTriNgayTrongNam
    
    def __str__(self):
        return f"{self.ngay}/{self.thang}/{self.nam}"


ngayA = Ngay(15, 3, 2025)
print("Ngày :", ngayA)
print(ngayA.ngayTrongNam())
print(ngayA.soNgayCuaThang(2, 2025))
