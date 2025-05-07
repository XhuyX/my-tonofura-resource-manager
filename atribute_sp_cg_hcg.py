"""
    hcg thì sẽ luôn xuất hiện xuyên suốt nên không cần lo về nó
    sp thì buộc phải xuất hiện 
    cg thì không phải lúc nào cũng xuất hiện
    có sp thì có thể suy ra cg
    nhưng cg thì không chắc có thể suy ra sp
"""
import os

src = r"C:\Users\Admin\Downloads\d1 resource"
dest = r"C:\Users\Admin\Downloads\d1 resource downloaded"

def printAtribute(type, stt: int):
    paths = {
        "cg": lambda i: os.path.join(src, f"cg_cg_{i}.png"),
        "sp": lambda i: os.path.join(src, f"sp_sp_{i}.png"),
        "hcg": lambda i: os.path.join(dest, str(i))
    }
    
    for i in range(1, stt):
        file_path = paths.get(type)
        if file_path and os.path.exists(file_path(i)):
            print(f"        attribute {i}" if type != "hcg" else f"        attribute {i}1")

if __name__ == "__main__":
    printAtribute("hcg", 1000)
    printAtribute("sp", 1000)
    printAtribute("cg", 1000)
