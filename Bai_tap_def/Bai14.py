def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_average_of_primes():
    primes = []
    while True:
        try:
            input_str = input("Nhap day so nguyen (cach nhau boi dau cach, hoac 'done' de ket thuc): ")
            
            if input_str.lower() == 'done':
                break
            
            numbers = list(map(int, input_str.split()))
            
            for num in numbers:
                if is_prime(num):
                    primes.append(num)
            
            if len(primes) == 0:
                print("Khong co so nguyen to trong day")
            else:
                average = sum(primes) / len(primes)
                print(f"Gia tri trung binh cua cac so nguyen to la: {average}")
            break
            
        except ValueError:
            print("Hay nhap day so nguyen hop le hoac 'done' de ket thuc")

get_average_of_primes()