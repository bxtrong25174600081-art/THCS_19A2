n = int(input("Nhập số phần tử: "))
a = [0] * n
for i in range(n):
    a[i] = int(input())
k = int(input("Nhập k: "))
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            print(a[i], a[j])