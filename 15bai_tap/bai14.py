# Nhập số lượng sinh viên
n = int(input("Nhập số lượng sinh viên: "))

sinh_vien = []

# Nhập thông tin cho từng sinh viên
for i in range(n):
    print(f"Nhập thông tin cho sinh viên {i + 1}:")
    ten = input("Tên sinh viên: ")
    diem = float(input("Điểm tổng kết: "))
    sinh_vien.append({"Tên": ten, "Điểm tổng kết": diem})

# In danh sách sinh viên hiện tại
print("\nDanh sách sinh viên hiện tại:")
for sv in sinh_vien:
    print(f"Tên: {sv['Tên']}, Điểm tổng kết: {sv['Điểm tổng kết']}")

# Nhập tên sinh viên cần sửa thông tin
ten_sua = input("\nNhập tên sinh viên cần sửa thông tin: ")

# Sửa thông tin sinh viên ứng với tên được nhập
sinh_vien_tim_thay = False
for sv in sinh_vien:
    if sv['Tên'] == ten_sua:
        sinh_vien_tim_thay = True
        diem_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_sua}: "))
        sv['Điểm tổng kết'] = diem_moi
        print(f"Đã cập nhật điểm cho sinh viên {ten_sua}")
        break

if not sinh_vien_tim_thay:
    print(f"Sinh viên có tên {ten_sua} không tồn tại")

# In danh sách sinh viên sau khi sửa
print("\nDanh sách sinh viên sau khi sửa:")
for sv in sinh_vien:
    print(f"Tên: {sv['Tên']}, Điểm tổng kết: {sv['Điểm tổng kết']}")
