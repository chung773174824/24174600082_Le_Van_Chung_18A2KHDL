# Nhập số lượng sinh viên
n = int(input("Nhập số lượng sinh viên: "))

sinh_vien = []

# Nhập thông tin cho từng sinh viên
for i in range(n):
    print(f"Nhập thông tin cho sinh viên {i + 1}:")
    ten = input("Tên sinh viên: ")
    diem = float(input("Điểm tổng kết: "))
    sinh_vien.append({"Tên": ten, "Điểm tổng kết": diem})

# In tiêu đề bảng
print(f"\n{'Tên':<10} {'Điểm':>5}")

# In thông tin sinh viên theo định dạng
for sv in sinh_vien:
    print(f"{sv['Tên']:<10} {sv['Điểm tổng kết']:>5.1f}")
