"""
    lý do có kiểm tra Ani [j].webm là để xác định video ani đã được đưa vào handbrake
"""
import os

basedir = r"C:\Users\Admin\Downloads\d1 resource downloaded\ani"

def deleteMP4(stt):
    for i in range(stt):
        ani_dir = os.path.join(basedir, f"ani_{i}")
        if os.path.exists(ani_dir):
            for j in range(1, 16):
                files = [os.path.join(ani_dir, f"ani {j}.mp4"), os.path.join(ani_dir, f"Ani {j}.webm")]
                if all(os.path.exists(file) for file in files):
                    os.remove(files[0])

if __name__ == "__main__":
    stt = int(open(r"C:\Users\Admin\Downloads\stt.txt").read())
    deleteMP4(stt)
