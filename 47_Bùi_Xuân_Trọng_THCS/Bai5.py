n = int(input("Số lượng phần tử: "))
L = []
for i in range(n): L += [int(input(f"Nhập L[{i}]: "))]
kq = []
for x in L:
    ton_tai = False
    for y in kq:
        if x == y: ton_tai = True; break
    if not ton_tai: kq += [x]
print("Sau khi lọc:", kq)
