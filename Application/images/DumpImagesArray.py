import os

resultFileStream = open("imagesResult.txt", "w")
currentPath = os.path.dirname(os.path.realpath(__file__))

def CollectFileNames():

    fileNamesList = []

    for root, dirs, files in os.walk(currentPath):
        for file in files:
            if not ".py" in os.path.join(root,file): 
                fileNamesList.append(os.path.join(root,file))

    return fileNamesList

def ReceiveDataFromFilePath( filePath ):

    file = open(filePath, "rb+")
    fileData = file.read()
    file.close()

    return fileData

def WriteDumpLineFromFileData( fileData ):

    bufferExtracted = list(fileData)
    bufferExtractedAsString = str(bufferExtracted)

    resultFileStream.writelines(bufferExtractedAsString + "\n")

def CreateDumpImagesLines():

    resultFileStream.writelines("IMAGES RESULT:" + "\n")

    fileNames = CollectFileNames()
    
    for fileNum in range(0, len(fileNames)):

        resultFileStream.writelines(fileNames[fileNum] +":" + "\n")
        
        fileData = ReceiveDataFromFilePath(fileNames[fileNum])
        WriteDumpLineFromFileData(fileData)

    resultFileStream.close()

CreateDumpImagesLines()
