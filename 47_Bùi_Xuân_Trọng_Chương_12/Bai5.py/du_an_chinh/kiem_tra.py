import sys
# Thêm đường dẫn thư mục thu_vien_chung vào hệ thống
sys.path.append("../thu_vien_chung") 

from thu_vien_chung import xu_ly_so

n = 17
result = xu_ly_so.kiem_tra_so_nguyen_to(n)

print(f"Số {n} là SNT:", result)