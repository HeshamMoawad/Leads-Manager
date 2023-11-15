# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charts.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qcharts import QChartWidget
from QSqlModels.orm import session , Lead , RowOfLiveData , RowOfData , Source

class ChartsPage(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setObjectName("ChartsPage")
        self.resize(783, 607)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headerFrame = QtWidgets.QFrame(self.frame)
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leadsLabel = QtWidgets.QLabel(self.headerFrame)
        self.leadsLabel.setObjectName("leadsLabel")
        self.horizontalLayout.addWidget(self.leadsLabel, 0, QtCore.Qt.AlignHCenter)
        self.livedataLabel = QtWidgets.QLabel(self.headerFrame)
        self.livedataLabel.setObjectName("livedataLabel")
        self.horizontalLayout.addWidget(self.livedataLabel, 0, QtCore.Qt.AlignHCenter)
        self.dataLabel = QtWidgets.QLabel(self.headerFrame)
        self.dataLabel.setObjectName("dataLabel")
        self.horizontalLayout.addWidget(self.dataLabel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.headerFrame)
        self.countFrame = QtWidgets.QFrame(self.frame)
        self.countFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.countFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.countFrame.setObjectName("countFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.countFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leadsCount = QtWidgets.QLabel(self.countFrame)
        self.leadsCount.setObjectName("Counters")
        self.horizontalLayout_4.addWidget(self.leadsCount, 0, QtCore.Qt.AlignHCenter)
        self.livedataCount = QtWidgets.QLabel(self.countFrame)
        self.livedataCount.setObjectName("Counters")
        self.horizontalLayout_4.addWidget(self.livedataCount, 0, QtCore.Qt.AlignHCenter)
        self.dataCount = QtWidgets.QLabel(self.countFrame)
        self.dataCount.setObjectName("Counters")
        self.horizontalLayout_4.addWidget(self.dataCount, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.countFrame)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dounatchart = QChartWidget(self.frame_3)
        # dounat = self.dounatchart.getDounatChart("",{
        #     'Jan': 10,
        #     'Feb': 15,
        #     'Mar': 8,
        #     'Apr': 20,
        #     'May': 12,
        #     'Jun': 25,
        #     'Jul': 18,
        #     'Aug': 22,
        #     'Sep': 30,
        #     'Oct': 15,
        #     'Nov': 28,
        #     'Dec': 20,
        # })
        # self.dounatchart.setChart(dounat)
        self.horizontalLayout_2.addWidget(self.dounatchart)
        self.barchart = QChartWidget(self.frame_3)
        # dounat = self.barchart.getBarChart("Test bar",{
        #     'Jan': 10,
        #     'Feb': 15,
        #     'Mar': 8,
        #     'Apr': 20,
        #     'May': 12,
        #     'Jun': 25,
        #     'Jul': 18,
        #     'Aug': 22,
        #     'Sep': 30,
        #     'Oct': 15,
        #     'Nov': 28,
        #     'Dec': 20,
        # })
        # self.barchart.setChart(dounat)
        self.horizontalLayout_2.addWidget(self.barchart)
        self.horizontalLayout_2.setStretch(0,3)
        self.horizontalLayout_2.setStretch(1,5)

        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.linechart = QChartWidget(self.frame_4)
        # line = self.linechart.getLineChart("Test line",{
        #     'Jan': 10,
        #     'Apr': 20,
        #     'May': 12,
        #     'Jun': 25,
        #     'Sep': 30,
        #     'Oct': 15,
        #     'Nov': 28,
        #     'Dec': 20,
        #     'd': 20,
        # })
        # self.linechart.setChart(line)
        self.horizontalLayout_3.addWidget(self.linechart)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        self.leadsLabel.setText("Leads")
        self.livedataLabel.setText("Live Data")
        self.dataLabel.setText("Total Data") 

        self.leadsCount.setMinimumWidth(100)
        self.livedataCount.setMinimumWidth(100)
        self.dataCount.setMinimumWidth(100)
        self.leadsCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.livedataCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dataCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.leadsLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.livedataLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.dataLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.setCounters()
        self.setDounat()

    def setCounters(self):
        leadsCount = session.query(Lead).count()
        livedatacount = session.query(RowOfLiveData).count()
        totaldatacount = session.query(RowOfData).count()
        self.leadsCount.setText(f"{leadsCount}")
        self.livedataCount.setText(f"{livedatacount}")
        self.dataCount.setText(f"{totaldatacount}")

    def setDounat(self):
        data = {}
        sources = session.query(Source).all()
        for source in sources :
            data.update({source.name:session.query(RowOfLiveData).filter(RowOfLiveData.id.in_(session.query(Lead.live_data_id))).filter(RowOfLiveData.source_id == source.id).count()})
        chart = self.dounatchart.getDounatChart("Sources",data)
        self.dounatchart.setChart(chart)
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ChartsPage()
    ui.show()
    sys.exit(app.exec_())