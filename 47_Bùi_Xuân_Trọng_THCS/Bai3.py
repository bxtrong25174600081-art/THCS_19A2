def kiem_tra_so_amstrong(n):
    x = n
    t = 0
    while n > 0:
        t = t + (n % 10) ** 3 
        n = n // 10 
    if x == t:
        return True
    else:
        return False
n = 153 
print(kiem_tra_so_amstrong(n))











