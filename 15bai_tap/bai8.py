# Nhập số dòng (m) và số cột (n)
m = int(input("Nhập số dòng (m): "))
n = int(input("Nhập số cột (n): "))

# Khởi tạo ma trận A
A = []
print("Nhập các phần tử của ma trận A: ")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    A.append(row)

# Nhập chỉ số cột i và j cần đảo
i = int(input("Nhập chỉ số cột i (1 <= i <= n): ")) - 1
j = int(input("Nhập chỉ số cột j (1 <= j <= n): ")) - 1

# Đảo vị trí hai cột i và j
for row in A:
    row[i], row[j] = row[j], row[i]

# In ma trận sau khi đã đảo vị trí hai cột
print("Ma trận sau khi đảo vị trí hai cột i và j là: ")
for row in A:
    print(" ".join(map(str, row)))
