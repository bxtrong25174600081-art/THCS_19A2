import os
if not os.path.exists("temp_files"):
    os.mkdir("temp_files")
    print("Đã tạo thư mục temp_files")
file_path = os.path.join("temp_files", "file.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Nội dung tệp tin tạm thời")
print("Đã tạo file.txt trong temp_files")
new_file_path = os.path.join("temp_files", "new_file.txt")
os.rename(file_path, new_file_path)
print("Đã đổi tên thành new_file.txt")
os.rename(new_file_path, "new_file.txt")
print("Đã di chuyển new_file.txt ra thư mục hiện tại")
os.rmdir("temp_files")
print("Đã xóa thư mục temp_files thành công")