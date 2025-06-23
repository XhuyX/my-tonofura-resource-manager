import os
import json
import subprocess

# Đường dẫn IDM
IDM_PATH = r"C:\Program Files (x86)\Internet Download Manager\IDMan.exe"

# Link gốc
BASE_URL = "https://tonofura-r-cdn-resource.deepone-online.com/deep_one/download_adv"

# Thư mục lưu
BASE_SAVE_PATH = r"C:\Users\Admin\Downloads\d1 resource downloaded"

# Thư mục chứa file JSON
base_input_dir = r"C:\Users\Admin\Downloads\d1 resource"

def add_to_idm_queue(url, save_path):
    """Thêm file vào hàng đợi IDM"""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    subprocess.call([
        IDM_PATH,
        '/a',  # Add vào queue
        '/d', url,
        '/p', os.path.dirname(save_path),
        '/f', os.path.basename(save_path),
        '/n'  # Không hiện hộp thoại
    ])

def process_file(stt, filepath, animated = False):
    """Xử lý file JSON"""
    if not os.path.isfile(filepath):
        print(f"Không tìm thấy file: {filepath}")
        return
    
    # Đọc JSON
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Đếm thứ tự
    mp3_cnt = 1
    jpg_cnt = 1
    mp4_cnt = 1

    for dict in data["resource"]:
        file_path = dict["path"]
        file_md5 = dict["md5"]
        ext = dict["fileName"][-4:]

        # Tạo URL tải
        download_url = f"{BASE_URL}/{file_path}/{file_md5}{ext}"

        # Xác định đường lưu file
        if ext == ".txt":
            save_folder = os.path.join(BASE_SAVE_PATH, stt)
            save_name = f"{stt}a.txt" if animated else f"{stt}.txt"
        elif ext == ".mp3":
            save_folder = os.path.join(BASE_SAVE_PATH, stt, f"hvoice_{stt}")
            save_name = f"hvoice_{mp3_cnt}.mp3"
            mp3_cnt += 1
        elif ext == ".jpg":
            save_folder = os.path.join(BASE_SAVE_PATH, stt, f"hcg_{stt}")
            save_name = f"hcg_hcg_{stt}{jpg_cnt}.jpg"
            jpg_cnt += 1
        elif ext == ".mp4" and animated:
            save_folder = os.path.join(BASE_SAVE_PATH, "ani", f"ani_{stt}")
            save_name = f"ani {mp4_cnt}.mp4"
            mp4_cnt += 1


        save_path = os.path.join(save_folder, save_name)
        print(save_path)
        # # Nếu file đã tồn tại thì bỏ qua
        if os.path.exists(save_path):
            print(f"⏩ Bỏ qua (file đã tồn tại): {save_path}")
            continue

        # # Thêm vào queue
        print(f"✅ Đưa vào queue: {download_url} -> {save_path}")
        add_to_idm_queue(download_url, save_path)


    print(f"🏁 Đã xử lý xong {stt}. Mở IDM -> Start Queue để tải nhé.")

if __name__=="__main__":
    process_file("1051",r"C:\Users\Admin\Downloads\d1 resource\1051.txt")
