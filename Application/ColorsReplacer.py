import os
import ColorsConst

packsPath = os.path.dirname(os.path.realpath(__file__))

def WriteBufferToFilePath( filePath, buffer ):

    streamWriter = open(filePath, "wb")
    streamWriter.write(buffer)
    streamWriter.close()

def CollectFilePathList():

    filePathList = []

    for root, dirs, files in os.walk(packsPath):
        for file in files:
            filePathList.append(os.path.join(root,file))

    return filePathList

def ColorsReplacerSwitcher( filePath, colorEnabled ):

    if ".pvr" in filePath:
        filePathConv = filePath.replace(".pvr", ".dds")
        filePath = filePathConv
        print("PVR Converted to DDS:", filePath)

    isDVPL = False
    if ".dvpl" in filePath:
        isDVPL = True

    colorBuffer = []

    if colorEnabled == "CYAN":
        colorBuffer = ColorsConst.NORMAL_CYAN
        if isDVPL == True:
            colorBuffer = ColorsConst.PACKED_CYAN

    elif colorEnabled == "GREEN":
        colorBuffer = ColorsConst.NORMAL_GREEN
        if isDVPL == True:
            colorBuffer = ColorsConst.PACKED_GREEN

    elif colorEnabled == "PINK":
        colorBuffer = ColorsConst.NORMAL_PINK
        if isDVPL == True:
            colorBuffer = ColorsConst.PACKED_PINK

    elif colorEnabled == "RED":
        colorBuffer = ColorsConst.NORMAL_RED
        if isDVPL == True:
            colorBuffer = ColorsConst.PACKED_RED

    elif colorEnabled == "YELLOW":
        colorBuffer = ColorsConst.NORMAL_YELLOW
        if isDVPL == True:
            colorBuffer = ColorsConst.PACKED_YELLOW

    WriteBufferToFilePath(filePath, colorBuffer)

def ColorsReplacer( colorEnabled ):

    print("Tracks Color Activated:", colorEnabled)

    filePathList = CollectFilePathList()

    for filePath in filePathList:
        if "track.dx11" in filePath:
            ColorsReplacerSwitcher(filePath, colorEnabled)

