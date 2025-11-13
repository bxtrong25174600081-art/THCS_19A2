kwh = int(input("Nhập số kWh điện tiêu thụ: "))

if kwh <= 100:
    tien = kwh * 1678
elif kwh <= 200:
    tien = 100 * 1678 + (kwh - 100) * 1734
else:
    tien = 100 * 1678 + 100 * 1734 + (kwh - 200) * 2014

print("Tổng tiền điện phải trả:", tien, "VNĐ")
