# Nhập số dòng và số cột của ma trận A và B
m = int(input("Nhập số dòng của ma trận A và B: "))
n = int(input("Nhập số cột của ma trận A và B: "))

# Khởi tạo ma trận A
A = []
print("Nhập ma trận A: ")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    A.append(row)

# Khởi tạo ma trận B
B = []
print("Nhập ma trận B: ")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"B[{i+1}][{j+1}]: "))
        row.append(element)
    B.append(row)

# Tính tổng hai ma trận A + B
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("\nTổng hai ma trận A và B là: ")
for row in C:
    print(" ".join(map(str, row)))

# Tính hiệu hai ma trận A - B
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] - B[i][j])
    C.append(row)

print("\nHiệu hai ma trận A và B là: ")
for row in C:
    print(" ".join(map(str, row)))

# Tính tích ma trận A với số k
k = int(input("\nNhập số k để nhân với ma trận A: "))
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] * k)
    C.append(row)

print(f"\nTích của ma trận A với số {k} là: ")
for row in C:
    print(" ".join(map(str, row)))

# Tích hai ma trận A và B
if len(A[0]) == len(B):
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        C.append(row)
    print("\nTích hai ma trận A và B là: ")
    for row in C:
        print(" ".join(map(str, row)))
else:
    print("\nKhông thể nhân hai ma trận này")

# Ma trận đối xứng của A
if m == n:
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[j][i])
        C.append(row)
    print("\nMa trận đối xứng của A là: ")
    for row in C:
        print(" ".join(map(str, row)))
else:
    print("\nMa trận A không phải là ma trận vuông, không thể tính ma trận đối xứng")
