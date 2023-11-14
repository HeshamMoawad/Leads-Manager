from PyQt5 import QtCore, QtGui, QtWidgets
from qmodels import MyMessageBox
from QSqlModels.orm import session , Agent , Source , Project ,RowOfData
from QSqlModels.models import TableModelView , ListModel
from QSqlModels.orm.reader import ReadExcelIntoDBModel 


QSS = open("assets\qss\popup.qss").read()


class AddPopupAgents(QtWidgets.QWidget):
    def __init__(self,title:str="Agents Adder", parent:QtWidgets.QWidget=None , ext:bool=False):
        super().__init__()
        self.setObjectName("AddPopup")
        self.resize(340, 170)
        self.setWindowTitle(title)
        self.setStyleSheet(QSS)
        self.ext = ext
        self.msg = MyMessageBox(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel, 0, QtCore.Qt.AlignHCenter)
        self.nameLabel.setText("Name : ")
        self.nameedit = QtWidgets.QLineEdit(self.frame)
        self.nameedit.setObjectName("nameedit")
        self.horizontalLayout.addWidget(self.nameedit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addWidget(self.frame)
        if ext :
            self.frame_3 = QtWidgets.QFrame(self)
            self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.extensionLabel = QtWidgets.QLabel(self.frame_3)
            self.extensionLabel.setObjectName("extensionLabel")
            self.extensionLabel.setText("Extention : ")
            self.horizontalLayout_2.addWidget(self.extensionLabel, 0, QtCore.Qt.AlignHCenter)
            self.extensionedit = QtWidgets.QLineEdit(self.frame_3)
            self.extensionedit.setObjectName("extensionedit")
            self.horizontalLayout_2.addWidget(self.extensionedit)
            self.horizontalLayout_2.setStretch(0, 1)
            self.horizontalLayout_2.setStretch(1, 2)
            self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okBtn = QtWidgets.QToolButton(self.frame_2)
        self.okBtn.setObjectName("okBtn")
        self.okBtn.setIcon(QtGui.QIcon("assets\icons\ok.png"))
        self.okBtn.setFixedSize(50,50)
        self.okBtn.setIconSize(QtCore.QSize(30,30))
        self.horizontalLayout_3.addWidget(self.okBtn)
        self.cancelBtn = QtWidgets.QToolButton(self.frame_2)
        self.cancelBtn.setObjectName("cancelBtn")
        self.cancelBtn.setIcon(QtGui.QIcon("assets\icons\cancel.png"))
        self.cancelBtn.setFixedSize(50,50)
        self.cancelBtn.setIconSize(QtCore.QSize(30,30))
        self.cancelBtn.clicked.connect(self.close)
        self.horizontalLayout_3.addWidget(self.cancelBtn)
        self.verticalLayout.addWidget(self.frame_2)
        self.okBtn.clicked.connect(self.ok)

    def ok (self):
        name = self.nameedit.text()
        if self.validate(name):
            if self.add(Agent(name=name)):
                self.msg.showInfo(f"Successfully added Agent : {name}")
            else:
                self.msg.showCritical("There are error !!!")
        else :
            self.msg.showWarning("Please enter name with length more than or equal 3 letters ","Not Valid")

    def validate(self,text:str)->bool:
        return len(text) >= 3 

    def add(self,model): 
        try :
            session.add(model)
            session.commit()
            return True
        except Exception as e : 
            print(e)
            return False

class AddPopupSources(AddPopupAgents): 
    def __init__(self, title: str = "Source Adder", parent: QtWidgets.QWidget = None, ext: bool = False):
        super().__init__(title, parent, ext)
    def ok (self):
        name = self.nameedit.text()
        if self.validate(name):
            if self.add(Source(name=name)):
                self.msg.showInfo(f"Successfully added Source : {name}")
            else:
                self.msg.showCritical("There are error !!!")
        else :
            self.msg.showWarning("Please enter name with length more than or equal 3 letters ","Not Valid")

class AddPopupProjects(AddPopupAgents):
    def __init__(self, title: str = "Projects Adder", parent: QtWidgets.QWidget = None, ext: bool = True):
        super().__init__(title, parent, ext)
    def ok (self):
        name = self.nameedit.text()
        extension = self.extensionedit.text()
        info = {}
        info.update({"name":name})
        if self.validate(name):
            if self.extensionedit.text() : info.update({"extension":extension})
            if self.add(Project(**info)):
                self.msg.showInfo(f"Successfully added Project : {name}")
            else:
                self.msg.showCritical("There are error !!!")
        else :
            self.msg.showWarning("Please enter name with length more than or equal 3 letters ","Not Valid")

class ViewDBTable(QtWidgets.QTableView):

    def __init__(self,table:str=None) -> None:
        super().__init__()
        if table : self.setTable(table)
        self.setStyleSheet(QSS)

        

    def setTable(self,table:str):
        self.table = table
        self.mymodel = TableModelView(table)
        self.mymodel.setEditStrategy(self.mymodel.EditStrategy.OnManualSubmit)

        self.setModel(self.mymodel)
        self.setWindowTitle(f"DB Viewer : {table}")
        self.show()
    
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.mymodel.submitAll()
        return super().closeEvent(a0)


class AddPopupData(QtWidgets.QWidget):
    def __init__(self,parent:QtWidgets.QWidget=None):
        super().__init__(parent)
        self.setObjectName("AddDataPopup")
        self.resize(355, 174)
        self.setStyleSheet(QSS)
        self.msg = MyMessageBox(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
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
        self.loadBtn.setIcon(QtGui.QIcon("assets\\icons\\uploadfile.png"))

        self.loadBtn.setFixedSize(50,50)
        self.loadBtn.setIconSize(QtCore.QSize(30,30))

        self.horizontalLayout.addWidget(self.loadBtn)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sourceLabel = QtWidgets.QLabel(self.frame_2)
        self.sourceLabel.setObjectName("sourceLabel")
        self.sourceLabel.setText("Source : ")
        self.horizontalLayout_2.addWidget(self.sourceLabel,alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addBtn = QtWidgets.QToolButton(self.frame_3)
        self.addBtn.setObjectName("addBtn")
        self.addBtn.setIcon(QtGui.QIcon("assets\icons\ok.png"))
        self.addBtn.setFixedSize(50,50)
        self.addBtn.setIconSize(QtCore.QSize(30,30))
        self.horizontalLayout_3.addWidget(self.addBtn)
        self.cancelBtn = QtWidgets.QToolButton(self.frame_3)
        self.cancelBtn.setObjectName("cancelBtn")
        self.cancelBtn.setIcon(QtGui.QIcon("assets\icons\cancel.png"))
        self.cancelBtn.setFixedSize(50,50)
        self.cancelBtn.setIconSize(QtCore.QSize(30,30))
        self.cancelBtn.clicked.connect(self.close)
        self.horizontalLayout_3.addWidget(self.cancelBtn)
        self.verticalLayout.addWidget(self.frame_3)
        self.loadBtn.clicked.connect(self.getPath)
        self.sourcesmodel = ListModel(Source)
        self.comboBox.setModel(self.sourcesmodel)
        self.addBtn.clicked.connect(self.submit)
        
    def setPrepared (self,prepared:bool):
        self.prepared = prepared

    def getPath(self):
        file_filter = 'Data File (*.xlsx );; Excel File (*.xlsx)'
        directory = QtWidgets.QFileDialog.getOpenFileName(
            caption = 'Select a Data file',
            filter = file_filter,
        )[0]
        print(directory)
        if len(directory) > 1 :
            self.prepared = False
            self.reader = ReadExcelIntoDBModel(directory)
            self.reader.start(self.reader.Priority.InheritPriority)
            self.reader.success.connect(lambda : self.excelLabel.setText(directory.split("/")[-1]))
            self.reader.success.connect(lambda : self.countLabel.setText(f"Count : {len(self.reader.data)}"))
            self.reader.Faild.connect(lambda : self.excelLabel.setText("Can't load sheet") )
            self.reader.success.connect(lambda : self.setPrepared(True))

    def submit(self):
        if self.prepared : 
            try :
                sequence = self.reader.apply(
                        RowOfData,
                        self.reader.session.query(Source).filter(Source.name == self.comboBox.currentText()).all()[0].id
                        )
                if sequence :
                    print("Will adding")
                    self.reader.session.add_all(sequence)
                    print("Will submit")
                    self.reader.session.commit()
                    print("Will success")
                    self.msg.showInfo("Success add to database")
                    self.close()
                else :
                    self.msg.showCritical("no new numbers")
            except IndexError :
                self.msg.showWarning("please choose source !!")
            except Exception as e :
                print(f"----{e}----")
        else :
            self.excelLabel.setText("Can't add to Database please restart app !")

    def refresh(self):
        self.excelLabel.setText("")
        self.countLabel.setText("")
        try :
            self.__delattr__("reader")
        except : ...
        self.sourcesmodel.refresh()

    def show(self) -> None:
        self.refresh()
        return super().show()

