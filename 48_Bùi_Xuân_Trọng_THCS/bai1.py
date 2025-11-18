import math

n = int(input("Nhập một số: "))

if n < 0:
    print("Số âm không phải là số chính phương")
else:
    can = int(math.sqrt(n))
    if can * can == n:
        print(n, "là số chính phương")
    else:
        print(n, "không phải số chính phương")

