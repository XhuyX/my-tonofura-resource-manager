import os
source = r'C:\Users\Admin\Downloads\d1 resource downloaded'
def lenani(stt):
    folder = os.path.join(source,fr'ani\ani_{stt}')
    aniImage = open(r'C:\Users\Admin\Downloads\after that\aniImage.txt','r').readlines()
    aniImage.append(f"#ani image {stt}\n")
    aniImagelen = len(os.listdir(folder))
    for i in range(1,aniImagelen+1):
        aniImage.append(f"image {stt}{i} = Movie(play = 'images/ani/ani_{stt}/Ani {i}.webm',size = (1280,720),loop = True)\n")
    aniImageWrite = open(r'C:\Users\Admin\Downloads\after that\aniImage.txt','w')
    for x in aniImage:
        aniImageWrite.write(x)
    aniAlbum = open(r'C:\Users\Admin\Downloads\after that\aniAlbum.txt','r').readlines()
    aniAlbum.append(f"# ani Album {stt}\n")
    string=f"    album_ani_{stt} =["
    for i in range(1,aniImagelen+1):
        string+= f"'{stt}{i}'"
        if (i!= aniImagelen):
            string+=','
    string+=']\n'
    aniAlbum.append(string)
    aniAlbumWrite = open(r'C:\Users\Admin\Downloads\after that\aniAlbum.txt','w')
    for x in aniAlbum:
        aniAlbumWrite.write(x)
    print(f"{stt} đã thêm khai báo ani image")
    # tra ve so luong mp4
    return aniImagelen
def lenHCG(stt):
    folder = os.path.join(source,f'{stt}/hcg_{stt}')
    #so luong hcg
    hcgLen = len(os.listdir(folder))
    HCG = open (r'C:\Users\Admin\Downloads\after that\hcgAlbum.txt','r').readlines()
    HCG.append(f"    #hcg album {stt}\n")
    string= f"    album_hcg_{stt} = ["
    for i in range(1,hcgLen+1):
        string+= f"'hcg_hcg_{stt}{i}'"
        if i!=hcgLen:
            string+=','
    string +=']\n'
    HCG.append(string)
    hcgWrite = open(r'C:\Users\Admin\Downloads\after that\hcgAlbum.txt','w')
    for x in HCG:
        hcgWrite.write(x)
    print(f"{stt} đã thêm khai báo hcg")

def printlabel(stt,file,ani=False):
    char =''
    mp3 =1
    flash = False
    anicheck = False
    A=[]
    if ani == False:
        A.append(f"label hscene_{stt}:\n")
    else:
        A.append(f"label hscene_{stt}a:\n    $_game_menu_screen = None\n")
        len = lenani(stt)
        for i in range(1,len+1):
            A.append(f"    define  ani{stt}{i} = Movie(play = 'images/ani/ani_{stt}/Ani {i}.webm',size = (1280,720),loop = True)\n")

    A.append(f"    scene black\n"
             f"    $ quick_menu = True\n"
             f"    play music 'audio/ost/bgm005.mp3' fadeout 1.0 fadein 1.0\n")

    for line in file:
        # character, voice

        if 'voice' in line:
            if char=='':
                char = f'    char{line[41:45]}'
            A.append(f"    voice 'audio/hvoice/hvoice_{stt}/hvoice_{mp3}.mp3'\n")
            if anicheck:
                A[-1],A[-2] =A[-2],A[-1]
            mp3+=1
            A.append(char)
        # thoai
        if 'black' in line and 'msg' in line:
            A[-1]+=(f"    '{line[35:-12]}'\n")
            if anicheck:
                A[-1],A[-2]=A[-2],A[-1]
                anicheck= False
        #scene (jpg)
        if 'flash' in line:
            flash = True
        if 'jpg' in line:
            if flash:
                A.append(f'    scene hcg_hcg_{stt}{int(line.split('.jpg')[0][-2:])} with flash\n')
                flash = False
            else:
                A.append(f'    scene hcg_hcg_{stt}{int(line.split('.jpg')[0][-2:])} with Dissolve(0.5)\n')
        #background color
        if 'bg,color' in line :
            A.append('    scene black with Dissolve(1.0)\n')
        #ani

        if '.mp4' in line:
            #flash
            if ':' in line:
                line = line.split('.mp4')
                A.append(f'    show expression Zoomable(ani{stt}{int(line[0][-2:])}) as cg\n')

                A.append(f'    show expression Zoomable(ani{stt}{int(line[1][-2:])}) as cg\n')

                anicheck = True

            else:
                A.append(f'    show expression Zoomable(ani{stt}{int(line.split(".mp4")[0][-2:])}) as cg\n')
    A.append("    $ quick_menu = False\n")
    A.append("    stop music\n")
    A.append("    scene black with Fade(0.5, 0.0, 0.5, color = '#000')\n    pause 1.0\n    jump showRoom\n")


    if os.path.exists(rf'C:\Users\Admin\Downloads\after that\renpy script\hscene_{stt}.rpy'):
        filef = open(rf'C:\Users\Admin\Downloads\after that\renpy script\hscene_{stt}.rpy','r',encoding="utf-8").readlines()
        fileWrite = open(rf'C:\Users\Admin\Downloads\after that\renpy script\hscene_{stt}.rpy', 'w',encoding="utf-8")
    else:
        fileWrite = open(rf'C:\Users\Admin\Downloads\after that\renpy script\hscene_{stt}.rpy', 'w',encoding="utf-8")
        filef = open(rf'C:\Users\Admin\Downloads\after that\renpy script\hscene_{stt}.rpy', 'r',encoding="utf-8").readlines()

    for x in A:
        filef.append(x)

    for x in filef:
        fileWrite.write(x)
    print(f"{stt} Lưu lại label")

if __name__ == '__main__':
    for i in range(1,int(open(r"C:\Users\Admin\Downloads\stt.txt").read())):
        if os.path.exists(fr'C:\Users\Admin\Downloads\d1 resource downloaded\{i}\{i}.txt'):
            read = open(fr'C:\Users\Admin\Downloads\d1 resource downloaded\{i}\{i}.txt','r',encoding='utf-8').readlines()
            printlabel(i,read,ani=False)
            lenHCG(i)
        if os.path.exists(fr'C:\Users\Admin\Downloads\d1 resource downloaded\{i}\{i}a.txt'):
            read = open(fr'C:\Users\Admin\Downloads\d1 resource downloaded\{i}\{i}a.txt','r',encoding='utf-8').readlines()
            printlabel(i, read, ani=True)

