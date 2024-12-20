def get_product_of_numbers():
    product = 1
    while True:
        try:
            user_input = input("Nhap so nguyen (hoac 'done' de ket thuc): ")
            if user_input.lower() == 'done':
                break
            number = int(user_input)
            product = product * number
        except ValueError:
            print("Hay nhap so nguyen hop le hoac 'done' de ket thuc")
    
    print(f"Tich cua cac so da nhap la: {product}")

get_product_of_numbers()