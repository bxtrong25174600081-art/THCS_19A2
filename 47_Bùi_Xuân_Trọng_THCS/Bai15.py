import math
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    can_bac_hai = int(math.sqrt(n))
    
    for i in range(2, can_bac_hai + 1):
        if n % i == 0:
            return False 
        return True
print("Danh sách các số nguyên tố trong khoảng [100, 500]:")
count = 0 
for so in range(100, 501):
    if kiem_tra_nguyen_to(so):
        print(so, end=" ") 
        count += 1
        if count % 10 == 0:
            print() 

print("\n\nTổng cộng tìm thấy:", count, "số nguyên tố.")