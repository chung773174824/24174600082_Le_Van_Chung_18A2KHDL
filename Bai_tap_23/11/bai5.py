chuoi_nhap = input("Nhap vao chuoi ky tu: ")

viet_hoa = 0
viet_thuong = 0

for chu in chuoi_nhap:
    if chu.isupper():  # Kiểm tra chữ hoa
        viet_hoa += 1
    elif chu.islower():  # Kiểm tra chữ cái in thường
        viet_thuong += 1

print(f"Chu cai in hoa: {viet_hoa}")
print(f"Chu cai in thuong: {viet_thuong}")
