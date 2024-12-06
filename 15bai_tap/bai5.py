# Nhập vào n
n = int(input("Nhập vào n = "))

# Tạo ma trận đơn vị
ma_tran_don_vi = []
for i in range(n):
    hang = [0] * n
    hang[i] = 1
    ma_tran_don_vi.append(hang)

# In ma trận đơn vị
for hang in ma_tran_don_vi:
    print(hang)
