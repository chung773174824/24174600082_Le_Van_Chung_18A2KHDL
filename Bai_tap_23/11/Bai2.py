chuoi_nhap_vao = input("nhap vao chuoi ky tu: ")
tach_chuoi = chuoi_nhap_vao.split()  # Tách chuỗi thành danh sách các phần tử (split)
chuoi_ket_qua = " ".join(tach_chuoi)  # Nối các phần tử trong danh sách thành một chuỗi (join)
print(f"Chuoi ket qua: {chuoi_ket_qua}")
