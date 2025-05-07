import os
basedir = r"C:\Users\Admin\Downloads\d1 resource downloaded\ani"
def deleteMP4(stt):
    for i in range(stt):
        ani_dir = os.path.join(basedir,f"ani_{i}")
        if os.path.exists(ani_dir):
            for j in range(1,16):
                mp4_file = os.path.join(ani_dir,f"ani {j}.mp4")
                webm_file = os.path.join(ani_dir,f"Ani {j}.webm")
                if os.path.exists(mp4_file) and os.path.exists(webm_file):
                    os.remove(mp4_file)
if __name__=="__main__":
    stt = open(r"C:\Users\Admin\Downloads\stt.txt").read()
    deleteMP4(int(stt))