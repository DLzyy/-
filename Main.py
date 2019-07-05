import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
 
from Uis.Ui_MainWindow import Ui_MainWindow
from Uis.Ui_LotPool import Ui_LotPool
from Uis.Ui_Settings import Ui_Settings

from lot_pool import lotPool
from Settings import settings

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.outPutLabel.setText(settings['greeting'])
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.next)
        self.mainButton.clicked.connect(self.drawLot)
        self.pushButton_6.clicked.connect(self.editLotPool)
        self.pushButton_5.clicked.connect(self.editSettings)

    def editLotPool(self):
        lotPoolDialog = LotPoolDialog()
        lotPoolDialog.exec_()
    
    def editSettings(self):
        settingsDialog = SettingsDialog()
        settingsDialog.exec_()

    def drawLot(self):
        if settings['drawstate'] == 1:
            self.mainButton.setIcon(self.icon1)
            self.outPutLabel.setText(lotPool.drawLot())
        elif settings['drawstate'] == 2:
            if not lotPool.running:
                self.mainButton.setIcon(self.icon5)
                self.next()
                lotPool.running = True
            else:
                self.mainButton.setIcon(self.icon1)
                self.timer.stop()
                lotPool.running = False

    def next(self):
        text = lotPool.next()
        self.outPutLabel.setText(text)
        if text != '签池不能为空!':
            self.timer.start(20)
        else:
            self.mainButton.setIcon(self.icon1)
            self.timer.stop()
            lotPool.running = False


class LotPoolDialog(QtWidgets.QDialog, Ui_LotPool):
    def __init__(self):
        super(LotPoolDialog, self).__init__()
        self.setupUi(self)
        self.LotPoolDialog.setPlainText(lotPool.getLotPool())
        self.OkButton.clicked.connect(self.getLotPool)
        self.CancelButton.clicked.connect(self.reject)

    def getLotPool(self):
        text = self.LotPoolDialog.toPlainText()
        self.LotPoolDialog.clear()
        lotPool.setLotPool(text)
        self.reject()

class SettingsDialog(QtWidgets.QDialog, Ui_Settings):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.setupUi(self)
        self.hlLineEdit.setText(str(settings['historyLen'] if settings['lotcount'] > 1 else '0'))
        self.gtLineEdit.setText(str(settings['greeting']))
        if settings['drawState'] == 1:
            self.radioButton_Draw.setChecked(True)
        elif settings['drawState'] == 2:
            self.radioButton_Turn.setChecked(True)
        self.radioButton_Draw.toggled.connect(lambda: self.getState(1))
        self.radioButton_Turn.toggled.connect(lambda: self.getState(2))
        self.OkButton.clicked.connect(self.getSettings)
        self.CancelButton.clicked.connect(self.reject)

    def getSettings(self):
        try:
            hl = self.hlLineEdit.text()
            gt = self.gtLineEdit.text()
            hl = int(hl)
            if hl != 0:
                assert hl>0 and hl<settings['lotCount']
            else:
                hl = 0
            gt = str(gt)
            self.reject()
            settings['historyLen'] = hl
            settings['greeting'] = gt
            lotPool.setHistory()
            settings.Save()
        except:
            QtWidgets.QMessageBox.about(self, "警告",  "输入无效！")

    def getState(self, number):
        settings['drawState'] = number




if __name__ == '__main__':

     app = QtWidgets.QApplication(sys.argv)
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())