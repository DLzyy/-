# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\VS-CODE\python\抽号器\抽号QT版\Uis\SimpleWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimpleWindow(object):
    def setupUi(self, SimpleWindow):
        SimpleWindow.setObjectName("SimpleWindow")
        SimpleWindow.resize(310, 71)
        self.setWindowIcon(QtGui.QIcon(":/pic/抽号.ico"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(SimpleWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputLabel = QtWidgets.QLabel(SimpleWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.outputLabel.setFont(font)
        self.outputLabel.setText("")
        self.outputLabel.setObjectName("outputLabel")
        self.horizontalLayout.addWidget(self.outputLabel)
        self.mainButton = QtWidgets.QPushButton(SimpleWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainButton.sizePolicy().hasHeightForWidth())
        self.mainButton.setSizePolicy(sizePolicy)
        self.mainButton.setText("")
        self.startIcon = QtGui.QIcon()
        self.startIcon.addPixmap(QtGui.QPixmap(":/pic/开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainButton.setIcon(self.startIcon)
        self.mainButton.setIconSize(QtCore.QSize(35, 35))
        self.mainButton.setObjectName("mainButton")
        self.horizontalLayout.addWidget(self.mainButton)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)
        self.pauseIcon = QtGui.QIcon()
        self.pauseIcon.addPixmap(QtGui.QPixmap(":/pic/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.retranslateUi(SimpleWindow)
        QtCore.QMetaObject.connectSlotsByName(SimpleWindow)

    def retranslateUi(self, SimpleWindow):
        _translate = QtCore.QCoreApplication.translate
        SimpleWindow.setWindowTitle(_translate("SimpleWindow", "抽号"))
        self.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)

import apprcc_rc
