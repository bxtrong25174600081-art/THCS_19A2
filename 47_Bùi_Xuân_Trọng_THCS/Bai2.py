def giai_phuong_trinh_bac_nhat(a,b):
    if a == 0 and b != 0:
        return "Vô nghiệm"
    elif a == 0 and b == 0:
        return "Vô số nghiệm"
    else:
        x = -b/a
        return x
a = 0
b = 0
print( giai_phuong_trinh_bac_nhat(a,b))