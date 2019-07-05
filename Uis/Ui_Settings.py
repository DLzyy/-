# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\VS-CODE\python\抽号QT版\Uis\Settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("SettingsDialog")
        Dialog.resize(366, 176)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.hlLebel = QtWidgets.QLabel(Dialog)
        self.hlLebel.setObjectName("hlLebel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hlLebel)
        self.hlLineEdit = QtWidgets.QLineEdit(Dialog)
        self.hlLineEdit.setObjectName("hlLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hlLineEdit)
        self.gtLabel = QtWidgets.QLabel(Dialog)
        self.gtLabel.setObjectName("gtLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gtLabel)
        self.gtLineEdit = QtWidgets.QLineEdit(Dialog)
        self.gtLineEdit.setObjectName("gtLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gtLineEdit)
        self.dsLabel = QtWidgets.QLabel(Dialog)
        self.dsLabel.setObjectName("dsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dsLabel)
        self.Widget = QtWidgets.QWidget(Dialog)
        self.Widget.setObjectName("Widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Widget)
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_Draw = QtWidgets.QRadioButton(self.Widget)
        self.radioButton_Draw.setObjectName("radioButton_Draw")
        self.horizontalLayout_2.addWidget(self.radioButton_Draw)
        self.radioButton_Turn = QtWidgets.QRadioButton(self.Widget)
        self.radioButton_Turn.setObjectName("radioButton_Turn")
        self.horizontalLayout_2.addWidget(self.radioButton_Turn)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Widget)
        self.verticalLayout.addLayout(self.formLayout)
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
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.hlLebel.setText(_translate("Dialog", "历史记录长度"))
        self.gtLabel.setText(_translate("Dialog", "问候语"))
        self.dsLabel.setText(_translate("Dialog", "模式"))
        self.radioButton_Draw.setText(_translate("Dialog", "抽取"))
        self.radioButton_Turn.setText(_translate("Dialog", "轮转"))
        self.OkButton.setText(_translate("Dialog", "完成"))
        self.CancelButton.setText(_translate("Dialog", "取消"))

