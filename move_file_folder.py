import os
import shutil
src = r"C:\Users\Admin\Downloads\d1 resource"
des_sp = r"D:\viewer\DeepOneViewerRe-1.0-pc\DeepOneViewerRe-1.0-pc\game\images\sp"
des_cg = r"D:\viewer\DeepOneViewerRe-1.0-pc\DeepOneViewerRe-1.0-pc\game\images\cg"
des_thumb = r"D:\viewer\DeepOneViewerRe-1.0-pc\DeepOneViewerRe-1.0-pc\game\images\thumb"
def movefile(stt:int):
    """ sp, thumb, cg
    """
    for i in range (1,stt):
        sp = os.path.join(src,f"sp_sp_{i}.png")
        sp_des = os.path.join(des_sp,f"sp_sp_{i}.png")

        cg = os.path.join(src,f"cg_cg_{i}.png")
        cg_des = os.path.join(des_cg, f"cg_cg_{i}.png")

        thumb = os.path.join(src,f"thumb_thumb_{i}.png")
        thumb_des = os.path.join(des_thumb,f"thumb_thumb_{i}.png")
        if os.path.exists(sp):
            shutil.move(sp,sp_des)
            shutil.move(thumb,thumb_des)
        if os.path.exists(cg):
            shutil.move(cg,cg_des)
        print(f"dã di chuyển {i}")
dlded= r'C:\Users\Admin\Downloads\d1 resource downloaded'
script =r"D:\viewer\DeepOneViewerRe-1.0-pc\DeepOneViewerRe-1.0-pc\game\script"
hcgdes = r'D:\viewer\DeepOneViewerRe-1.0-pc\DeepOneViewerRe-1.0-pc\game\images\hcg'
voicedes = r"D:\viewer\DeepOneViewerRe-1.0-pc\DeepOneViewerRe-1.0-pc\game\audio\hvoice"
anides = r"D:\viewer\DeepOneViewerRe-1.0-pc\DeepOneViewerRe-1.0-pc\game\images\ani"
def moveFolder (stt:int):
    """ hcg, ani, hvoice
        stt text
    """
    for i in range(1,stt):
        folderSTT = os.path.join(dlded,f"{i}")
        if os.path.exists(folderSTT):
            ## ben trong folder
            ###txt


            txtFile = os.path.join(folderSTT,f"{i}.txt")
            scriptDES = os.path.join(script,fr"hscript og\{i}.txt")
            txtANI = os.path.join(folderSTT,f"{i}a.txt")
            scriptaniDES = os.path.join(script,fr"hscript og\{i}a.txt")
            if os.path.exists(txtFile):
                shutil.move (txtFile, scriptDES)
            if os.path.exists(txtANI):
                shutil.move(txtANI,scriptaniDES)

            ##hcg , ani, audio
            hcgfolder = os.path.join(folderSTT,f"hcg_{i}")
            hvoicefolder = os.path.join(folderSTT, f"hvoice_{i}")
            if os.path.exists(hcgfolder):
                shutil.move(hcgfolder,os.path.join(hcgdes,f"hcg_{i}"))
                shutil.move(hvoicefolder, os.path.join(voicedes,f"hvoice_{i}"))
            anifolder = os.path.join(dlded,fr"ani\ani_{i}")
            if os.path.exists(anifolder):
                shutil.move(anifolder,os.path.join(anides,f"ani_{i}"))
        print(f"move folder{i}")
if __name__=="__main__":
    moveFolder(1000)