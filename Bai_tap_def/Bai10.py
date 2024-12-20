import math

def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def decimal_to_fraction(decimal):
    str_decimal = str(decimal)
    if '.' in str_decimal:
        decimal_places = len(str_decimal.split('.')[1])
    else:
        decimal_places = 0
    denominator = 10 ** decimal_places
    numerator = int(decimal * denominator)
    common_divisor = ucln(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def get_decimal_input():
    while True:
        try:
            decimal = float(input("Nhap so thap phan: "))
            numerator, denominator = decimal_to_fraction(decimal)
            print(f"So thap phan {decimal} duoi dang phan so toi gian la: {numerator}/{denominator}")
            break
        except ValueError:
            print("Hay nhap so thap phan hop le")

get_decimal_input()