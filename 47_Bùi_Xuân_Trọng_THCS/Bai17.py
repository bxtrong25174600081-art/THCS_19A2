n = int(input("Nhập số cặp key-value: "))
d = {}
for i in range(n):
    key = input("Nhập key: ")
    value = int(input("Nhập value: "))
    d[key] = value
max_key = None
max_value = None
for k in d:
    if max_value is None or d[k] > max_value:
        max_value = d[k]
        max_key = k
print("Key có value lớn nhất:", max_key)