"""
    
"""
import os
import json
import subprocess

# Đường dẫn IDM và các cấu hình
IDM_PATH = r"C:\Program Files (x86)\Internet Download Manager\IDMan.exe"
BASE_URL = "https://tonofura-r-cdn-resource.deepone-online.com/deep_one/download_adv"
BASE_SAVE_PATH = r"C:\Users\Admin\Downloads\d1 resource downloaded"

# Thư mục chứa file JSON
base_input_dir = r"C:\Users\Admin\Downloads\d1 resource"

# Các loại file và thư mục tương ứng
EXTENSIONS = {
    ".txt": lambda stt, animated: (os.path.join(BASE_SAVE_PATH, stt), f"{stt}a.txt" if animated else f"{stt}.txt"),
    ".mp3": lambda stt, animated: (os.path.join(BASE_SAVE_PATH, stt, f"hvoice_{stt}"), f"hvoice_{stt}.mp3"),
    ".jpg": lambda stt, animated: (os.path.join(BASE_SAVE_PATH, stt, f"hcg_{stt}"), f"hcg_hcg_{stt}.jpg"),
    ".mp4": lambda stt, animated: (os.path.join(BASE_SAVE_PATH, "ani", f"ani_{stt}"), f"ani {stt}.mp4") if animated else None
}

def add_to_idm_queue(url, save_path):
    """Thêm file vào hàng đợi IDM"""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    subprocess.call([IDM_PATH, '/a', '/d', url, '/p', os.path.dirname(save_path), '/f', os.path.basename(save_path), '/n'])

def process_file(stt, filepath, animated=False):
    """Xử lý file JSON"""
    if not os.path.isfile(filepath):
        print(f"Không tìm thấy file: {filepath}")
        return
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    counts = {"mp3": 1, "jpg": 1, "mp4": 1}

    for dict in data["resource"]:
        file_path = dict["path"]
        file_md5 = dict["md5"]
        ext = dict["fileName"][-4:]

        # Tạo URL tải
        download_url = f"{BASE_URL}/{file_path}/{file_md5}{ext}"

        # Xác định đường lưu file và tên file
        save_info = EXTENSIONS.get(ext)
        if not save_info:
            continue

        save_folder, save_name = save_info(stt, animated)
        if not save_folder:
            continue

        save_path = os.path.join(save_folder, save_name)
        print(save_path)

        if os.path.exists(save_path):
            print(f"⏩ Bỏ qua (file đã tồn tại): {save_path}")
            continue

        # Thêm vào queue
        print(f"✅ Đưa vào queue: {download_url} -> {save_path}")
        add_to_idm_queue(download_url, save_path)

    print(f"🏁 Đã xử lý xong {stt}. Mở IDM -> Start Queue để tải nhé.")

if __name__ == "__main__":
    process_file("1051", r"C:\Users\Admin\Downloads\d1 resource\1051.txt")
