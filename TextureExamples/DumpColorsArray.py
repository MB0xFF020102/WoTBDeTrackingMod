normalFilenames = ["cyan.dx11.dds", "green.dx11.dds", "pink.dx11.dds", "red.dx11.dds", "yellow.dx11.dds"]
packedFilenames = ["cyan.dx11.dds.dvpl", "green.dx11.dds.dvpl", "pink.dx11.dds.dvpl", "red.dx11.dds.dvpl", "yellow.dx11.dds.dvpl"]

numberOfColorsNormal = len(normalFilenames)
numberOfColorsPacked = len(packedFilenames)

if (numberOfColorsNormal != numberOfColorsPacked):
	print("Logger::Error: (numberOfColorsNormal != numberOfColorsPacked)")
	exit()

resultFileStream = open("dumpResult.txt", "w")

def GetPathNameFromFilename( isNormal, fileName ):

	filePathResult = ""

	if (isNormal == True):
		filePathResult = "NORMAL/" + fileName

	elif (isNormal == False):
		filePathResult = "DVPL/" + fileName

	return filePathResult

def ReceiveDataFromFilePath( filePath ):

	file = open(filePath, "rb+")
	fileData = file.read()
	file.close()

	return fileData

def WriteDumpLineFromFileData( fileData ):

	bufferExtracted = list(fileData)
	bufferExtractedAsString = str(bufferExtracted)

	resultFileStream.writelines(bufferExtractedAsString + "\n")

def CreateDumpLines():

	resultFileStream.writelines("NORMAL IN ORDER:" + "\n")

	for fileNum in range (0, numberOfColorsNormal):

		fileName = normalFilenames[fileNum]
		filePath = GetPathNameFromFilename(True, fileName)
		fileData = ReceiveDataFromFilePath(filePath)

		WriteDumpLineFromFileData(fileData)

	resultFileStream.writelines("PACKED IN ORDER:" + "\n")

	for fileNum in range (0, numberOfColorsPacked):

		fileName = packedFilenames[fileNum]
		filePath = GetPathNameFromFilename(False, fileName)
		fileData = ReceiveDataFromFilePath(filePath)

		WriteDumpLineFromFileData(fileData)

	resultFileStream.close()

CreateDumpLines()