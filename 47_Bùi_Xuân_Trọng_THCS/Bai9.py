def tinh_tong_chu_so(n):
    if n < 10:
        return n
    else:
        chu_so_cuoi = n % 10
        phan_con_lai = n // 10
        return chu_so_cuoi + tinh_tong_chu_so(phan_con_lai)
n = 12345
ket_qua = tinh_tong_chu_so(n)
print(f"Tổng các chữ số của {n} là: {ket_qua}")