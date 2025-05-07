"""
tạm chưa có cách thu gọn chương trình này
"""

import os.path

def getroom(stt):
    file = open(fr'C:\Users\Admin\Downloads\d1 resource downloaded\{stt}\{stt}.txt','r',encoding='utf-8').readlines()
    for line in file:
        if 'voice' in line:
            return( line.split('character/')[-1][:4])
def checkani(stt):
    return os.path.exists(fr'C:\Users\Admin\Downloads\d1 resource downloaded\ani\ani_{stt}')

def imagebutton(stt):
    roomnum = getroom(stt)
    path = fr'C:\Users\Admin\Downloads\after that\room\{roomnum}imagebutton.txt'
    if os.path.exists(path):
        A=open(path,'r').readlines()
        filewrite = open(path,'w')
    else:
        filewrite = open(path, 'w')
        A = open(path, 'r').readlines()

    A.append("        imagebutton:\n")
    A.append(f"            idle 'thumb {stt} idle'\n")
    A.append(f"            hover 'thumb {stt} hover'\n")
    A.append(f"            action SetVariable('view','cg'),SetVariable('altId','{stt}'),Hide('room'),Show('room_{stt}')\n")

    for x in A:
        filewrite.write(x)
    print(f"Image button không có lỗi {stt}")
