import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n

def get_perfect_square_input():
    while True:
        n = input("Nhap so nguyen duong n: ")
        if n.isdigit():
            num = int(n)
            if is_perfect_square(num):
                return num
            else:
                print(f"{num} khong phai la so chinh phuong, hay nhap lai")
        else:
            print("Day khong phai so nguyen hop le, hay nhap lai")

number = get_perfect_square_input()
print(f"{number} la so chinh phuong")