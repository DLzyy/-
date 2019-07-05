# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\VS-CODE\python\抽号QT版\Uis\LotPool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LotPool(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("LotPoolDialog")
        Dialog.resize(630, 493)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/列表.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LotPoolDialog = QtWidgets.QTextEdit(Dialog)
        self.LotPoolDialog.setObjectName("LotPool")
        self.verticalLayout.addWidget(self.LotPoolDialog)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(1, -1, 1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OkButton = QtWidgets.QPushButton(Dialog)
        self.OkButton.setObjectName("OkButton")
        self.horizontalLayout.addWidget(self.OkButton)
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "签池"))
        self.OkButton.setText(_translate("Dialog", "完成"))
        self.CancelButton.setText(_translate("Dialog", "取消"))

import apprcc_rc