def screen(stt,view):
    roomnum = getroom(stt)
    path = fr'D:\viewer\DeepOneViewerRe-1.0-pc\DeepOneViewerRe-1.0-pc\game\script\room\room_{roomnum}.rpy'
    A=[]
    filewrite=[]
    if os.path.exists(path):
        A=open(path,'r').readlines()
        A.append('\n')
        filewrite = open(path,'w')
    else:
        emptyroom = open(r'C:\Users\Admin\Downloads\after that\emptyroom.txt','r').readlines()
        a = open(r'C:\Users\Admin\Downloads\after that\emptyroom.txt','w')
        for x in emptyroom:
            a.write(x)
        a.write(f'{roomnum}\n')
        return 
    
    A.append(f"screen room_{stt}():\n")
    A.append(f"    tag room\n    add 'img_background'\n    add 'sp {stt}'\n")
    A.append(f"    textbutton 'Alts' text_size 30 xpos 750 ypos 25 action Hide('room'),Show('room_{roomnum}')\n")
    if view!=1:
        A.append("    textbutton 'CG' text_size 30 xpos 750 ypos 75 action SetVariable('view','cg')\n")
    if view==1:
        A.append("    hbox xpos 750 ypos 125 spacing 30:\n")
        A.append("        textbutton 'Scene 1' text_size 30 action SetVariable('view','1')\n")
        A.append("    showif view == '1':\n")
        A.append(f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt}),Jump('viewAlbum')\n")
        A.append(f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt}')\n")
        A.append(f"        add 'hcg {stt}1 idle' xpos 800 ypos 275\n")
    elif view==2:
        if not checkani(stt+1):
            A.append("    hbox xpos 750 ypos 125 spacing 30:\n"
              "        textbutton 'Scene 1' text_size 30 action SetVariable('view','1')\n"
              "        textbutton 'Scene 2' text_size 30 action SetVariable('view','2')\n")
            A.append("    showif view == 'cg':\n"
              "        textbutton 'Zoom' text_size 30 xpos 950 ypos 225 action Jump('zoomCg')\n"
              f"        add 'cg {stt} idle' xpos 800 ypos 275\n")
            A.append("    elif view == '1':\n"
              f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt}),Jump('viewAlbum')\n"
              f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt}')\n"
              f"        add 'hcg {stt}1 idle' xpos 800 ypos 275\n")
            A.append("    elif view == '2':\n"
              f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt+1}),Jump('viewAlbum')\n"
              f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt+1}')\n"
              f"        add 'hcg {stt+1}1 idle' xpos 800 ypos 275\n")
        if checkani(stt+1):
            A.append("    hbox xpos 750 ypos 125 spacing 30:\n"
                  "        textbutton 'Scene 1' text_size 30 action SetVariable('view','1')\n"
                  "        textbutton 'Scene 2' text_size 30 action SetVariable('view','2')\n"
                  "    hbox xpos 750 ypos 175 spacing 30:\n"
                  "        textbutton 'Scene 2A' text_size 30 action SetVariable('view','2ani')\n")
            A.append("    showif view == 'cg':\n"
                  "        textbutton 'Zoom' text_size 30 xpos 950 ypos 225 action Jump('zoomCg')\n"
                  f"        add 'cg {stt} idle' xpos 800 ypos 275\n")
            A.append("    elif view == '1':\n"
                  f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt}),Jump('viewAlbum')\n"
                  f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt}')\n"
                  f"        add 'hcg {stt}1 idle' xpos 800 ypos 275\n")
            A.append("    elif view == '2':\n"
                  f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt + 1}),Jump('viewAlbum')\n"
                  f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt + 1}')\n"
                  f"        add 'hcg {stt + 1}1 idle' xpos 800 ypos 275\n")
            A.append("    elif view == '2ani':\n"
                  f"        textbutton 'Ani' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_ani_{stt+1}),Jump('viewAlbum')\n"
                  f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt+1}a')\n"
                  f"        add 'hcg {stt+1}1 idle' xpos 800 ypos 275\n")
    elif view==3:
        if not checkani(stt+2):
            A.append("    hbox xpos 750 ypos 125 spacing 30:\n"
              "        textbutton 'Scene 1' text_size 30 action SetVariable('view','1')\n"
              "        textbutton 'Scene 2' text_size 30 action SetVariable('view','2')\n"
              "    hbox xpos 750 ypos 175 spacing 30:\n"
              "        textbutton 'Scene 3' text_size 30 action SetVariable('view','3')\n")
            A.append("    showif view == 'cg':\n"
              "        textbutton 'Zoom' text_size 30 xpos 950 ypos 225 action Jump('zoomCg')\n"
              f"        add 'cg {stt} idle' xpos 800 ypos 275\n")
            A.append("    elif view == '1':\n"
              f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt}),Jump('viewAlbum')\n"
              f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt}')\n"
              f"        add 'hcg {stt}1 idle' xpos 800 ypos 275\n")
            A.append("    elif view == '2':\n"
              f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt + 1}),Jump('viewAlbum')\n"
              f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt + 1}')\n"
              f"        add 'hcg {stt + 1}1 idle' xpos 800 ypos 275\n")
            A.append("    elif view == '3':\n"
              f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt + 2}),Jump('viewAlbum')\n"
              f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt + 2}')\n"
              f"        add 'hcg {stt + 2}1 idle' xpos 800 ypos 275\n")
        if checkani(stt+2):
            A.append("    hbox xpos 750 ypos 125 spacing 30:\n"
                  "        textbutton 'Scene 1' text_size 30 action SetVariable('view','1')\n"
                  "        textbutton 'Scene 2' text_size 30 action SetVariable('view','2')\n"
                  "    hbox xpos 750 ypos 175 spacing 30:\n"
                  "        textbutton 'Scene 3' text_size 30 action SetVariable('view','3')\n"
                  "        textbutton 'Scene 3A' text_size 30 action SetVariable('view','3ani')\n")

            A.append("    showif view == 'cg':\n"
                  "        textbutton 'Zoom' text_size 30 xpos 950 ypos 225 action Jump('zoomCg')\n"
                  f"        add 'cg {stt} idle' xpos 800 ypos 275\n")
            A.append("    elif view == '1':\n"
                  f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt}),Jump('viewAlbum')\n"
                  f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt}')\n"
                  f"        add 'hcg {stt}1 idle' xpos 800 ypos 275\n")
            A.append("    elif view == '2':\n"
                  f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt + 1}),Jump('viewAlbum')\n"
                  f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt + 1}')\n"
                  f"        add 'hcg {stt + 1}1 idle' xpos 800 ypos 275\n")
            A.append("    elif view == '3':\n"
                  f"        textbutton 'HCG' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_hcg_{stt + 2}),Jump('viewAlbum')\n"
                  f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt + 2}')\n"
                  f"        add 'hcg {stt + 2}1 idle' xpos 800 ypos 275\n")
            A.append("    elif view == '3ani':\n"
                  f"        textbutton 'Ani' text_size 30 xpos 870 ypos 225 action Function(createTempAlbum,album_ani_{stt+2}),Jump('viewAlbum')\n"
                  f"        textbutton 'Scene' text_size 30 xpos 1040 ypos 225 action Hide('room'),Jump('hscene_{stt + 2}a')\n"
                  f"        add 'hcg {stt + 2}1 idle' xpos 800 ypos 275\n")
    A.append("    use navi_buttons\n")
    for x in A:
        filewrite.write(x)
    print(f"screen không có lỗi {stt}")

if __name__ == '__main__':
    """
        sau doi ten file
    """
    Arr=[]
    for i in range(291,int(open(r"C:\Users\Admin\Downloads\stt.txt").read())):
        des= rf'C:\Users\Admin\Downloads\d1 resource\sp_sp_{i}.png'
        if os.path.exists(des):
            Arr.append(i)
    Arr.append(291)
    for i in range(len(Arr)-1):

        imagebutton(Arr[i])
        screen(Arr[i],Arr[i+1]-Arr[i])
