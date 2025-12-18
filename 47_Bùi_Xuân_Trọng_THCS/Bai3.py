s = input("Nhập chuỗi: ")
kq = ""
space = False
for ch in s:
    if ch == " ":
        if not space:
            kq += ch
        space = True
    else:
        kq += ch
        space = False
print(kq)