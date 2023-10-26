from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel , QSqlQuery
app = QApplication([])

# Connect to the database
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('Data\database.db')
db.open()

# Create a table view
table_view = QTableView()



# SELECT Live_Data.agent_id , Live_Data.number , Live_Data.project_id , Live_Data.source_id , Live_Data.timestamp ,Sources.source_name
# FROM Live_Data 
# JOIN Sources
# WHERE Live_Data.timestamp = 0 

# Create a model and set it on the table view
model = QSqlTableModel()
model.setQuery(QSqlQuery("""
SELECT Live_Data.agent_id , Live_Data.number , Live_Data.project_id , Live_Data.source_id , Live_Data.timestamp ,Sources.source_name
FROM Live_Data 
JOIN Sources , 
WHERE Live_Data.timestamp = 0 

"""))

model.select()

table_view.setModel(model)

# Enable update, delete, and save operations
def update_record():
    # print(model.data())
    print(model.submitAll())

def delete_record():
    model.removeRow(table_view.currentIndex().row())
    print(model.submitAll())

def save_record():
    row = model.rowCount()
    model.insertRow(row)
    print(model.submitAll())

# Create buttons for update, delete, and save operations
update_button = QPushButton('Update')
update_button.clicked.connect(update_record)

delete_button = QPushButton('Delete')
delete_button.clicked.connect(delete_record)

save_button = QPushButton('Save')
save_button.clicked.connect(save_record)

# Create a layout and add the table view and buttons to it
layout = QVBoxLayout()
layout.addWidget(table_view)
layout.addWidget(update_button)
layout.addWidget(delete_button)
layout.addWidget(save_button)

# Create a main window and set the layout
window = QMainWindow()
central_widget = QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)
window.show()

# Run the application
app.exec_()

# Close the database connection
db.close()


