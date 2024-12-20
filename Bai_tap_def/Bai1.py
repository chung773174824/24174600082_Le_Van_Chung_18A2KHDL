def get_integer_input():
    while True:
        n = input("Nhap so nguyen n: ")
        if n.lstrip('-').isdigit():
            return int(n)
        else:
            print("Day khong phai la so nguyen, hay nhap lai")

number = get_integer_input()
print(f"{number} la so nguyen")