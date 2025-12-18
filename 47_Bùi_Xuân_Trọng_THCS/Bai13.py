r = int(input("Nhập số hàng: "))
c = int(input("Nhập số cột: "))

if r != c:
    print("Không phải ma trận vuông, nên không phải ma trận đơn vị.")
else:
    M = [[int(input(f"M[{i}][{j}]: ")) for j in range(c)] for i in range(r)]
    
    la_don_vi = True
    for i in range(r):
        for j in range(c):
            if i == j:
                if M[i][j] != 1:
                    la_don_vi = False
            else: 
                if M[i][j] != 0:
                    la_don_vi = False
                    
    if la_don_vi:
        print("Đây là ma trận đơn vị.")
    else:
        print("Đây không phải ma trận đơn vị.")