from PyQt5.QtWidgets import (
    QStyle,
    QCalendarWidget ,
    QLineEdit,
    QMainWindow , 
    QApplication ,
    QMessageBox , 
    QWidget 
    )
from PyQt5.QtCore import (
    QCalendar,
    QModelIndex,
    QRect,
    pyqtProperty,
    Qt,
    QEvent,
    pyqtSignal,
    QSize ,
    QModelIndex
    )
from PyQt5.QtGui import QIcon
import typing , sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt , QStringListModel
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QCompleter
from PyQt5.QtSql import QSqlDatabase , QSqlQuery  , QSqlTableModel




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


class Calendar(QWidget):
    Clicked = pyqtSignal()
    def __init__(self, parent: typing.Optional['QWidget'] = None) -> None:
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(500, 500, 274, 230))
        self.setObjectName("Calendar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.Clicked.emit)
        self.pushButton.clicked.connect(self.close)
        self.value = self.calendarWidget.selectedDate()
        self.calendarWidget.setHorizontalHeaderFormat(self.calendarWidget.HorizontalHeaderFormat.SingleLetterDayNames)
        self.calendarWidget.setVerticalHeaderFormat(self.calendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setFirstDayOfWeek(Qt.DayOfWeek.Saturday)
        self.calendarWidget.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
        # self.calendarWidget

    def close(self) -> bool:
        self.value = self.calendarWidget.selectedDate()
        return super().close()


class SQLSyntaxHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.rules = [
            (r'\bSELECT\b', Qt.GlobalColor.darkRed),
            (r'\bFROM\b', Qt.darkRed),
            (r'\bWHERE\b', Qt.darkRed),
            (r'\bJOIN\b', Qt.darkRed),
            (r'\bLEFT\b', Qt.darkRed),
            (r'\bRIGHT\b', Qt.darkRed),
            (r'\bINNER\b', Qt.darkRed),
            (r'\bON\b', Qt.darkRed),
            (r'\bAND\b', Qt.darkRed),
            (r'\bOR\b', Qt.darkRed),
            (r'\bNOT\b', Qt.darkRed),
            (r'\bORDER BY\b', Qt.darkRed),
            (r'\bGROUP BY\b', Qt.darkRed),
            (r'\bLIMIT\b', Qt.darkRed),
            (r'\bOFFSET\b', Qt.darkRed),
            (r'\bAS\b', Qt.darkRed),
        ]

    def highlightBlock(self, text):
        for pattern, color in self.rules:
            self.highlight(pattern, text, color)

    def highlight(self, pattern, text, color):
        import re
        for match in re.finditer(pattern, text):
            start, end = match.span()
            self.setFormat(start, end - start, color)



class SQLCodeEditor(QTextEdit):
    def __init__(self,parent:QWidget=None):
        super().__init__(parent)
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setModel(self.createCompleterModel())
        self.highlighter = SQLSyntaxHighlighter(self.document())
        self.completer.setWrapAround(False)
        self.completer.setWidget(self)
        self.completer.activated.connect(self.insertCompletion)
        self.completer.activated.connect(self.completer.popup().hide)

    def insertCompletion(self, completion):
        if self.completer.widget() != self:
            return
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.StartOfWord, QTextCursor.KeepAnchor)
        cursor.insertText(completion)
        self.setTextCursor(cursor)

    def textUnderCursor(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.WordUnderCursor)
        return cursor.selectedText()

    def createCompleterModel(self):
        model = QStringListModel()
        model.setStringList(self.completionList())
        return model

    def completionList(self):
        return ["SELECT", "FROM", "WHERE", "JOIN", "LEFT", "RIGHT", "INNER", "ON", "AND", "OR", "NOT", "ORDER BY", "GROUP BY"]

    def focusInEvent(self, e):
        self.completer.setWidget(self)
        super(SQLCodeEditor, self).focusInEvent(e)

    def keyPressEvent(self, event):
        if self.completer.popup().isVisible():
            if event.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab):
                event.ignore()
                return
        super(SQLCodeEditor, self).keyPressEvent(event)
        if event.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Tab, Qt.Key_Space):
            cursor = self.textCursor()
            cursor.select(QTextCursor.WordUnderCursor)
            extra = cursor.selectedText()
            popup = self.completer.popup()
            popup.setCurrentIndex(self.completer.model().index(0, 0))
            cr = self.cursorRect()
            cr.setWidth(popup.sizeHintForColumn(0)
                        + popup.verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
        else:
            cursor = self.textCursor()
            cursor.select(QTextCursor.WordUnderCursor)
            prefix = cursor.selectedText()
            if prefix != self.completer.completionPrefix():
                self.completer.setCompletionPrefix(prefix)
                self.completer.popup().setCurrentIndex(
                    self.completer.completionModel().index(0, 0))
            cr = self.cursorRect()
            cr.setWidth(self.completer.popup().sizeHintForColumn(0)
                        + self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)


class QueryTableModel(QSqlTableModel):
    lengthChanged = pyqtSignal(int)
    def __init__(self) -> None:
        super().__init__()


    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        return super().flags(index) & ~Qt.ItemFlag.ItemIsEditable

    def setQuery(self, query: str) -> None:
        response =  super().setQuery(QSqlQuery(str(query)))
        self.lengthChanged.emit(self.rowCount(QModelIndex()))
        return response

    def clear(self) -> None:
        self.lengthChanged.emit(0)
        return super().clear()