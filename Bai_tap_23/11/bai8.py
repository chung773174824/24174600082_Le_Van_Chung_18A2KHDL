str_1 = input("Nhap vao chuoi str_1: ")
str_2 = input("Nhap vao chuoi str_2: ")

if str_2 in str_1:
    print(f"'{str_2}' nam trong '{str_1}'")
else:
    print(f"'{str_2}' khong nam trong '{str_1}'")

if str_1 in str_2:
    print(f"'{str_1}' nam trong '{str_2}'")
else:
    print(f"'{str_1}' khong nam trong '{str_2}'")
