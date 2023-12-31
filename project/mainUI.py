# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os 
jornal_path = os.path.join("Data\database.db-journal")
if os.path.isfile(jornal_path):
    try :
        os.remove(jornal_path)
    except Exception as e:
        print(e)
        # input("Press Enter to exit : ")

from PyQt5 import QtCore, QtGui, QtWidgets
from qmodels import MyQMainWindow , MyMessageBox
from addleadspage import AddLeadsPage
from sheetspage import SheetsPage
from managedatapage import ManagerDataPage
from querypage import QueryPage
from reportpage import ReportPage
from chartspage import ChartsPage
from PyQt5.QtSql import QSqlDatabase


class MainWindow(MyQMainWindow):

    def SetupUi(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry(0)
        screen_height = int(screen.height()*0.8)
        screen_width = int(screen.width()*0.8)
        self.QSS = open('assets\qss\main.qss','r').read()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("Data\database.db")
        self.db.open()
        self.setObjectName("MainWindow")
        self.resize(screen_width+1, screen_height+1)
        self.move(int((screen.width()-screen_width)/2),int((screen.height()-screen_height)/2))
        self.setFrameLess()
        self.setBackgroundTransparent()
        self.mainWidget.setStyleSheet(self.QSS)
        self.widget = QtWidgets.QWidget(self.mainWidget)
        self.widget.setGeometry(QtCore.QRect(0, -1, screen_width, screen_height))
        self.widget.setObjectName("centralwidget")
        self.msg = MyMessageBox(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QFrame(self.widget)
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leftFrame = QtWidgets.QFrame(self.headerFrame)
        self.leftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.leftFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.logoLabel = QtWidgets.QLabel(self.leftFrame)
        self.logoLabel.setObjectName("logoLabel")
        self.gridLayout.addWidget(self.logoLabel, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.leftFrame)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.midFrame = QtWidgets.QFrame(self.headerFrame)
        self.midFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.midFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.midFrame.setObjectName("midFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.midFrame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.chartBtnPage = QtWidgets.QToolButton(self.midFrame)
        self.chartBtnPage.setObjectName("chartBtnPage")
        self.chartBtnPage.setCheckable(True)
        self.horizontalLayout_2.addWidget(self.chartBtnPage)
        self.queryBtnPage = QtWidgets.QToolButton(self.midFrame)
        self.queryBtnPage.setObjectName("queryBtnPage")
        self.queryBtnPage.setCheckable(True)
        self.horizontalLayout_2.addWidget(self.queryBtnPage)
        self.managerDataBtnPage = QtWidgets.QToolButton(self.midFrame)
        self.managerDataBtnPage.setObjectName("managerDataBtnPage")
        self.managerDataBtnPage.setCheckable(True)
        self.horizontalLayout_2.addWidget(self.managerDataBtnPage)
        self.reportBtnPage = QtWidgets.QToolButton(self.midFrame)
        self.reportBtnPage.setObjectName("reportBtnPage")
        self.reportBtnPage.setCheckable(True)
        self.horizontalLayout_2.addWidget(self.reportBtnPage)
        self.sheetsBtnPage = QtWidgets.QToolButton(self.midFrame)
        self.sheetsBtnPage.setObjectName("sheetsBtnPage")
        self.sheetsBtnPage.setCheckable(True)
        self.horizontalLayout_2.addWidget(self.sheetsBtnPage)
        self.addLeadsBtnPage = QtWidgets.QToolButton(self.midFrame)
        self.addLeadsBtnPage.setCheckable(True)
        self.addLeadsBtnPage.setObjectName("addLeadsBtnPage")
        self.horizontalLayout_2.addWidget(self.addLeadsBtnPage)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.midFrame)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.rightFrame = QtWidgets.QFrame(self.headerFrame)
        self.rightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightFrame.setObjectName("rightFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.rightFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minimizeBtn = QtWidgets.QToolButton(self.rightFrame)
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout.addWidget(self.minimizeBtn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.exitBtn = QtWidgets.QToolButton(self.rightFrame)
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout.addWidget(self.exitBtn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.rightFrame)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 5)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addWidget(self.headerFrame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout.addWidget(self.stackedWidget)
        self.group = QtWidgets.QButtonGroup(self.midFrame)
        self.group.addButton(self.addLeadsBtnPage )
        self.group.addButton(self.sheetsBtnPage )
        self.group.addButton(self.reportBtnPage )
        self.group.addButton(self.managerDataBtnPage )
        self.group.addButton(self.queryBtnPage )
        self.group.addButton(self.chartBtnPage )
        self.group.buttonClicked.connect(lambda : self.stackedWidget.setCurrentIndex((self.group.checkedId()*-1)-2))
        self.addLeadsBtnPage.setChecked(True)

        self.addleadspage = AddLeadsPage(self)
        self.stackedWidget.insertWidget(0,self.addleadspage)
        self.sheetspage = SheetsPage(self)
        self.stackedWidget.insertWidget(1,self.sheetspage)
        self.reportpage = ReportPage(self)
        self.stackedWidget.insertWidget(2,self.reportpage)
        self.managerdatapage = ManagerDataPage(self,self.QSS)
        self.stackedWidget.insertWidget(3,self.managerdatapage)
        self.querypage = QueryPage(self)
        self.stackedWidget.insertWidget(4,self.querypage)
        self.chartspage = ChartsPage(self)
        self.stackedWidget.insertWidget(5,self.chartspage)
        
        self.exitBtn.setAutoRaise(True)
        self.minimizeBtn.setAutoRaise(True)
        self.exitBtn.setIcon(QtGui.QIcon("assets\icons\\black-exit.png"))
        self.exitBtn.setIconSize(QtCore.QSize(14,14))
        self.exitBtn.setFixedSize(QtCore.QSize(24,24))
        self.minimizeBtn.setIcon(QtGui.QIcon("assets\icons\\black-minus.png"))
        self.minimizeBtn.setIconSize(QtCore.QSize(20,20))
        self.minimizeBtn.setFixedSize(QtCore.QSize(24,24))
        self.exitBtn.clicked.connect(self.close)
        self.minimizeBtn.clicked.connect(self.showMinimized)
        #####
        self.addLeadsBtnPage.setIcon(QtGui.QIcon('assets\icons\home.png'))
        self.sheetsBtnPage.setIcon(QtGui.QIcon('assets\icons\sheets.png'))
        self.reportBtnPage.setIcon(QtGui.QIcon('assets\icons\\report.png'))
        self.managerDataBtnPage.setIcon(QtGui.QIcon('assets\icons\data-manager.png'))
        self.queryBtnPage.setIcon(QtGui.QIcon('assets\icons\query.png'))
        self.chartBtnPage.setIcon(QtGui.QIcon('assets\icons\charts.png'))
        #####
        self.addLeadsBtnPage.setFixedSize(24,24)
        self.sheetsBtnPage.setFixedSize(24,24)
        self.reportBtnPage.setFixedSize(24,24)
        self.managerDataBtnPage.setFixedSize(24,24)
        self.queryBtnPage.setFixedSize(24,24)
        self.chartBtnPage.setFixedSize(24,24)


        self.stackedWidget.setCurrentIndex(0)
        super().SetupUi()


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.db.commit()
        self.db.close()
        return super().closeEvent(a0)


if __name__ == "__main__":
    ui = MainWindow()
    ui.setAppStyle('Fusion')
    ui.show()
