
def moveFolderToViewer(i):
    """
        run this last
    """
    import os
    import shutil
    path = f'/home/huy/Downloads/deep one resource/{i}/hcg_{i}'
    if os.path.exists(path):
        shutil.move(path,f'/home/huy/Downloads/DeepOneViewerRe-1.0-pc - Copy/game/images/hcg/hcg_{i}')
    path = f'/home/huy/Downloads/deep one resource/{i}/hvoice_{i}'
    if os.path.exists(path):
        shutil.move(path,f'/home/huy/Downloads/DeepOneViewerRe-1.0-pc - Copy/game/audio/hvoice/hvoice_{i}')
    path = f'/home/huy/Downloads/deep one resource/{i}/ani_{i}'
    if os.path.exists(path):
        shutil.move(path, f'/home/huy/Downloads/DeepOneViewerRe-1.0-pc - Copy/game/images/ani/ani_{i}')
for i in range(1,1000):
    moveFolderToViewer(i)