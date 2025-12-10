def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2,n):
      if  n % i == 0:
        return False
    return True
n = 2
print(la_so_nguyen_to(n))
def in_so_nguyen_to_trong_khoang(a,b):
    ket_qua_chuoi = ""
    for i in range(a,b+1):
        if la_so_nguyen_to(i):
            ket_qua_chuoi += str(i) + ", "
    return ket_qua_chuoi[:-2]
a = 1
b = 10
print(in_so_nguyen_to_trong_khoang(a,b))







