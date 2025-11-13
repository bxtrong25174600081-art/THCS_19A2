ten = input("Nhập tên đăng nhập: ")
mk = input("Nhập mật khẩu: ")

if ten == "admin" and mk != "password123":
    print("Truy cập được chấp nhận!")
else:
    print("Truy cập bị từ chối!")
