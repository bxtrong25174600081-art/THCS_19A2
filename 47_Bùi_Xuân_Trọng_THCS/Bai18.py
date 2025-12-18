n = int(input("Nhập số cặp key-value: "))
d = {}
for i in range(n):
    key = input("Nhập key: ")
    value = input("Nhập value: ")
    d[key] = value
dao = {}
for k in d:
    v = d[k]
    dao[v] = k
print("Dictionary đảo:", dao)