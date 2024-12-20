def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor = divisor + 1
    
    return factors

def get_prime_factors_input():
    while True:
        try:
            number = int(input("Nhap so nguen duong de tim thua so nguyen to: "))
            if number <= 1:
                print("Hay nhap so nguyen duong lon hon 1")
                continue
            
            factors = prime_factors(number)
            print(f"Cac thua so nguyen to cua {number} la: {factors}")
            break
        except ValueError:
            print("Hay nhap so nguyen hop le")

get_prime_factors_input()