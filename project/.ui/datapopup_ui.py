# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Hesham Private\Leads-Manager\project\.ui\datapopup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(355, 174)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.countLabel = QtWidgets.QLabel(self.frame)
        self.countLabel.setObjectName("countLabel")
        self.horizontalLayout.addWidget(self.countLabel, 0, QtCore.Qt.AlignLeft)
        self.excelLabel = QtWidgets.QLabel(self.frame)
        self.excelLabel.setObjectName("excelLabel")
        self.horizontalLayout.addWidget(self.excelLabel, 0, QtCore.Qt.AlignLeft)
        self.loadBtn = QtWidgets.QToolButton(self.frame)
        self.loadBtn.setObjectName("loadBtn")
        self.horizontalLayout.addWidget(self.loadBtn)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sourceLabel = QtWidgets.QLabel(self.frame_2)
        self.sourceLabel.setObjectName("sourceLabel")
        self.horizontalLayout_2.addWidget(self.sourceLabel)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addBtn = QtWidgets.QToolButton(self.frame_3)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout_3.addWidget(self.addBtn)
        self.cancelBtn = QtWidgets.QToolButton(self.frame_3)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_3.addWidget(self.cancelBtn)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.countLabel.setText(_translate("Form", "TextLabel"))
        self.excelLabel.setText(_translate("Form", "TextLabel"))
        self.loadBtn.setText(_translate("Form", "..."))
        self.sourceLabel.setText(_translate("Form", "TextLabel"))
        self.addBtn.setText(_translate("Form", "..."))
        self.cancelBtn.setText(_translate("Form", "..."))
