# Nhập vào dãy A gồm n phần tử từ bàn phím
ds_so = []

while True:
    n = input("Nhập vào số phần tử n trong danh sách: ")
    if not n.isdigit():
        print("Yêu cầu nhập lại số nguyên dương!!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhập giá trị số thứ {i + 1}: ")
        try:
            so = float(so)
            break
        except ValueError:
            print("Yêu cầu nhập vào số!!")
    ds_so.append(so)

# Tính tổng các phần tử trong dãy A
tong = sum(ds_so)
print(f"Tổng các số vừa nhập: {tong}")
