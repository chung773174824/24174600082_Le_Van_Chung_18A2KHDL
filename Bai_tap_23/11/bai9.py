chuoi_nhi_phan = input("Nhap vao chuoi nhi phan (chi gom 0 va 1): ")

# Kiểm tra xem chuỗi có phải số nhị phân không
is_nhi_phan = all(ky_tu in '01' for ky_tu in chuoi_nhi_phan)

if is_nhi_phan:
    so_thap_phan = int(chuoi_nhi_phan, 2)
    print(f"So thap phan tuong ung la: {so_thap_phan}")
else:
    print("Chuoi khong phai la so nhi phan hop le.")
