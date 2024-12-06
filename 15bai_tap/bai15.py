#Bài 15: Viết một chương trình quản lý một danh sách sinh viên.
# Danh sách sinh viên chứa các thông tin:
# - "Mã sinh viên"
# - "Họ đệm"
# - "Tên"
# - "Điểm toán"
# - "Điểm lý"
# - "Điểm hóa"
# - "Điểm trung bình" được tính từ 3 điểm toán, lý, hóa
# Thiết kế chương trình quản lý có menu như sau:
# 1. Xem danh sách sinh viên
# 2. Nhập thông tin sinh viên mới vào danh sách
# 3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên
# 4. Xóa thông tin sinh viên ứng với mã sinh viên
# 5. Thoát chương trình
# Khởi tạo danh sách sinh viên rỗng
while True:
    print("MENU")
    print("1. Xem danh sách sinh viên")
    print("2. Nhập thông tin sinh viên mới vào danh sách")
    print("3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
    print("4. Xóa thông tin sinh viên ứng với mã sinh viên")
    print("5. Thoát chương trình")
    lua_chon = input("nhap lua chon: ")
    if lua_chon.isdigit() == False:
        print("yeu cau nhap lai")
    else:
        lua_chon = int(lua_chon)
        ds_sv = []
        if lua_chon == 1:
            print("Xem danh sách sinh viên")
            print(ds_sv)
        elif lua_chon == 2:
            # Danh sách sinh viên chứa các thông tin:
            # - "Mã sinh viên"
            # - "Họ đệm"
            # - "Tên"
            # - "Điểm toán"
            # - "Điểm lý"
            # - "Điểm hóa"
            # - "Điểm trung bình" được tính từ 3 điểm toán, lý, hóa
            print("nhap thong tin sinh vien vao danh sach")
            sv = ["ma_sv: ",
                  "ho_dem: ",
                  "ten: ",
                  "diem_toan: ",
                  "diem_ly: ",
                  "diem_hoa: ",
                  "diem_tb: "
                  ]
            #Cách 1: yc nhập vào số sv cần nhập
            n = int(input("nhap vao so sinh vien can cap nhap"))
            #
            n = int(n)
            for sv in range(n):
                print("")
        elif lua_chon == 3:

            print("chay 3")
        elif lua_chon == 4:
            print("chay 4")
        elif lua_chon == 5:
            print("thoat chuong trinh")
            break
        else:
            print("yeu cau nhap lai")