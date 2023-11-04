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


# from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation , QSqlQuery
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

# app = QApplication([])

# # Create a connection to the database
# db = QSqlDatabase.addDatabase("QSQLITE")
# db.setDatabaseName("Data\database.db")
# db.open()

# # Create the relational table model
# model = QSqlRelationalTableModel()
# model.setTable("Live_Data")
# model.setRelation(0, QSqlRelation("Agents", "id", "agent_name")) 
# model.setRelation(2, QSqlRelation("Projects", "id", "project_name")) 
# model.setRelation(3, QSqlRelation("Sources", "id", "source_name")) 

# t = model.relationModel(0)
# t.setFilter('agent_name = "name 2"')
# t.select()

# print(model.relationModel(0).filter())

# # Populate the model with data
# # model.select()

# # Create a view to display the table
# view = QTableView()
# view.setModel(model)

# # Show the main window
# window = QMainWindow()
# window.setCentralWidget(view)
# window.show()

# # app.exec_()
# from sqlalchemy import create_engine ,text
# from sqlalchemy.orm import sessionmaker
# import sqlalchemy as db
# # Create SQLAlchemy engine
# engine = create_engine('sqlite:///Data\database.db')

# # Create SQLAlchemy engine and session
# metadata = db.MetaData() #extracting the metadata
# division= db.Table('Live_Data', metadata, autoload_with=engine) #Table object

# print(division.select().filter(text('division.id = 1' )))

import pandas as pd
import sqlite3



con = sqlite3.connect("test.db")

df = pd.DataFrame({
    "uniqueval" :[9,3 , 8 , 7,48],
})
print(df)
df.to_sql("tests",con,if_exists='append',index=False)
