# Nhập vào số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
A = []
B = []

# Phân loại số lẻ và số chẵn nhỏ hơn n
for i in range(n):
    if i % 2 != 0:
        A.append(i)
    else:
        B.append(i)

# Sắp xếp dãy số theo thứ tự giảm dần
A.sort(reverse=True)
B.sort(reverse=True)

# In ra danh sách A và B
print("Danh sách A (số lẻ):", A)
print("Danh sách B (số chẵn):", B)
