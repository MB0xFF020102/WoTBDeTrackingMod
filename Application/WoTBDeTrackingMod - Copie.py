from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

import tempfile, os
import AppConst

tempDirectory = tempfile.gettempdir()
tempStoragePath = tempDirectory + "\\WoTBDeTrackingMod"

if os.path.exists(tempStoragePath) != True:
    os.mkdir(tempStoragePath)

    # Way to Store App Images
    streamImages = open(tempStoragePath+"\\ColorCyan.png", "wb")
    streamImages.write(AppConst.ColorCyanPng)
    streamImages = open(tempStoragePath+"\\ColorGreen.png", "wb")
    streamImages.write(AppConst.ColorGreenPng)
    streamImages = open(tempStoragePath+"\\ColorPink.png", "wb")
    streamImages.write(AppConst.ColorPinkPng)
    streamImages = open(tempStoragePath+"\\ColorRed.png", "wb")
    streamImages.write(AppConst.ColorRedPng)
    streamImages = open(tempStoragePath+"\\ColorYellow.png", "wb")
    streamImages.write(AppConst.ColorYellowPng)
    streamImages = open(tempStoragePath+"\\Demonstration.png", "wb")
    streamImages.write(AppConst.DemonstrationPng)
    streamImages = open(tempStoragePath+"\\SaveDataPath.png", "wb")
    streamImages.write(AppConst.SaveDataPathPng)
    streamImages.close()
    

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
        self.SaveDataPath = QtWidgets.QLabel(self.centralwidget)
        self.SaveDataPath.setGeometry(QtCore.QRect(180, 150, 311, 31))
        self.SaveDataPath.setText("")
        self.SaveDataPath.setObjectName("SaveDataPath")
        self.SaveDataPathLine = QtWidgets.QLineEdit(self.centralwidget)
        self.SaveDataPathLine.setGeometry(QtCore.QRect(180, 120, 311, 20))
        self.SaveDataPathLine.setObjectName("SaveDataPathLine")
        self.ColorRed = QtWidgets.QLabel(self.centralwidget)
        self.ColorRed.setGeometry(QtCore.QRect(180, 80, 151, 31))
        self.ColorRed.setText("")
        self.ColorRed.setObjectName("ColorRed")
        self.ColorYellow = QtWidgets.QLabel(self.centralwidget)
        self.ColorYellow.setGeometry(QtCore.QRect(340, 80, 151, 31))
        self.ColorYellow.setText("")
        self.ColorYellow.setObjectName("ColorYellow")
        self.ColorPink = QtWidgets.QLabel(self.centralwidget)
        self.ColorPink.setGeometry(QtCore.QRect(340, 40, 151, 31))
        self.ColorPink.setText("")
        self.ColorPink.setObjectName("ColorPink")
        self.ColorGreen = QtWidgets.QLabel(self.centralwidget)
        self.ColorGreen.setGeometry(QtCore.QRect(180, 40, 151, 31))
        self.ColorGreen.setText("")
        self.ColorGreen.setObjectName("ColorGreen")
        self.ColorCyan = QtWidgets.QLabel(self.centralwidget)
        self.ColorCyan.setGeometry(QtCore.QRect(180, 0, 311, 31))
        self.ColorCyan.setText("")
        self.ColorCyan.setObjectName("ColorCyan")

        demonstrationPixmap = QPixmap(tempStoragePath+"\\Demonstration.png")
        self.Demonstration.setPixmap(demonstrationPixmap)

        saveDataPathPixmap = QPixmap(tempStoragePath+"\\SaveDataPath.png")
        self.SaveDataPath.setPixmap(saveDataPathPixmap)

        colorCyanPixmap = QPixmap(tempStoragePath+"\\ColorCyan.png")
        colorGreenPixmap = QPixmap(tempStoragePath+"\\ColorGreen.png")
        colorPinkPixmap = QPixmap(tempStoragePath+"\\ColorPink.png")
        colorYellowPixmap = QPixmap(tempStoragePath+"\\ColorYellow.png")
        colorRedPixmap = QPixmap(tempStoragePath+"\\ColorRed.png")

        self.ColorCyan.setPixmap(colorCyanPixmap)
        self.ColorGreen.setPixmap(colorGreenPixmap)
        self.ColorPink.setPixmap(colorPinkPixmap)
        self.ColorYellow.setPixmap(colorYellowPixmap)
        self.ColorRed.setPixmap(colorRedPixmap)
        
        WoTBDeTrackingMod.setCentralWidget(self.centralwidget)

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
