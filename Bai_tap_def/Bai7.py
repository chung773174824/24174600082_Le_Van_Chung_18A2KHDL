def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_ucln_input():
    while True:
        try:
            num1 = int(input("Nhap so nguyen thu nhat: "))
            num2 = int(input("Nhap so nguyen thu hai: "))
            result = ucln(num1, num2)
            print(f"Uoc chung lon nhat cua {num1} va {num2} la: {result}")
            break
        except ValueError:
            print("Hay nhap so nguyen hop le")

get_ucln_input()