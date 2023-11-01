from PyQt5 import QtCore, QtGui, QtWidgets
from qmodels import MyMessageBox
from QSqlModels.orm import session , Agent , Source , Project


class AddPopupAgents(QtWidgets.QWidget):
    def __init__(self,title:str="", parent:QtWidgets.QWidget=None , ext:bool=False,css:str=""):
        super().__init__()
        self.setObjectName("AddPopup")
        self.resize(340, 170)
        self.setWindowTitle(title)
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
        self.setStyleSheet(css)
        # print(css)

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
        except Exception as e : return False

class AddPopupSources(AddPopupAgents): 
    def __init__(self, title: str = "Source Adder", parent: QtWidgets.QWidget = None, ext: bool = False, css: str = ""):
        super().__init__(title, parent, ext, css)
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
    def __init__(self, title: str = "Projects Adder", parent: QtWidgets.QWidget = None, ext: bool = False, css: str = ""):
        super().__init__(title, parent, ext, css)
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
