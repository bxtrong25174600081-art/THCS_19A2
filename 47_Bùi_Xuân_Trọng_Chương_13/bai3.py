danh_sach_cac_so = [10, 25, 30, 45, 50]

with open('so_nguyen.txt', 'w') as f:
    for n in danh_sach_cac_so:
        f.write(str(n) + "\n")