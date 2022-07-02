from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

import tempfile, os
import ColorsReplacer
import AppConst

tempDirectory = tempfile.gettempdir()
tempStoragePath = tempDirectory + "\\WoTBDeTrackingMod"

dataDirectory = ""

def ReadSaveDataPath():
    global dataDirectory
    if os.path.exists("savedDataPath.txt") == True:
        streamReader = open("savedDataPath.txt", "r")
        dataDirectory = streamReader.read()
        streamReader.close()
    else:
        dataDirectory = "Enter here your WoTB/Data/3d directory"

def WriteSaveDataPath( dirToSave ):
    streamWriter = open("savedDataPath.txt", "w")
    streamWriter.write(dirToSave)
    streamWriter.close()

class Ui_WoTBDeTrackingMod(object):
    def setupUi(self, WoTBDeTrackingMod):
        WoTBDeTrackingMod.setObjectName("WoTBDeTrackingMod")
        WoTBDeTrackingMod.resize(495, 184)
        WoTBDeTrackingMod.setMinimumSize(QtCore.QSize(495, 184))
        WoTBDeTrackingMod.setMaximumSize(QtCore.QSize(495, 184))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        WoTBDeTrackingMod.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(WoTBDeTrackingMod)
        self.centralwidget.setObjectName("centralwidget")
        self.Demonstration = QtWidgets.QLabel(self.centralwidget)
        self.Demonstration.setGeometry(QtCore.QRect(-4, -8, 181, 201))
        self.Demonstration.setText("")
        self.Demonstration.setObjectName("Demonstration")
        self.SaveDataPathLine = QtWidgets.QLineEdit(self.centralwidget)
        self.SaveDataPathLine.setGeometry(QtCore.QRect(180, 120, 311, 20))
        self.SaveDataPathLine.setObjectName("SaveDataPathLine")
        self.ColorCyan = QtWidgets.QPushButton(self.centralwidget)
        self.ColorCyan.setGeometry(QtCore.QRect(180, 1, 311, 31))
        self.ColorCyan.setText("")
        self.ColorCyan.setObjectName("ColorCyan")
        self.ColorGreen = QtWidgets.QPushButton(self.centralwidget)
        self.ColorGreen.setGeometry(QtCore.QRect(180, 40, 151, 31))
        self.ColorGreen.setText("")
        self.ColorGreen.setObjectName("ColorGreen")
        self.ColorPink = QtWidgets.QPushButton(self.centralwidget)
        self.ColorPink.setGeometry(QtCore.QRect(340, 40, 151, 31))
        self.ColorPink.setText("")
        self.ColorPink.setObjectName("ColorPink")
        self.ColorRed = QtWidgets.QPushButton(self.centralwidget)
        self.ColorRed.setGeometry(QtCore.QRect(180, 80, 151, 31))
        self.ColorRed.setText("")
        self.ColorRed.setObjectName("ColorRed")
        self.ColorYellow = QtWidgets.QPushButton(self.centralwidget)
        self.ColorYellow.setGeometry(QtCore.QRect(340, 80, 151, 31))
        self.ColorYellow.setText("")
        self.ColorYellow.setObjectName("ColorYellow")
        self.SaveDataPath = QtWidgets.QPushButton(self.centralwidget)
        self.SaveDataPath.setGeometry(QtCore.QRect(180, 150, 311, 31))
        self.SaveDataPath.setText("")
        self.SaveDataPath.setObjectName("SaveDataPath")
        WoTBDeTrackingMod.setCentralWidget(self.centralwidget)

        ReadSaveDataPath()
        self.SaveDataPathLine.setText(dataDirectory)

        # Design
        demonstrationPixmap = QPixmap(tempStoragePath+"\\Demonstration.png")
        self.Demonstration.setPixmap(demonstrationPixmap)

        self.SaveDataPath.setIcon(QIcon(tempStoragePath+"\\SaveDataPath.png"))
        self.SaveDataPath.setIconSize(QtCore.QSize(311,31))

        self.ColorCyan.setIcon(QIcon(tempStoragePath+"\\ColorCyan.png"))
        self.ColorCyan.setIconSize(QtCore.QSize(311,31))

        self.ColorGreen.setIcon(QIcon(tempStoragePath+"\\ColorGreen.png"))
        self.ColorGreen.setIconSize(QtCore.QSize(151,31))
        
        self.ColorPink.setIcon(QIcon(tempStoragePath+"\\ColorPink.png"))
        self.ColorPink.setIconSize(QtCore.QSize(151,31))
        
        self.ColorYellow.setIcon(QIcon(tempStoragePath+"\\ColorYellow.png"))
        self.ColorYellow.setIconSize(QtCore.QSize(151,31))
        
        self.ColorRed.setIcon(QIcon(tempStoragePath+"\\ColorRed.png"))
        self.ColorRed.setIconSize(QtCore.QSize(151,31))

        # Buttons Actions
        def ChangeTracksToCyan():
            dataDirectory = self.SaveDataPathLine.text()
            ColorsReplacer.ColorsReplacer("CYAN", dataDirectory)

        def ChangeTracksToGreen():
            dataDirectory = self.SaveDataPathLine.text()
            ColorsReplacer.ColorsReplacer("GREEN", dataDirectory)

        def ChangeTracksToPink():
            dataDirectory = self.SaveDataPathLine.text()
            ColorsReplacer.ColorsReplacer("PINK", dataDirectory)

        def ChangeTracksToYellow():
            dataDirectory = self.SaveDataPathLine.text()
            ColorsReplacer.ColorsReplacer("YELLOW", dataDirectory)

        def ChangeTracksToRed():
            dataDirectory = self.SaveDataPathLine.text()
            ColorsReplacer.ColorsReplacer("RED", dataDirectory)
        
        self.ColorCyan.clicked.connect(ChangeTracksToCyan)
        self.ColorGreen.clicked.connect(ChangeTracksToGreen)
        self.ColorPink.clicked.connect(ChangeTracksToPink)
        self.ColorYellow.clicked.connect(ChangeTracksToYellow)
        self.ColorRed.clicked.connect(ChangeTracksToRed)

        def SaveDataPathAction():
            WriteSaveDataPath(self.SaveDataPathLine.text())

        self.SaveDataPath.clicked.connect(SaveDataPathAction)

        self.retranslateUi(WoTBDeTrackingMod)
        QtCore.QMetaObject.connectSlotsByName(WoTBDeTrackingMod)

    def retranslateUi(self, WoTBDeTrackingMod):
        _translate = QtCore.QCoreApplication.translate
        WoTBDeTrackingMod.setWindowTitle(_translate("WoTBDeTrackingMod", "WoTBDeTrackingMod"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WoTBDeTrackingMod = QtWidgets.QMainWindow()
    ui = Ui_WoTBDeTrackingMod()
    ui.setupUi(WoTBDeTrackingMod)
    WoTBDeTrackingMod.show()
    sys.exit(app.exec_())
