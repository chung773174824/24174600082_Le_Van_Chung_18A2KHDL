nhap_vao_chuoi = input("Nhap vao chuoi ky tu: ")
try:
    float(nhap_vao_chuoi)
    print("Chuoi la so thap phan")
except ValueError:
    print("Chuoi khong phai so thap phan")
