n_A = int(input("Tập A có bao nhiêu phần tử? "))
tap_A = set()
for i in range(n_A):
    gia_tri = input(f"Nhập phần tử thứ {i+1} của A: ")
    tap_A.add(gia_tri)

n_B = int(input("Tập B có bao nhiêu phần tử? "))
tap_B = set()
for i in range(n_B):
    gia_tri = input(f"Nhập phần tử thứ {i+1} của B: ")
    tap_B.add(gia_tri)
tap_giao = set()
for phan_tu in tap_A:
    if phan_tu in tap_B:
        tap_giao.add(phan_tu)
hieu_A_B = set()
for phan_tu in tap_A:
    if phan_tu not in tap_B:
        hieu_A_B.add(phan_tu)
tap_hop = set()
for phan_tu in tap_A:
    tap_hop.add(phan_tu)
for phan_tu in tap_B:
    tap_hop.add(phan_tu)

print("Giao của hai tập hợp:", tap_giao)
print("Hiệu A - B:", hieu_A_B)
print("Hợp của hai tập hợp:", tap_hop)