n = int(input("Bạn muốn nhập bao nhiêu số vào Tuple? "))
danh_sach_tam = []
for i in range(n):
    so = int(input(f"Nhập số thứ {i+1}: "))
    danh_sach_tam += [so]
tup_goc = tuple(danh_sach_tam)

ds_chan = []
ds_le = []
tong_chan = 0
tong_le = 0

for so in tup_goc:
    if so % 2 == 0:
        ds_chan += [so]
        tong_chan += so
    else:
        ds_le += [so]
        tong_le += so

print("Tuple chẵn:", tuple(ds_chan), "- Tổng:", tong_chan)
print("Tuple lẻ:", tuple(ds_le), "- Tổng:", tong_le)