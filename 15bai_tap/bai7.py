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

# In ma trận A vừa nhập
print("Ma trận A vừa nhập là: ")
for row in A:
    print(" ".join(map(str, row)))

# Nhập hàng i và hàng j cần đảo
i = int(input("Nhập vào hàng i: "))
j = int(input("Nhập vào hàng j: "))

# Đảo vị trí hai hàng i và j
A[i], A[j] = A[j], A[i]

# In ma trận sau khi đã đảo vị trí hai hàng
print("Ma trận sau khi đã đảo vị trí hai hàng là: ")
for row in A:
    print(" ".join(map(str, row)))
