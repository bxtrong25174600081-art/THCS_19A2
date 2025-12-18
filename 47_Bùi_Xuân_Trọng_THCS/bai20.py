n = int(input("Nhập số cặp key-value: "))
d = {}
for i in range(n):
    key = input("Nhập key: ")
    value = int(input("Nhập value: "))
    d[key] = value
ket_qua = {}
for k in d:
    if d[k] > 50:
        ket_qua[k] = d[k]
print("Các cặp thỏa điều kiện:", ket_qua)