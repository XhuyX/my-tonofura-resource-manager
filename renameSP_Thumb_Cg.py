import os

def change (category,index):
    des= r"C:\Users\Admin\Downloads\d1 resource"
    if category =='sp':
        os.rename(des+rf"\sp_{index}.png",des+rf"\sp_sp_{index}.png")
    elif category =='thumb':
        os.rename(des+rf"\thumb_{index}.png",des+rf"\thumb_thumb_{index}.png")
    elif category =='cg':
        os.rename(des+rf"\cg_{index}.png",des+rf"\cg_cg_{index}.png")
if __name__ == '__main__':
    stt= int(open(r"C:\Users\Admin\Downloads\stt.txt",'r').read())
    for i in range(1,stt):
        if os.path.exists(fr"C:\Users\Admin\Downloads\d1 resource\cg_{i}.png"):
            change('cg',i)
        if os.path.exists(fr"C:\Users\Admin\Downloads\d1 resource\sp_{i}.png"):
            change('sp',i)
        if os.path.exists(fr"C:\Users\Admin\Downloads\d1 resource\thumb_{i}.png"):
            change('thumb',i)
