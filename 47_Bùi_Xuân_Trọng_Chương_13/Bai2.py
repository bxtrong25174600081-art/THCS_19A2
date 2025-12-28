noi_dung = """Python là một ngôn ngữ lập trình
mạnh mẽ, dễ học và có nhiều ứng dụng. Nó được sử dụng rộng rãi trong phát
triển web, khoa học dữ liệu, trí tuệ nhân tạo và tự động hóa. Cộng đồng Python
rất lớn và hỗ trợ tuyệt vời, với nhiều thư viện phong phú để giải quyết mọi vấn
đề."""
with open("vanban.txt", "w", encoding="utf-8") as file:
    file.write(noi_dung)
with open("vanban.txt", "r", encoding="utf-8") as file:
    noi_dung = file.read()
print(noi_dung)
cac_tu = noi_dung.lower().split()
tan_suat = {}
for tu in cac_tu:
    tu = tu.strip(".,;:!?()")
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1
print(tan_suat)