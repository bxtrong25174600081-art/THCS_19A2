n = int(input("Nhập số sinh viên: "))
sv = {}
for i in range(n):
    ten = input("Nhập tên: ")
    diem = int(input("Nhập điểm: "))
    sv[ten] = diem
nhom = {}
for ten in sv:
    diem = sv[ten]
    if diem not in nhom:
        nhom[diem] = [ten]
    else:
        nhom[diem].append(ten)
print(nhom)