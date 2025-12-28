import os
os.makedirs("my_project/src", exist_ok=True)
os.makedirs("my_project/docs", exist_ok=True)
os.makedirs("my_project/data", exist_ok=True)
open("my_project/src/main.py", "w").close()
open("my_project/docs/README.md", "w").close()
open("my_project/data/input.txt", "w").close()
print("Danh sach cac thu muc con trong my_project:")
sub_folders = os.listdir("my_project")
print(sub_folders)

for folder in sub_folders:
    path = os.path.join("my_project", folder)
    if os.path.isdir(path):
        files = os.listdir(path)
        print(f"Thu muc {folder} chua: {files}")