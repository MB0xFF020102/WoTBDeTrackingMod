import os
import ColorsConst

packsPath = os.path.dirname(os.path.realpath(__file__))

def CollectFilePathList():

    filePathList = []

    for root, dirs, files in os.walk(packsPath):
        for file in files:
            filePathList.append(os.path.join(root,file))

    return filePathList

def ColorsReplacer( colorEnabled ):

    filePathList = CollectFilePathList()

    for filePath in filePathList:
        if "track.dx11" in filePath:
            print(filePath)

ColorsReplacer("colorEnabled")
