luong_cb = float(input("Nhập mức lương cơ bản: "))
ngay_cong = int(input("Nhập số ngày công: "))

luong_ngay = luong_cb / 22
tong_luong = luong_ngay * ngay_cong

if ngay_cong > 22:
    tong_luong += tong_luong * 0.1  # thưởng 10%
elif ngay_cong < 22:
    tong_luong -= tong_luong * 0.05  # phạt 5%

print("Tổng lương thực nhận:")
