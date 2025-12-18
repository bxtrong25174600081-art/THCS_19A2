r = int(input("Số hàng: "))
c = int(input("Số cột: "))
mt = []
for i in range(r):
    h = []
    for j in range(c): h += [int(input(f"Nhập mt[{i}][{j}]: "))]
    mt += [h]
max_s = -999999
idx = 0
for i in range(r):
    s = 0
    for val in mt[i]: s += val
    if s > max_s: max_s = s; idx = i
print(f"Hàng {idx} có tổng lớn nhất: {max_s}")