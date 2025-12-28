ten_nguon = "nguon.jpg"
ten_dich = "copy_nguon".jpg
with open(ten_nguon, 'rb') as f_nguon:
    with open(ten_dich, 'wb') as f_dich:
        while True:
            khoi_du_lieu = f_nguon.read(1024)
            if not khoi_du_lieu:
                break
            f_dich.write(khoi_du_lieu)
print("Đã sao chép tập tin thành công!")