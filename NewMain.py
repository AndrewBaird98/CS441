import self as self
from PySide2 import QtCore, QtGui, QtWidgets
from Event import Event
import ProjectUI
import WebScraperTest
import GoogleCalendar
import EventManager
import ProjectUI2
from functools import partial

class MyQtAPP(ProjectUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtAPP, self).__init__()
        self.setupUi(self)
        self.ui = ProjectUI2.Ui_EventWindow()
        self.window = QtWidgets.QMainWindow()


        self.AddEventsCalndar.clicked.connect(self.GoogleAddEvent)
        self.PrintEventsCalendar.clicked.connect(self.GooglePrintEvent)

        self.labelList = []
        EventManager.FindEvents()
        self.EventPage()
        for i in range(len(self.labelList)):
            self.labelList[i].mousePressEvent = lambda event: self.oneEventInfo(i)

        self.DarkModeButton.toggled.connect(self.DarkMode)


    def EventPage(self):
        for e in EventManager.FullEventList:
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            label.setMinimumSize(QtCore.QSize(0, 40))
            label.setCursor(QtCore.Qt.PointingHandCursor)
            label.setStyleSheet("background-color: rgb(255, 255, 255);")
            label.setMargin(6)
            label.setWordWrap(True)
            label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
            label.setObjectName("label")
            label.setText(e.name + "\n    " + e.date)
            self.verticalLayout_2.addWidget(label)
            self.labelList.append(label)

    def oneEventInfo(self, i):
        self.ui.setupUi(self.window)
        EventManager.EventInfoDisplay(EventManager.FullEventList[i], self.ui.textBrowser)
        self.window.show()

    def GoogleAddEvent(self):
        service = GoogleCalendar.getAPI()
        attendees = ['baird013@cougars.csusm.edu']
        currentEvent = Event("Taco Tuesday", "2019-11-28", "09:00:00-07:00", "17:00:00-07:00", "San Marcos", "CA", "$6",
                             "300 San Marcos Blvd", "Nightlife", "Enjoy Tacos half price", "www.google.com", "+21",
                             'RRULE:FREQ=DAILY;COUNT=2;', attendees)
        GoogleCalendar.AddEvent(service, self.textBrowser_2, currentEvent)

    def GooglePrintEvent(self):
        service = GoogleCalendar.getAPI()
        GoogleCalendar.printEvents(service, 10, self.textBrowser_2)


    def DarkMode(self):
        if self.DarkModeButton.isChecked() == True:
            self.centralwidget.setStyleSheet("background-color: rgb(51, 51, 51);")
            self.frame.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                     "border-color: rgb(204, 204, 204);\n"
                                     "")
            self.SearchButton.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.searchBar.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                         "color: rgb(230, 230, 230);\n"
                                         "selection-background-color: rgba(102, 204, 255, 243);")
            self.DarkModeButton.setStyleSheet("color: rgb(230, 230, 230);\n"
                                           "")
            self.toolButton.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.HomeWidget.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.tableWidget.setStyleSheet("background-color: rgb(128, 128, 128);")
            self.MyEventsTab.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.scrollArea.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.textBrowser_2.setStyleSheet("background-color: rgb(128, 128, 128);\n"
                                             "color: rgb(255, 255, 255);")
            self.AddEventsCalndar.setStyleSheet("background-color: rgb(128, 0, 64);\n"
                                                "color: rgb(255, 255, 255);")
            self.PrintEventsCalendar.setStyleSheet("background-color: rgb(128, 0, 64);\n"
                                                   "color: rgb(255, 255, 255);")
            self.frame_2.setStyleSheet("background-color: rgb(25, 25, 25);")
            self.tableWidget.setStyleSheet("background-color: rgb(128, 128, 128);")

            for i in self.labelList:
                i.setStyleSheet("background-color: rgb(128, 128, 128);\n"
                                           "color: rgb(255, 255, 255);")

        else:
            self.centralwidget.setStyleSheet("default")
            self.frame.setStyleSheet("default")
            self.SearchButton.setStyleSheet("default")
            self.searchBar.setStyleSheet("default")
            self.DarkModeButton.setStyleSheet("default")
            self.toolButton.setStyleSheet("default")
            self.HomeWidget.setStyleSheet("default")
            self.EventsWidget.setStyleSheet("default")
            self.AllEventsTab.setStyleSheet("default")
            self.EventTab.setStyleSheet("default")
            self.MyEventsTab.setStyleSheet("default")
            self.CalendarTab.setStyleSheet("default")
            self.tableWidget.setStyleSheet("default")
            self.MyEventsTab.setStyleSheet("default")
            self.textBrowser_2.setStyleSheet("default")
            self.AddEventsCalndar.setStyleSheet("default")
            self.PrintEventsCalendar.setStyleSheet("default")
            self.frame_2.setStyleSheet("background-color: rgb(7, 64, 128);")
            self.tableWidget.setStyleSheet("default")
            self.scrollArea.setStyleSheet("default")
            self.scrollAreaWidgetContents.setStyleSheet("default")
            for i in self.labelList:
                i.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtAPP()
    qt_app.show()
    app.exec_()

