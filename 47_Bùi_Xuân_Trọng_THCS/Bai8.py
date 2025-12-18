n = int(input("Số lượng phần tử: "))
L = []
for i in range(n): L += [int(input(f"Nhập L[{i}]: "))]
k = int(input("Nhập k: "))
k %= n
kq = [0] * n
for i in range(n):
    kq[(i + k) % n] = L[i]
print("List sau khi dịch:", kq)