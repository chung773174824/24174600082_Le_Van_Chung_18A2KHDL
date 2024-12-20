def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_float_input():
    while True:
        n = input("Nhap so thuc n: ")
        if is_float(n):
            return float(n)
        else:
            print("Day khong phai so thuc, hay nhap lai")

number = get_float_input()
print(f"{number} la so thuc")