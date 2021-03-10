from PySide2.QtCore import *
from PySide2.QtGui import *
import PySide2.QtWidgets as QtWidgets
import UI
import Resources
import sys
import configparser
import pypresence
parser=configparser.ConfigParser()
parser.read("config.ini")

class MainWindow(QtWidgets.QMainWindow, UI.Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.ui= UI.Ui_MainWindow()
		self.ui.setupUi(self)
		self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.threadpool = QThreadPool()
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 92, 157, 150))
		self.ui.Pages.setCurrentWidget(self.ui.MainPage)
		self.setWindowTitle("Custom Rich Presence")
		self.show()
		def start():
			id=parser['RequiredOnes']['id']
			state=parser['RequiredOnes']['state']
			details=parser['OptionalOnes']['details']
			
			args={}
			if details!="":
				args['details']=details
			if state!="":
				args['state']=state
			print(id,state,details)
			rpc_client=pypresence.Client(client_id=id, pipe=0, loop=None, handler=None)
			while True:
				QtWidgets.QApplication.processEvents()
				rpc_client.start()
				rpc_client.set_activity(**args)
		self.ui.CustomButtons.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.ButtonsPage))
		self.ui.AdvancedToMain.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.MainPage))
		self.ui.ButtonsToMain.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.MainPage))
		self.ui.Advanced.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.AdvancedPage))
		self.ui.StartStop.clicked.connect(lambda: start())



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()