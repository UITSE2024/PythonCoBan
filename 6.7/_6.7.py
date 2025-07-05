import sys
from typing import Callable

ThiSinh = tuple[str, str, float, float]

def nhap_thi_sinh() -> ThiSinh:
    so_bao_danh = input("So bao danh: ").strip()
    ho_ten = input("Ho va ten: ").strip()
    diem_toan = input("Diem toan: ").strip()
    diem_van = input("Diem van: ").strip()
    
    if not all([so_bao_danh, ho_ten, diem_toan, diem_van]):
        return ()
    
    return so_bao_danh, ho_ten, float(diem_toan), float(diem_van)

def loc_thi_sinh(loc: Callable[[ThiSinh], bool], ds_thi_sinh: list[ThiSinh]) -> list[ThiSinh]:
    return [thi_sinh for thi_sinh in ds_thi_sinh if loc(thi_sinh)]

def is_tong_diem_tren_10(thi_sinh: ThiSinh) -> bool:
    return thi_sinh[-1] + thi_sinh[-2] > 10

def co_diem_bang_khong(thi_sinh: ThiSinh) -> bool:
    return thi_sinh[-1] * thi_sinh[-2] == 0
        
def main() -> int:
    ds_thi_sinh: list[ThiSinh] = []

    while (ts := nhap_thi_sinh()):
        ds_thi_sinh.append(ts)

    print(
        "Danh sach thi sinh:",
        *ds_thi_sinh,
        sep="\n"
    )

    ds_tren_10: list[ThiSinh] = loc_thi_sinh(is_tong_diem_tren_10, ds_thi_sinh)
    print(
        "Danh sach thi sinh co diem > 10:",
        *ds_tren_10,
        sep="\n"
    )

    print(
        "Danh sach thi sinh liet:",
        *filter(co_diem_bang_khong, ds_thi_sinh),
        sep="\n"
    )

    return 0

if __name__ == "__main__":
    sys.exit(main())