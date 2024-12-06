# Nhập số lượng sinh viên
ds_sinh_vien = []
n = int(input("Nhập số lượng sinh viên: "))
for sinh_vien in range(n):
    print(f"Nhập thông tin sinh viên thứ {sinh_vien + 1}:")
    ten = input("Tên sinh viên: ")
    diem = float(input("Điểm tổng kết cuối năm: "))
    thong_tin_sinh_vien = {"Tên": ten, "Điểm": diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)

# In danh sách sinh viên
print("\nDanh sách sinh viên:")
for sv in ds_sinh_vien:
    print(f"Tên: {sv['Tên']}, Điểm: {sv['Điểm']}")
