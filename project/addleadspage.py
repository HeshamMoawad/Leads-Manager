# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addleads.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qmodels import SearchBar ,QueryTableModel
from QSqlModels.models import ListModel , Agent ,Project , Lead




class AddLeadsPage(QtWidgets.QWidget):
    def __init__(self,parent:QtWidgets.QWidget=None):
        super().__init__(parent)
        self.setObjectName("AddLeadsPage")
        self.resize(783, 607)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchbar = SearchBar(self.frame)
        self.searchbar.setEndAnimate(QtCore.QSize(185,30))
        self.searchbar.toolButton.setIcon(QtGui.QIcon("assets\icons\search.png"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.searchbar.setSizePolicy(sizePolicy)
        self.searchbar.setObjectName("searchbar")
        self.horizontalLayout_3.addWidget(self.searchbar)
        self.agentbox = QtWidgets.QComboBox(self.frame)        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.agentbox.setSizePolicy(sizePolicy)
        self.agentbox.setObjectName("agentbox")
        self.horizontalLayout_3.addWidget(self.agentbox)
        self.projectbox = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.projectbox.setSizePolicy(sizePolicy)
        self.projectbox.setObjectName("projectbox")
        self.horizontalLayout_3.addWidget(self.projectbox)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.frame_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.counterlabel = QtWidgets.QLabel(self.frame_3)
        self.counterlabel.setObjectName("counterlabel")
        self.counterlabel.setText("Count : ")
        self.horizontalLayout.addWidget(self.counterlabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.exportBtn = QtWidgets.QToolButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.exportBtn.setSizePolicy(sizePolicy)
        self.exportBtn.setObjectName("exportBtn")
        self.exportBtn.setIcon(QtGui.QIcon("assets\icons\export.png"))
        self.exportBtn.setFixedSize(50,50)
        self.exportBtn.setIconSize(QtCore.QSize(30,30))
        self.horizontalLayout.addWidget(self.exportBtn)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(241, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.addButton = QtWidgets.QToolButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setObjectName("addButton")
        self.addButton.setIcon(QtGui.QIcon("assets\icons\\add.png"))
        self.addButton.setIconSize(QtCore.QSize(50,50))
        self.horizontalLayout_2.addWidget(self.addButton)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setPointSize(10)
        font.setFamily("Narkisim")
        self.signeture = QtWidgets.QLabel(self.frame_4)
        self.signeture.setText("MarCode")
        self.signeture.setFont(font)
        self.signeture.setObjectName("signeture")
        self.horizontalLayout_2.addWidget(self.signeture, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(2, 1)

        self.agentbox.setFixedHeight(40)
        self.projectbox.setFixedHeight(40)
        
        self.listmodelagent = ListModel(Agent)
        self.agentbox.setModel(self.listmodelagent)

        self.listmodelproject = ListModel(Project)
        self.projectbox.setModel(self.listmodelproject)

        self.querymodel = QueryTableModel()
        self.tableView.setModel(self.querymodel)
        self.querymodel.lengthChanged.connect(lambda x: self.counterlabel.setText(f"Count : {x}"))
        self.searchbar.lineEdit.textChanged.connect(self.setQuery)
        self.agentbox.currentTextChanged.connect(self.setQuery)
        self.projectbox.currentTextChanged.connect(self.setQuery)
        self.query = ""
        self.refeshShortcut = QtWidgets.QShortcut('Ctrl+R',self)
        self.refeshShortcut.activated.connect(self.refresh)
        self.refresh()

    def setQuery(self):
        self.query = f"""
        SELECT live_data.number AS number , sources.name AS source , agents.name AS agent ,projects.name AS project FROM live_data
        JOIN sources ON sources.id = live_data.source_id
        JOIN agents ON agents.id = live_data.agent_id
        JOIN projects ON projects.id = live_data.project_id
        WHERE number LIKE '%{self.searchbar.lineEdit.text()}%'
        """
        if self.projectbox.currentText():
            self.query += f"AND project = \'{self.projectbox.currentText()}\'"
        if self.agentbox.currentText():
            self.query += f"AND agent = \'{self.agentbox.currentText()}\'"
        self.querymodel.setQuery(self.query)

    # def addLead(self):
    #     lead = Lead(
    #         number = self.searchbar.lineEdit.text(),
    #         live_data_id = 1
    #     )

    def refresh(self):
        self.listmodelagent.refresh()
        self.listmodelproject.refresh()
        self.querymodel.clear()
        self.searchbar.lineEdit.clear()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AddLeadsPage()
    ui.show()
    sys.exit(app.exec_())
