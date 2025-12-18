r1 = int(input("Nhập số hàng ma trận A: "))
c1 = int(input("Nhập số cột ma trận A: "))
r2 = int(input("Nhập số hàng ma trận B: "))
c2 = int(input("Nhập số cột ma trận B: "))

if c1 != r2:
    print("Phép nhân không khả thi vì số cột A khác số hàng B!")
else:
    print("Nhập ma trận A:")
    A = [[int(input(f"A[{i}][{j}]: ")) for j in range(c1)] for i in range(r1)]
    
    print("Nhập ma trận B:")
    B = [[int(input(f"B[{i}][{j}]: ")) for j in range(c2)] for i in range(r2)]
    C = []
    for i in range(r1):
        hang_moi = []
        for j in range(c2):
            hang_moi += [0]
        C += [hang_moi]
    for i in range(r1):
        for j in range(c2):
            tong_tich = 0
            for k in range(c1):
                tong_tich += A[i][k] * B[k][j]
            C[i][j] = tong_tich

    print("Ma trận tích C là:")
    for hang in C:
        print(hang)