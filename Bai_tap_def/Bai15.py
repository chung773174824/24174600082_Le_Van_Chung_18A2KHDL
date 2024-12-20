def is_perfect_number(n):
    if n <= 1:
        return False
    divisors_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors_sum = divisors_sum + i
    return divisors_sum == n

def get_smallest_perfect_number():
    while True:
        try:
            input_str = input("Nhap day so nguyen (cach nhau boi dau cach, hoac 'done' de ket thuc): ")
            
            if input_str.lower() == 'done':
                break
            
            numbers = list(map(int, input_str.split()))
            
            perfect_numbers = [num for num in numbers if is_perfect_number(num)]
            
            if not perfect_numbers:
                print("Khong co so hoan hao trong day")
            else:
                smallest_perfect = min(perfect_numbers)
                print(f"So hoan hao nho nhat trong day la: {smallest_perfect}")
            break
            
        except ValueError:
            print("Hay nhap day so nguyen hop le hoac 'done' de ket thuc")


get_smallest_perfect_number()