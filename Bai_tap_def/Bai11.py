def get_sum_of_numbers():
    total = 0
    while True:
        try:
            user_input = input("Nhap so nguyen (hoac 'done' de ket thuc): ")
            if user_input.lower() == 'done':
                break
            number = int(user_input)
            total = total + number
        except ValueError:
            print("Hay nhap so nguyen hop le hoac 'done' de ket thuc.")
    
    print(f"Tong cua cac so da nhap la: {total}")

get_sum_of_numbers()