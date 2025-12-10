def tim_so_nguyen_lon_nhat(a,b,c):
    kq = None
    if a % 2 != 0: 
        kq = a
    if b % 2 != 0:
        if kq is None or b > kq :
            kq = b
    if c % 2 != 0:
        if kq is None or c > kq :
            kq = c
    if kq is None:
        return "-1"
    else:
        return kq
a = 10481
b = 3246
c = 32456
print (tim_so_nguyen_lon_nhat(a,b,c))