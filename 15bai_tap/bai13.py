# Nhập số lượng sinh viên
n = int(input("Nhập số lượng sinh viên: "))
sinh_vien = []
for i in range(n):
    print(f"Nhập thông tin cho sinh viên {i + 1}:")
    ten = input("Tên sinh viên: ")
    diem = float(input("Điểm tổng kết: "))
    sinh_vien.append({"Tên": ten, "Điểm tổng kết": diem})

# Nhập thông tin sinh viên mới
ten_moi = input("\nNhập tên sinh viên cần thêm: ")
diem_moi = float(input("Nhập điểm tổng kết của sinh viên: "))

# Kiểm tra xem sinh viên đã tồn tại hay chưa
sinh_vien_ton_tai = False
for sv in sinh_vien:
    if sv['Tên'] == ten_moi:
        sinh_vien_ton_tai = True
        break

if sinh_vien_ton_tai:
    print("Thông tin sinh viên đã tồn tại")
else:
    sinh_vien.append({"Tên": ten_moi, "Điểm tổng kết": diem_moi})
    print("Đã thêm sinh viên")

# In danh sách sinh viên hiện tại
print("\nDanh sách sinh viên hiện tại:")
for sv in sinh_vien:
    print(f"Tên: {sv['Tên']}, Điểm tổng kết: {sv['Điểm tổng kết']}")
