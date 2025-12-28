header = "ID, Tên sản phẩm, Giá\n"
rows = ["1, Laptop, 1200\n", "2, Chuột máy tính, 25\n", "3, Bàn phím, 75\n"]
with open('san_pham.txt', 'w', encoding='utf-8') as f:
    f.write(header + "".join(rows))
id_update = input("Nhập ID cần sửa: ")
gia_moi = input("Nhập giá mới: ")
new_data = []
with open('san_pham.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    new_data.append(lines[0])
    for line in lines[1:]:
        parts = line.strip().split(", ")
        if parts[0] == id_update:
            parts[2] = gia_moi
        new_data.append(", ".join(parts) + "\n")
with open('san_pham.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_data)