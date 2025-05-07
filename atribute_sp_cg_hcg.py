import os
src = r"C:\Users\Admin\Downloads\d1 resource"
def printAtribute(type,stt: int):
    "sp or cg or hcg"
    for i in range(1,stt):
        if type == "cg":
            file = os.path.join(src,f"cg_cg_{i}.png")
            if os.path.exists(file):
                print (f"        attribute {i}")
        elif type == "sp":
            file = os.path.join(src,f"sp_sp_{i}.png")
            if os.path.exists(file):
                print (f"        attribute {i}")
        elif type=="hcg":
            if os.path.exists(fr"C:\Users\Admin\Downloads\d1 resource downloaded\{i}"):
                print (f"        attribute {i}1")
if __name__=="__main__":
    printAtribute("hcg",1000)

