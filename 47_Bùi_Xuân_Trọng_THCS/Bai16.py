s = input("Nhập chuỗi: ")
dem = {}
for ch in s:
    if ch in dem:
        dem[ch] = dem[ch] + 1
    else:
        dem[ch] = 1
print(dem)