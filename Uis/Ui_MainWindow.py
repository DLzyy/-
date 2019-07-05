# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\VS-CODE\python\抽号器\Uis\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/抽号.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainButton.setGeometry(QtCore.QRect(320, 310, 150, 100))
        self.mainButton.setMinimumSize(QtCore.QSize(150, 100))
        self.mainButton.setMaximumSize(QtCore.QSize(150, 100))
        self.mainButton.setAutoFillBackground(False)
        self.mainButton.setText("")
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap(":/pic/开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainButton.setIcon(self.icon1)
        self.mainButton.setIconSize(QtCore.QSize(70, 70))
        self.mainButton.setObjectName("mainButton")
        self.outPutLabel = QtWidgets.QLabel(self.centralwidget)
        self.outPutLabel.setGeometry(QtCore.QRect(100, 120, 581, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(50)
        self.outPutLabel.setFont(font)
        self.outPutLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outPutLabel.setObjectName("outPutLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(675, 490, 121, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pic/列表.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pic/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.icon5 = QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap(":/pic/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "抽号"))
        self.outPutLabel.setText(_translate("MainWindow", "Hello World!"))

import apprcc_rc
