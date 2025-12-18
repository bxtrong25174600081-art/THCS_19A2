n = int(input("Nhập số phần tử: "))
a = [0] * n
for i in range(n):
    a[i] = int(input())
tong_chan = 0
tong_le = 0
for i in range(n):
    if a[i] % 2 == 0:
        tong_chan = tong_chan + a[i]
    else:
        tong_le = tong_le + a[i]
print("Tổng chẵn:", tong_chan)
print("Tổng lẻ:", tong_le)