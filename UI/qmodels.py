from PyQt5.QtWidgets import (
    QLineEdit,
    QMainWindow , 
    QApplication ,
    QMessageBox , 
    QWidget
    )
from PyQt5.QtCore import (
    QRect,
    pyqtProperty,
    Qt,
    QEvent,
    pyqtSignal,
    QSize
    )
from PyQt5.QtGui import QIcon
import typing , sys
from PyQt5 import QtCore, QtGui, QtWidgets



class MyMessageBox(QMessageBox):
    INFO = QMessageBox.Icon.Information
    WARNING = QMessageBox.Icon.Warning
    CRITICAL = QMessageBox.Icon.Critical

    def showWarning(self,text:typing.Optional[str]="Warning",title:typing.Optional[str]="Warning"):
        self.setIcon(self.WARNING)
        self.setWindowTitle(title)
        self.setText(text)
        self.exec_()

    def showInfo(self,text:typing.Optional[str]="Info",title:typing.Optional[str]="Information"):
        self.setIcon(self.INFO)
        self.setWindowTitle(title)
        self.setText(text)
        self.exec_()

    def showCritical(self,text:typing.Optional[str]="Critical",title:typing.Optional[str]="Critical"):
        self.setIcon(self.CRITICAL)
        self.setWindowTitle(title)
        self.setText(text)
        self.exec_()        

    def showAsk(self,text:typing.Optional[str]="Critical",title:typing.Optional[str]="Ask"):
        self.setIcon(self.Icon.Question)
        self.setWindowTitle(title)
        self.setText(text)
        self.setStandardButtons(self.StandardButton.Ok | self.StandardButton.Cancel)
        return self.exec_()


## ------------ QMainWindow custom widget
class MyQMainWindow(QMainWindow):
    App = QApplication(sys.argv)
    Leaved = pyqtSignal()
    Entered = pyqtSignal()
    ShowSignal = pyqtSignal()
    MessageBox = MyMessageBox()
    msg = MyMessageBox()
    
    
    def __init__(self) -> None:
        super().__init__()
        self.App.addLibraryPath("gifs")
        self.mainWidget = QWidget(self)
        self.mainWidget.setObjectName("mainWidget")
        self.SetupUi()

    def leaveEvent(self, a0:QEvent) -> None: 
        """Method that will running if your mouse Leaved From Widget """
        self.Leaved.emit()
        return super().leaveEvent(a0)

    def enterEvent(self, a0:QEvent) -> None:
        """Method that will running if your mouse Entered Into Widget """
        self.Entered.emit()
        return super().enterEvent(a0)
    
    def setFrameLess(self):
        """to set your window without frame"""
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

    def setBackgroundTransparent(self):
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def SetupUi(self):
        """the method that will run Automaticly with calling class"""
        self.setCentralWidget(self.mainWidget)
        self.show()
        sys.exit(self.App.exec_())

    def setAppIcon(self,relativePath:str):
        """To set Icon For Your App"""
        app_icon = QIcon()
        app_icon.addFile(relativePath, QSize(16,16))
        app_icon.addFile(relativePath, QSize(24,24))
        app_icon.addFile(relativePath, QSize(32,32))
        app_icon.addFile(relativePath, QSize(48,48))
        app_icon.addFile(relativePath, QSize(256,256))
        self.App.setWindowIcon(app_icon)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() == Qt.LeftButton:
                self.move(self.mapToParent(event.pos() - self.drag_start_position))
        except : ...
        
    def setAppStyle(self,style:str):
        self.App.setStyle(style)



class AnimatedLineEdit(QLineEdit):
    def __init__(self,parent:QWidget=None):
        super().__init__(parent)
        self.__size = self.size()

    @pyqtProperty(QSize)
    def Size(self):
        return self.__size

    @Size.setter
    def Size(self,size:QSize):
        self.__size = size
        self.setFixedSize(self.__size)

    


class SearchBar(QtWidgets.QWidget):
    def __init__(self,parent:QWidget=None):
        super().__init__(parent)
        self.setObjectName("SearchBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.toolButton = QtWidgets.QToolButton(self)
        self.toolButton.setCheckable(True)
        self.toolButton.setObjectName("SearchBar_toolButton")
        self.horizontalLayout.addWidget(self.toolButton,alignment=Qt.AlignmentFlag.AlignLeft)
        self.lineEdit = AnimatedLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setObjectName("SearchBar_lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit,alignment=Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.setStretch(1, 1)
        self.animation = QtCore.QPropertyAnimation(self.lineEdit,b'Size')
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutSine)
        self.animation.setDuration(700)
        self.toolButton.clicked.connect(self.animate)
        self.animation.setStartValue(QSize(0,0))
        

    def setEndAnimate(self,size:QSize):
        self.animation.setEndValue(size)
        self.lineEdit.setFixedSize(QSize(0,0))
        self.toolButton.setFixedSize(QSize(size.height(),size.height()))

    def animate(self):
        if self.toolButton.isChecked():
            self.animation.setDirection(self.animation.Direction.Forward)
            self.animation.start()
        else :
            self.animation.setDirection(self.animation.Direction.Backward)
            self.animation.start()
