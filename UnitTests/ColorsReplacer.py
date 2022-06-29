import os
import ColorsConst

packsPath = os.path.dirname(os.path.realpath(__file__))

def CollectFilePathList():

    filePathList = []

    for root, dirs, files in os.walk(packsPath):
        for file in files:
            filePathList.append(os.path.join(root,file))

    return filePathList

def ColorsReplacerSwitcher( filePath, colorEnabled ):

    print("Track FilePath Found:", filePath)

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
        colorBuffer = ColorsConst.NORMAL_CYAN
        if isDVPL == True:
            colorBuffer = ColorsConst.PACKED_YELLOW

    print("Overwriting To Filled Color:", filePath)

    colorReplacer = open(filePath, "wb")
    colorReplacer.write(colorBuffer)
    colorReplacer.close()

def ColorsReplacer( colorEnabled ):

    print("Replacing Color is:", colorEnabled)

    filePathList = CollectFilePathList()

    for filePath in filePathList:
        if "track.dx11" in filePath:
            ColorsReplacerSwitcher(filePath, colorEnabled)

ColorsReplacer("CYAN")
