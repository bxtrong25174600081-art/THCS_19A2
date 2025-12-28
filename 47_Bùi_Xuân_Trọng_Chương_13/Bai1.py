noi_dung = """Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và có nhiều ứng dụng.
Nó được sử dụng rộng rãi trong phát triển web, khoa học dữ liệu, trí tuệ nhân tạo và tự động hóa.
Cộng đồng Python rất lớn và hỗ trợ tuyệt vời, với nhiều thư viện phong phú để giải quyết mọi vấn
đề."""
with open("python.txt", "w", encoding="utf-8") as file:
    file.write(noi_dung)
with open("python.txt", "r", encoding="utf-8") as file:
    van_ban = file.read()
so_tu = len(van_ban.split())
print(van_ban)
print("\nTổng số từ trong tập tin là:", so_tu)