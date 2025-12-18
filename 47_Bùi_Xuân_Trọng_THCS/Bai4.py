n = int(input("Nhập số phần tử: "))
a = [0] * n
for i in range(n):
    a[i] = int(input(f"Nhập a[{i}]: "))


max1 = -999999999
max2 = -999999999

for i in range(n):
    if a[i] > max1:
        max2 = max1 
        max1 = a[i] 
    elif a[i] > max2 and a[i] != max1:
        max2 = a[i]

if max2 == -999999999:
    print("Không tìm thấy số lớn thứ hai.")
else:
    print("Số lớn thứ hai là:", max2)