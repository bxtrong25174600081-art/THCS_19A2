import csv
with open("nhan_vien.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Lương"])
    writer.writerow([1, "Trường", 50000])
    writer.writerow([2, "Linh", 20000])
    writer.writerow([3, "Thảo", 75000])
    writer.writerow([4, "Trọng", 80000])
with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if int(row["Lương"]) > 50000:
            print(row)