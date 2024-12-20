def is_perfect_number(n):
    if n <= 1:
        return False
    divisors_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors_sum = divisors_sum + i
    return divisors_sum == n

def get_perfect_number_input():
    while True:
        n = input("Nhap so nguyen duong n: ")
        if n.isdigit():
            num = int(n)
            if is_perfect_number(num):
                return num
            else:
                print(f"{num} khong phai la so hoan hao, hay nhap lai")
        else:
            print("Day khong phai so nguyen hop le, hay nhap lai")

number = get_perfect_number_input()
print(f"{number} la so hoan hao")