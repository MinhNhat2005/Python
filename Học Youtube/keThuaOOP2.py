from abc import ABC, abstractmethod


class HangSanXuat:
    """Thông tin hãng sản xuất."""
    def __init__(self, ten_hang_san_xuat: str, ten_quoc_gia: str):
        self.ten_hang_san_xuat = ten_hang_san_xuat
        self.ten_quoc_gia = ten_quoc_gia

    def __str__(self) -> str:
        return f"{self.ten_hang_san_xuat} ({self.ten_quoc_gia})"


class PhuongTienDiChuyen(ABC):
    """
    Lớp trừu tượng – mô tả mọi phương tiện di chuyển.
    Thuộc tính protected (tiền tố _)
    """
    def __init__(self, loai_phuong_tien: str, hang_san_xuat: HangSanXuat):
        self._loai_phuong_tien = loai_phuong_tien
        self._hang_san_xuat = hang_san_xuat

    # --- Các phương thức dùng chung ---------------------------------

    def lay_ten_hang_san_xuat(self) -> str:
        """Trả về tên hãng sản xuất."""
        return str(self._hang_san_xuat)

    def bat_dau(self):
        print(f"{self._loai_phuong_tien} đang khởi động…")

    def tang_toc(self):
        print(f"{self._loai_phuong_tien} tăng tốc!")

    def dung_lai(self):
        print(f"{self._loai_phuong_tien} dừng lại.")

    # --- Phải được override ở lớp con -------------------------------
    @abstractmethod
    def lay_van_toc(self) -> float:
        """Trả về vận tốc hiện thời (km/h)."""
        pass


# ======================= CÁC LỚP KẾ THỪA ============================

class MayBay(PhuongTienDiChuyen):
    def __init__(self, hang_san_xuat: HangSanXuat, loai_nhien_lieu: str, toc_do_tb: float = 800.0):
        super().__init__("Máy bay", hang_san_xuat)
        self._loai_nhien_lieu = loai_nhien_lieu
        self._toc_do_tb = toc_do_tb  # km/h

    # Bổ sung hành vi riêng
    def cat_canh(self):
        print("Máy bay cất cánh!")

    def ha_canh(self):
        print("Máy bay hạ cánh!")

    # Override
    def lay_van_toc(self) -> float:
        return self._toc_do_tb


class XeOto(PhuongTienDiChuyen):
    def __init__(self, hang_san_xuat: HangSanXuat, loai_nhien_lieu: str, toc_do_tb: float = 120.0):
        super().__init__("Xe ô tô", hang_san_xuat)
        self._loai_nhien_lieu = loai_nhien_lieu
        self._toc_do_tb = toc_do_tb

    def lay_van_toc(self) -> float:
        return self._toc_do_tb


class XeDap(PhuongTienDiChuyen):
    def __init__(self, hang_san_xuat: HangSanXuat, toc_do_tb: float = 25.0):
        super().__init__("Xe đạp", hang_san_xuat)
        self._toc_do_tb = toc_do_tb

    def lay_van_toc(self) -> float:
        return self._toc_do_tb


# ======================= DEMO NGẮN GỌN ==============================

if __name__ == "__main__":
    boeing   = HangSanXuat("Boeing", "Hoa Kỳ")
    toyota   = HangSanXuat("Toyota", "Nhật Bản")
    martin   = HangSanXuat("Martin Bike", "Việt Nam")

    may_bay = MayBay(boeing, loai_nhien_lieu="Jet A‑1", toc_do_tb=905)
    xe_oto  = XeOto(toyota, loai_nhien_lieu="Xăng RON95", toc_do_tb=180)
    xe_dap  = XeDap(martin, toc_do_tb=32)

    for pt in (may_bay, xe_oto, xe_dap):
        print(f"--- {pt.lay_ten_hang_san_xuat()} ---")
        pt.bat_dau()
        pt.tang_toc()
        print(f"Vận tốc trung bình: {pt.lay_van_toc():.0f} km/h")
        pt.dung_lai()
        print()
