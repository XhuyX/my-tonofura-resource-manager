import os
source = '/home/huy/Downloads/deep one resource'
def getroom(stt):
    file = open(f'/home/huy/Downloads/deep one resource/{stt}/{stt}.txt','r',encoding='utf-8').readlines()
    fileCharDefine = open('/home/huy/Downloads/DeepOneViewerRe-1.0-pc - Copy/game/script/characters.rpy','r').readlines()
    for line in file:
        if 'name,<outline width=2 color=black>' in line:
            charname= line.split('name,<outline width=2 color=black>')[-1].split("</outline>,")[0].split("<ruby>")[-1].split("</ruby>")[0].split("|")[-1]
            for x in fileCharDefine:
                if charname in x:
                    return x.split("= Character")[0][-5:]

def printlabel(stt,file):
    char =''
    mp3 =1
    flash = False
    A=[]
    A.append(f"label hscene_{stt}:\n")
    A.append(f"    scene black\n"
             f"    $ quick_menu = True\n"
             f"    play music 'audio/ost/bgm005.mp3' fadeout 1.0 fadein 1.0\n")
    for line in file:
        # character, voice
        if 'voice' in line:
            if char=='':
                char = f'    char{getroom(stt)}'
            A.append(f"    voice 'audio/hvoice/hvoice_{stt}/hvoice_{mp3}.mp3'\n")
            mp3+=1
            A.append(char)
        # thoai
        if 'black' in line and 'msg' in line:
            A[-1]+=(f"    '{line[35:-12]}'\n")
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
    A.append("    $ quick_menu = False\n")
    A.append("    stop music\n")
    A.append("    scene black with Fade(0.5, 0.0, 0.5, color = '#000')\n    pause 1.0\n    jump showRoom\n")
    fileWrite = open(f'/home/huy/Downloads/renpy script/hscene_{stt}.rpy', 'w')
    for x in A:
        fileWrite.write(x)
def lenHCG(stt):
    folder = os.path.join(source,f'{stt}/hcg_{stt}')
    #so luong hcg
    hcgLen = len(os.listdir(folder))
    HCG = open ('/home/huy/Downloads/hcgAlbum.txt','r').readlines()
    HCG.append(f"    #hcg album {stt}\n")
    string= f"    album_hcg_{stt} = ["
    for i in range(1,hcgLen+1):
        string+= f"'hcg_hcg_{stt}{i}'"
        if i!=hcgLen:
            string+=','
    string +=']\n'
    HCG.append(string)
    hcgWrite = open('/home/huy/Downloads/hcgAlbum.txt','w')
    for x in HCG:
        hcgWrite.write(x)
def imagebutton(stt):
    roomnum = getroom(stt)
    path = f'/home/huy/Downloads/room/imagebutton.txt'
    if os.path.exists(path):
        A=open(path,'r').readlines()
        filewrite = open(path,'w')
    else:
        filewrite = open(path, 'w')
        A = open(path, 'r').readlines()
    A.append("        imagebutton:\n")
    A.append(f"            idle 'icon {roomnum} idle'\n")
    A.append(f"            hover 'icon {roomnum} hover'\n")
    A.append(f"            action SetVariable('altId','{stt}'),Hide('girl_icon'),Show('room_{stt}')\n")
    for x in A:
        filewrite.write(x)
def screen(stt):
    roomnum = getroom(stt)
    roomnum= int(roomnum)
    path = f'/home/huy/Downloads/room/screen.txt'
    if os.path.exists(path):
        A=open(path,'r').readlines()
        filewrite = open(path,'w')
    else:
        filewrite = open(path, 'w')
        A = open(path, 'r').readlines()
    A.append('\n')
    A.append(f"screen room_{stt}():\n    tag room\n    add 'img_background'\n")
    A.append(f"    add 'sp {roomnum}00'\n")
    A.append(f"    textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt}),Jump('viewAlbum')\n")
    A.append(f"    textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt}')\n")
    A.append(f"    add 'hcg {stt}1 idle' xpos 800 ypos 275\n")
    A.append(f"    use navi_buttons\n")
    for x in A:
        filewrite.write(x)
if __name__ == '__main__':
    for i in range(483,513):
        if os.path.exists(f'/home/huy/Downloads/deep one resource/{i}/{i}.txt'):
            read = open(f'/home/huy/Downloads/deep one resource/{i}/{i}.txt', 'r', encoding='utf-8').readlines()
            printlabel(i,read)
            lenHCG(i)
            imagebutton(i)
            screen(i)
            #print(getroom(i))