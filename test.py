# from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget
# from PyQt5.QtSql import QSqlDatabase, QSqlTableModel , QSqlQuery

# app = QApplication([])

# # Connect to the database
# db = QSqlDatabase.addDatabase('QSQLITE')
# db.setDatabaseName('Data\database.db')
# db.open()

# # Create a table view
# table_view = QTableView()



# # SELECT Live_Data.agent_id , Live_Data.number , Live_Data.project_id , Live_Data.source_id , Live_Data.timestamp ,Sources.source_name
# # FROM Live_Data 
# # JOIN Sources
# # WHERE Live_Data.timestamp = 0 

# # Create a model and set it on the table view
# model = QSqlTableModel()
# model.setQuery(QSqlQuery(
# """
# SELECT Live_Data.agent_id , Live_Data.number , Live_Data.project_id , Live_Data.source_id , Live_Data.timestamp ,Sources.source_name
# FROM Live_Data 
# JOIN Sources , 
# WHERE Live_Data.timestamp = 0 
# """
# ))

# model.select()

# table_view.setModel(model)

# # Enable update, delete, and save operations
# def update_record():
#     # print(model.data())
#     print(model.submitAll())

# def delete_record():
#     model.removeRow(table_view.currentIndex().row())
#     print(model.submitAll())

# def save_record():
#     row = model.rowCount()
#     model.insertRow(row)
#     print(model.submitAll())

# # Create buttons for update, delete, and save operations
# update_button = QPushButton('Update')
# update_button.clicked.connect(update_record)

# delete_button = QPushButton('Delete')
# delete_button.clicked.connect(delete_record)

# save_button = QPushButton('Save')
# save_button.clicked.connect(save_record)

# # Create a layout and add the table view and buttons to it
# layout = QVBoxLayout()
# layout.addWidget(table_view)
# layout.addWidget(update_button)
# layout.addWidget(delete_button)
# layout.addWidget(save_button)

# # Create a main window and set the layout
# window = QMainWindow()
# central_widget = QWidget()
# central_widget.setLayout(layout)
# window.setCentralWidget(central_widget)
# window.show()

# # Run the application
# app.exec_()

# # Close the database connection
# db.close()


import sys
from PyQt5 import QtGui, QtCore , QtWidgets

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        
        self.home()

    def home(self):
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractAction = QtWidgets.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        checkBox = QtWidgets.QCheckBox('Shrink Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtWidgets.QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice = QtWidgets.QLabel("Windows Vista", self)



        comboBox = QtWidgets.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.move(50, 250)
        
        model = comboBox.model()
        for row in range(10):
            item = QtGui.QStandardItem(str(row))
        
            item.setForeground(QtGui.QColor('red'))
            font = item.font()
            font.setPointSize(10)
            item.setFont(font)
            model.appendRow(item)

        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)

        self.show()


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        
        

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
        

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        

    
def run():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('windowsvista'))
    GUI = Window()
    sys.exit(app.exec_())


run()
