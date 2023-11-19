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

# import pandas as pd
# import sqlite3



# con = sqlite3.connect("test.db")

# df = pd.DataFrame({
#     "uniqueval" :[9,3 , 8 , 7,48],
# })
# print(df)
# df.to_sql("tests",con,if_exists='append',index=False)

# import re

# text = """Your text containing phone numbers goes here.
# +966546987321 548963215 966584963123 +966 50 231 9548

# """

# # Regex pattern to find Saudi Arabian phone numbers
# pattern = r'\b(?:\+?966\s?5\d{8}|\b5\d{8})\b'

# # Find all matches in the text
# matches = re.findall(pattern, text)

# # Print the matches
# print(matches)
# import pathlib
# import os

# BASE_DIR = pathlib.Path(__file__).resolve().parent
# directory = os.path.join(BASE_DIR,"Exports","2023","11","6")
# if os.path.isdir(directory) :
#     print("True")
# else :
#     os.makedirs(directory)
# from project.utils import getdir


# print(getdir("tttt.xlsx"))
# from PyQt5 import QtCore 

# t = QtCore.QDate(0,0,0)
# print(True if  t == QtCore.QDate() else None)
# from project.QSqlModels.orm.db import con
# import pandas

# df = pandas.read_sql_query("SELECT * FROM data",con)

# print(df)

# df.drop_duplicates(inplace=True)
# print(df)

################################################################################

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# from matplotlib.dates import date2num
# from datetime import datetime
# import calendar , numpy


# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(100, 100, 800, 600)
#         self.setWindowTitle("Matplotlib in PyQt5 Example")

#         # Create a central widget with a QVBoxLayout
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout(central_widget)

#         # Create a Matplotlib figure and canvas
#         self.figure = Figure()
#         self.canvas = FigureCanvas(self.figure)
#         layout.addWidget(self.canvas)

#         # Create QLineEdit widgets for entering values and labels
#         self.dates_input = QLineEdit(self)
#         self.values_input = QLineEdit(self)
#         layout.addWidget(QLabel("Enter Dates (YYYY-MM-DD):"))
#         layout.addWidget(self.dates_input)
#         layout.addWidget(QLabel("Enter Values:"))
#         layout.addWidget(self.values_input)

#         # Create a "Plot" button
#         self.plot_button = QPushButton("Plot", self)
#         self.plot_button.clicked.connect(self.plot_chart)
#         layout.addWidget(self.plot_button)

#     def plot_chart(self):
#         # Get dates and values from input fields
#         dates_str = self.dates_input.text()
#         values_str = self.values_input.text()

#         # Convert string input to lists of dates and values
#         dates = list(calendar.month_abbr[1:]) #[datetime.strptime(date.strip(), '%Y-%m-%d') for date in dates_str.split(',')]
#         values = numpy.random.randn(len(dates)-1)
#         print(values)

#         # Update the chart with new data
#         self.update_chart(dates, values)

#     def update_chart(self, dates, values):
#         # Clear previous data
#         self.figure.clear()

#         # Plot the new data
#         ax = self.figure.add_subplot(111)
#         ax.scatter(dates,values)

#         ax.set_title('Leads Over Time')
#         ax.set_xlabel('Dates')
#         ax.set_ylabel('Number of Leads')

#         # Redraw the canvas
#         self.canvas.draw()

# if __name__ == "__main__":

#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())
###########################################################################################
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis , QPieSeries 
# from PyQt5.QtGui import QPainter , QColor
# from PyQt5.QtCore import Qt


# class ChartExample(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(100, 100, 800, 600)
#         self.setWindowTitle("PyQtChart Example")

#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout(central_widget)

#         # Create a chart
#         chart = QChart()
#         chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
#         # chart.setTheme(QChart.ChartTheme.ChartThemeDark)
#         # Create a line series
#         series = QPieSeries()
#         series.setHoleSize(0.30)
#         slice = series.append("asddd",1.7)
#         slice.setExploded(True)
#         slice.setLabelVisible(True)

#         series.append("adwqrqtrtt",3.4)
#         # series.append(0, 0)

#         # # Add the series to the chart
#         chart.addSeries(series)

#         # Create X and Y axes
#         axis_x = QValueAxis()
#         axis_y = QValueAxis()

#         # Set labels for axes
#         axis_x.setTitleText("X Axis")
#         axis_y.setTitleText("Y Axis")

#         # Add axes to the chart
#         chart.setAxisX(axis_x, series)
#         chart.setAxisY(axis_y, series)

#         # Create a chart view
#         chart_view = QChartView(chart)
#         chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
#         # chart_view.setStyleSheet("""
#         # QGraphicsView{
#         # background-color:red;
#         # border:2px solid blue;
#         # border-radius:20px;
#         # }
        
