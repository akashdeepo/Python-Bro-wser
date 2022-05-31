from msilib.schema import Font
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        #backbutton
        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)


        #forwardbutton
        fwd_btn = QAction('Forward',self)
        fwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fwd_btn)

        #reloadbutton
        refresh_btn = QAction('Refresh',self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        #Homebutton
        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        #adding a search bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        #to change search bar url when site changes
        self.browser.urlChanged.connect(self.update_url)

    #defining the functionalities!!
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Bro-wser')
window = MainWindow()
app.exec_()