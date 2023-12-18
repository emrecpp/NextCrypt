# Copyright github@emrecpp
# Emre Demircan
import sys, os, json
input_files = []

DIR_TOP = os.getcwd()
exclude_dir = ["__pycache__", "unused_Icons"]
def getListOfFiles(dirName, DISLANAN_KLASOR=None):
    if DISLANAN_KLASOR != None and DISLANAN_KLASOR == dirName:
        return None
    if not os.path.exists(dirName): return []
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            x = getListOfFiles(fullPath, DISLANAN_KLASOR)
            if x != None:
                allFiles += x

        else:
            allFiles.append(fullPath)

    return allFiles

files = getListOfFiles(DIR_TOP, exclude_dir)  
TOTAL = """<RCC>
  <qresource prefix="img">"""
for file in files: 
    if file.endswith(".py") or file.endswith(".qrc") or file.endswith(".pyc"):
        continue
    calced = str(file).replace(DIR_TOP+"\\", "").replace("\\", "/")
    TOTAL += f"\t<file>{calced}</file>" + "\n"
    
    
TOTAL += """
</qresource>
</RCC>"""

#print(TOTAL)
if True:
    with open("images.qrc", "w") as f:
        f.write(TOTAL)
    print("qrc successfully created!")