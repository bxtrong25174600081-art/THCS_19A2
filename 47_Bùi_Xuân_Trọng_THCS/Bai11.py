n = int(input("Nhập kích thước ma trận vuông n: "))
matrix = []
for i in range(n):
    hang = []
    for j in range(n):
        val = int(input(f"Nhập phần tử [{i}][{j}]: "))
        hang += [val]
    matrix += [hang]
la_doi_xung = True
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            la_doi_xung = False
            break

if la_doi_xung:
    print("Đây là ma trận đối xứng.")
else:
    print("Đây không phải ma trận đối xứng.")