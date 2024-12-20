def is_positive_number(s):
    return s.isdigit() and int(s) > 0

def get_positive_number():
    while True:
        n = input("Nhap so duong n: ")
        if is_positive_number(n):
            return int(n)
        else:
            print("Day khong phai la so nguyen duong, hay nhap lai")

number = get_positive_number()
print(f"{number} la so nguyen duong")