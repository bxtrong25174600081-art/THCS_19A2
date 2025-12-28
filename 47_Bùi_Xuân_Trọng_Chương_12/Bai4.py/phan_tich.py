from du_lieu import danh_sach, tu_dien

# Dữ liệu có sẵn
ds = [5, 6, 7, 8, 9]
diction = {"ten": "Tờ Rọng", "tuoi": 18, "thanh_pho": "Hanoi"}

# Gọi hàm từ module
x = danh_sach.sap_xep_tang_dan(ds)
y = tu_dien.lay_gia_tri(diction, "ten")

# In kết quả
print(x)
print(y)