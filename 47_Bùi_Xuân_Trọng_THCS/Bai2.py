s = input("Nhập chuỗi: ")
n = int(input("Nhập độ dài n: "))

tu_hien_tai = ""
for ky_tu in s:
    if ky_tu != " ":
        tu_hien_tai += ky_tu
    else:
        do_dai = 0
        for _ in tu_hien_tai: 
            do_dai += 1
        if do_dai > n:
            print(tu_hien_tai)
        tu_hien_tai = ""
do_dai_cuoi = 0
for _ in tu_hien_tai: 
    do_dai_cuoi += 1

if do_dai_cuoi > n:
    print(tu_hien_tai)