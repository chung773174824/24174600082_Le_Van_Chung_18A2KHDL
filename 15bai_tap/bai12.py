# Nhập số lượng sinh viên
n = int(input("Nhập số lượng sinh viên: "))
sinh_vien = []
for i in range(n):
    print(f"Nhập thông tin cho sinh viên {i + 1}:")
    ten = input("Tên sinh viên: ")
    diem = float(input("Điểm tổng kết: "))
    sinh_vien.append({"Tên": ten, "Điểm tổng kết": diem})

# In danh sách sinh viên hiện tại
print("\nDanh sách sinh viên hiện tại:")
for sv in sinh_vien:
    print(f"Tên: {sv['Tên']}, Điểm tổng kết: {sv['Điểm tổng kết']}")

# Nhập tên sinh viên cần xóa
ten_xoa = input("\nNhập tên sinh viên cần xóa: ")

# Xóa thông tin sinh viên ứng với tên được nhập
sinh_vien = [sv for sv in sinh_vien if sv['Tên'] != ten_xoa]

# In danh sách sinh viên sau khi xóa
print("\nDanh sách sinh viên sau khi xóa:")
for sv in sinh_vien:
    print(f"Tên: {sv['Tên']}, Điểm tổng kết: {sv['Điểm tổng kết']}")
