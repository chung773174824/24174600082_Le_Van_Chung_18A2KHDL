def find_divisors(n):
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def get_divisors_input():
    while True:
        try:
            num = int(input("Nhap so nguyen: "))
            divisors = find_divisors(num)
            print(f"Cac uoc cua {num} la: {divisors}")
            break
        except ValueError:
            print("Hay nhap so nguyen hop le")

get_divisors_input()