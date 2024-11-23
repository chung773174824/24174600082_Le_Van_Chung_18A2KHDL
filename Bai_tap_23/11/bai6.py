nhap_vao_chuoi = input("Nhap vao chuoi ky tu: ")
if nhap_vao_chuoi.startswith('-') and nhap_vao_chuoi[1:].isdigit():  # Kiểm tra số âm và chuỗi là số
    print("Chuoi la so am")
else:
    print("Chuoi khong phai so am")
