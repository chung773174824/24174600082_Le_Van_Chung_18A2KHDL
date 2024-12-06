# Nhập vào số nguyên dương n
ds_nguyen_to = []
while True:
    n = input("Nhập vào số nguyên dương n: ")
    if not n.isdigit():
        print("Yêu cầu nhập lại số nguyên dương!!")
    else:
        n = int(n)
        break

# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(k):
    if k < 2:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

# In ra các số nguyên tố nhỏ hơn n
for i in range(2, n):
    if la_so_nguyen_to(i):
        ds_nguyen_to.append(i)

# Sắp xếp và in danh sách các số nguyên tố
ds_nguyen_to.sort()
print(ds_nguyen_to)

# Tính tổng các giá trị trong danh sách
tong = sum(ds_nguyen_to)
print("Tổng các số nguyên tố:", tong)
