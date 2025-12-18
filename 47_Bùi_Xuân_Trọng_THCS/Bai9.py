n = int(input("Kích thước ma trận vuông n: "))
mt = []
for i in range(n):
    hang = []
    for j in range(n): hang += [int(input(f"Nhập mt[{i}][{j}]: "))]
    mt += [hang]
tong = 0
for i in range(n): tong += mt[i][n - 1 - i]
print("Tổng chéo phụ:", tong)