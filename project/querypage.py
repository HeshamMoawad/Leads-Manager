# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qmodels import SQLCodeEditor

class QueryPage(QtWidgets.QWidget):
    def __init__(self, parent:QtWidgets.QWidget = None ):
        super().__init__(parent)
        self.setObjectName("QueryPage")
        self.resize(783, 607)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setText("Query : ")
        self.horizontalLayout_2.addWidget(self.label)
        self.textEdit = SQLCodeEditor(self.frame)
        self.textEdit.setPlaceholderText("Enter Queries Here ... ")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.runBtn = QtWidgets.QToolButton(self.frame_4)
        self.runBtn.setIcon(QtGui.QIcon("assets\icons\\run.png"))
        self.runBtn.setFixedSize(50,50)
        self.runBtn.setIconSize(QtCore.QSize(30,30))
        self.verticalLayout_3.addWidget(self.runBtn)
        self.submit = QtWidgets.QToolButton(self.frame_4)
        self.submit.setIcon(QtGui.QIcon("assets\icons\database-save.png"))
        self.submit.setFixedSize(50,50)
        self.submit.setIconSize(QtCore.QSize(30,30))
        self.verticalLayout_3.addWidget(self.submit)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.frame_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.counterLabel = QtWidgets.QLabel(self.frame_3)
        self.counterLabel.setObjectName("counterLabel")
        self.counterLabel.setText("Count : ")
        self.horizontalLayout_3.addWidget(self.counterLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.exportBtn = QtWidgets.QToolButton(self.frame_3)
        self.exportBtn.setObjectName("exportBtn")
        self.exportBtn.setIcon(QtGui.QIcon("assets\icons\export.png"))
        self.exportBtn.setFixedSize(50,50)
        self.exportBtn.setIconSize(QtCore.QSize(30,30))
        self.horizontalLayout_3.addWidget(self.exportBtn)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.horizontalLayout.addWidget(self.widget)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = QueryPage()
    ui.show()
    sys.exit(app.exec_())
