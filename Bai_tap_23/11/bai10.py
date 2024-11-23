chuoi_nhap = input("Nhap vao chuoi ky tu: ")

so = ""
chu = ""

for ky_tu in chuoi_nhap:
    if ky_tu.isdigit():
        so += ky_tu
    else:
        chu += ky_tu

chuoi_moi = so + chu
print("Chuoi moi sau khi don tat ca so ve dau chuoi la:", chuoi_moi)
