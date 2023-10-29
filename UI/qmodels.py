from PyQt5.QtWidgets import (
    QMainWindow , 
    QApplication ,
    QMessageBox , 
    QWidget
    )
from PyQt5.QtCore import (
    Qt,
    QEvent,
    pyqtSignal,
    QSize
    )
from PyQt5.QtGui import QIcon
import typing , sys



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
        self.mainWidget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

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
        if event.buttons() == Qt.LeftButton:
            self.move(self.mapToParent(event.pos() - self.drag_start_position))
