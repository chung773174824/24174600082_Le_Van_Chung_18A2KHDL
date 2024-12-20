def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Mau so khong the bang 0")
    u = ucln(numerator, denominator)
    return numerator // u, denominator // u

def get_fraction_input():
    while True:
        try:
            numerator = int(input("Nhap tu so: "))
            denominator = int(input("Nhap mau so: "))
            simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
            print(f"Phan so toi gian la: {simplified_numerator}/{simplified_denominator}")
            break
        except ValueError as e:
            print(e)

get_fraction_input()