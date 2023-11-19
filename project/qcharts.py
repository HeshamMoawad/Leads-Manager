from PyQt5.QtChart import (
    QChart ,
    QChartView,
    QPieSeries ,
    QLineSeries ,
    QBarSeries ,
    QPieSlice ,
    QBarSet ,
    QBarCategoryAxis ,
    QValueAxis ,
    QDateTimeAxis
)
from PyQt5.QtCore import (
    QObject ,
    Qt ,
)
from PyQt5.QtGui import(
    QPainter ,
    QColor
)
import typing

# class QChartConverter(QObject):
#     def __init__(self, parent: QObject = None) -> None:
#         super().__init__(parent)

#     def getPieChart(self):

    

class QChartWidget(QChartView):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

    def _getChart(self,title:str)-> QChart:
        chart = QChart()
        chart.setTitle(title)
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        chart.legend().setVisible(False)
        return chart


    def getDounatChart(self,title:str,data:typing.Dict[str,float])-> QChart:
        chart = self._getChart(title)
        series = QPieSeries()
        series.setHoleSize(0.39)
        highslice = QPieSlice()
        for label , value in data.items():
            slice = series.append(label,float(value))
            slice.clicked.connect(self.explodeSlice)
            slice.setLabel(f"{label} : {int(value)}")
            if slice.value() > highslice.value() :
                highslice = slice

        chart.addSeries(series)
        return chart

    def explodeSlice(self):
        slice = self.sender()  
        if slice.isExploded():
            slice.setExploded(False)
            slice.setLabelVisible(False)
        else :
            slice.setExploded(True)
            slice.setLabelVisible(True)




    def getBarChart(self,title:str,data:typing.Dict[str,float])-> QChart:
        chart = self._getChart(title)
        series = QBarSeries()
        set = QBarSet("Average")
        set.setColor(QColor(33,177,255,255))
        set.append(data.values())
        series.append(set)
        chart.addSeries(series)
        axis_x = QBarCategoryAxis()
        axis_x.setCategories(data.keys())
        chart.addAxis(axis_x,Qt.AlignmentFlag.AlignBottom)
        chart.setAxisX(axis_x,series)
        axis_y = QValueAxis()
        axis_y.setTickCount(10)
        axis_y.setLabelFormat("%.0f")
        chart.addAxis(axis_y,Qt.AlignmentFlag.AlignLeft)
        chart.setAxisY(axis_y,series)
        return chart



    def getLineChart(self, title: str, data: typing.Dict[str, typing.Tuple[float]]) -> QChart:
        chart = self._getChart(title)
        line_series = QLineSeries()
        for index , value in enumerate(data.values()):
            line_series.append(index,value)
        chart.addSeries(line_series)
        axis_x = QBarCategoryAxis()
        axis_x.setCategories(data.keys())
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.setAxisX(axis_x,line_series)
        axis_y = QValueAxis()
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        chart.setAxisY(axis_y,line_series)

        return chart




