def tinh_tien_thuong(so_huy_chuong):
    if so_huy_chuong > 10:
        return so_huy_chuong * 500000
    elif 5 <= so_huy_chuong <= 10:
        return so_huy_chuong * 300000
    elif 1 <= so_huy_chuong < 5:
        return so_huy_chuong * 200000
    return 0


def xem_danh_sach_cau_thu(ds_cau_thu):
    if not ds_cau_thu:
        print("Danh sách cầu thủ trống.")
        return
    for cau_thu in ds_cau_thu:
        print(f"Mã: {cau_thu['ma_ct']}, Tên: {cau_thu['ten']}, Tuổi: {cau_thu['tuoi']}, "
              f"Vị trí: {cau_thu['vi_tri']}, Số huy chương: {cau_thu['so_huy_chuong']}, "
              f"Tiền thưởng: {cau_thu['tien_thuong']}")


def nhap_cau_thu(ds_cau_thu):
    try:
        ma_ct = input("Nhập mã cầu thủ: ")
        ten = input("Nhập tên cầu thủ: ")
        tuoi = int(input("Nhập tuổi cầu thủ: "))
        vi_tri = input("Nhập vị trí (Thủ môn/Hậu vệ/Tiền vệ/Tiền đạo): ")
        so_huy_chuong = int(input("Nhập số huy chương: "))
        tien_thuong = tinh_tien_thuong(so_huy_chuong)
        cau_thu = {
            "ma_ct": ma_ct,
            "ten": ten,
            "tuoi": tuoi,
            "vi_tri": vi_tri,
            "so_huy_chuong": so_huy_chuong,
            "tien_thuong": tien_thuong
        }
        ds_cau_thu.append(cau_thu)
    except ValueError:
        print("Lỗi: Tuổi và số huy chương phải là số nguyên.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


def xoa_cau_thu(ds_cau_thu):
    try:
        ma_ct = input("Nhập mã cầu thủ cần xóa: ")
        for cau_thu in ds_cau_thu:
            if cau_thu["ma_ct"] == ma_ct:
                ds_cau_thu.remove(cau_thu)
                print(f"Đã xóa cầu thủ có mã {ma_ct}.")
                return
        print(f"Không tìm thấy cầu thủ có mã {ma_ct}.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


def sua_cau_thu(ds_cau_thu):
    try:
        ma_ct = input("Nhập mã cầu thủ cần sửa: ")
        for cau_thu in ds_cau_thu:
            if cau_thu["ma_ct"] == ma_ct:
                cau_thu["ten"] = input("Nhập tên mới: ")
                cau_thu["tuoi"] = int(input("Nhập tuổi mới: "))
                cau_thu["vi_tri"] = input("Nhập vị trí mới: ")
                cau_thu["so_huy_chuong"] = int(input("Nhập số huy chương mới: "))
                cau_thu["tien_thuong"] = tinh_tien_thuong(cau_thu["so_huy_chuong"])
                print(f"Đã cập nhật thông tin cầu thủ có mã {ma_ct}.")
                return
        print(f"Không tìm thấy cầu thủ có mã {ma_ct}.")
    except ValueError:
        print("Lỗi: Tuổi và số huy chương phải là số nguyên.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


def sap_xep_cau_thu(ds_cau_thu):
    try:
        ds_cau_thu.sort(key=lambda ct: ct["so_huy_chuong"])
        print("Danh sách cầu thủ đã được sắp xếp theo số huy chương.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


def main():
    ds_cau_thu = []
    while True:
        print("\n1. Xem danh sách cầu thủ")
        print("2. Nhập cầu thủ mới")
        print("3. Xóa cầu thủ")
        print("4. Sửa thông tin cầu thủ")
        print("5. Sắp xếp cầu thủ theo số huy chương")
        print("6. Thoát")
        try:
            lua_chon = int(input("Nhập lựa chọn của bạn: "))
            if lua_chon == 1:
                xem_danh_sach_cau_thu(ds_cau_thu)
            elif lua_chon == 2:
                nhap_cau_thu(ds_cau_thu)
            elif lua_chon == 3:
                xoa_cau_thu(ds_cau_thu)
            elif lua_chon == 4:
                sua_cau_thu(ds_cau_thu)
            elif lua_chon == 5:
                sap_xep_cau_thu(ds_cau_thu)
            elif lua_chon == 6:
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()