#         # """)

#         layout.addWidget(chart_view)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ChartExample()
#     window.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget , QPushButton
# from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis , QPieSlice
# from PyQt5.QtCore import Qt

# class BarChartExample(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(100, 100, 800, 600)
#         self.setWindowTitle("Basic Bar Chart Example")

#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout(central_widget)

#         # Create a bar chart
#         chart = QChart()
#         chart.setTitle("Sample Bar Chart")
#         chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)

#         # Create a bar series
#         series = QBarSeries()

#         # Create a bar set with data
#         bar_set = QBarSet("Values")
#         bar_set << 1 << 2 << 3 << 4 << 5

#         # Add the bar set to the series
#         series.append(bar_set)

#         # Add the series to the chart
#         chart.addSeries(series)


#         # Create the X axis
#         axis_x = QBarCategoryAxis()
#         axis_x.append("data")
#         chart.addAxis(axis_x, Qt.AlignBottom)
#         chart.setAxisX(axis_x, series)

#         # Create the Y axis
#         axis_y = QValueAxis()
#         chart.addAxis(axis_y, Qt.AlignLeft)
#         chart.setAxisY(axis_y, series)

#         # Create a chart view
#         chart_view = QChartView(chart)
#         layout.addWidget(chart_view)
#         btn = QPushButton(central_widget)
#         btn.clicked.connect(lambda : chart.removeSeries(series))
#         btn.clicked.connect(lambda : chart.addSeries(series))
#         layout.addWidget(btn)

        

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = BarChartExample()
#     window.show()
#     sys.exit(app.exec_())


# from PyQt5.QtChart import QLineSeries, QValueAxis, QChart, QChartView , QBarCategoryAxis
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# import sys
# from datetime import datetime

# class QChartWidget(QChartView):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#     def getLineChart(self, title: str, data: dict) -> QChart:
#         chart = QChart()
#         chart.setTitle(title)


#         line_series = QLineSeries()
#         for month, leads in data.items():
#             timestamp = datetime.strptime(month, '%b').month  # Convert month abbreviation to number
#             line_series.append(timestamp, leads)
#             print(timestamp, leads)

#         chart.addSeries(line_series)

#         axis_x = QBarCategoryAxis()
#         axis_x.setCategories(data.keys())
#         chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
#         chart.setAxisX(axis_x,line_series)

#         axis_y = QValueAxis()
#         chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
#         chart.setAxisY(axis_y,line_series)


#         return chart



# class LineChartExample(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(100, 100, 800, 600)
#         self.setWindowTitle("Line Chart Example")

#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout(central_widget)

#         # Example data with months and leads
#         data = {
#             'Jan': 10,
#             'Feb': 15,
#             'Mar': 8,
#             'Apr': 20,
#             'May': 12,
#             'Jun': 25,
#             'Jul': 18,
#             'Aug': 22,
#             'Sep': 30,
#             'Oct': 15,
#             'Nov': 28,
#             'Dec': 20,
#         }

#         chart_widget = QChartWidget()
#         chart = chart_widget.getLineChart("Leads per Month", data)
#         chart_view = QChartView(chart)
#         layout.addWidget(chart_view)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = LineChartExample()
#     window.show()
#     sys.exit(app.exec_())



# import calendar 
# from datetime import datetime



# print(calendar.monthrange(2023,1))
# x = calendar.month_abbr[1]
# print(x)

# data = {}

# for index in range(1,13):
#     print(index)
#     name = calendar.month_abbr[index]
#     last_day = calendar.monthrange(2023,index)[1]
#     date_from = datetime(datetime.now().year,index,1)
#     date_to = datetime(datetime.now().year,index,last_day)
#     data.update({name:[date_from,date_to]})

# print(data)


from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QValueAxis, QLineSeries , QChartView, QChart
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a chart
        chart = QChart()

        # Create a value axis
        axisY = QValueAxis()

        # Set the tick count to control the number of ticks on the axis
        axisY.setTickCount(10)

        # Set the label format to display integers
        axisY.setLabelFormat("%.0f")

        # Add the axis to the chart

        # Create a series with some data
        series = QLineSeries()
        series.append(1, 1)
        series.append(2, 4)
        series.append(3, 9)
        series.append(4, 16)
        series.append(5, 25)

        # Add the series to the chart
        chart.addSeries(series)
        chart.setAxisY(axisY,series)

        # # Attach the series to the axis
        # chart.setAxisY(axisY, series)

        # Create a chart view and set the chart on it
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Set the central widget
        self.setCentralWidget(chart_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
