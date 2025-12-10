def kiem_tra_so_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:  
            tong_uoc += i
    return tong_uoc == n

def tinh_tong_so_hoan_hao(a, b):
    tong_ket_qua = 0
    for so_hien_tai in range(a, b + 1):
        if kiem_tra_so_hoan_hao(so_hien_tai):
            print(f"-> Tìm thấy số hoàn hảo: {so_hien_tai}")
            tong_ket_qua += so_hien_tai
            
    return tong_ket_qua
a = 1
b = 30
ket_qua = tinh_tong_so_hoan_hao(a, b)
print(f"Tổng các số hoàn hảo từ {a} đến {b} là: {ket_qua}")