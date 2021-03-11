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
global started
started=False


id=parser['RequiredOnes']['id']
state=parser['RequiredOnes']['state']
details=parser['OptionalOnes']['details']
starttime=parser['OptionalOnes']['startime']
endtime=parser['OptionalOnes']['endtime']
largeimage=parser['OptionalOnes']['largeimage']
largeimage_tooltip=parser['OptionalOnes']['largeimage_tooltip']
smallimage=parser['OptionalOnes']['smallimage']
smallimage_tooltip=parser['OptionalOnes']['smallimage_tooltip']
button1=parser['CustomButtons']['button1']
button1url=parser['CustomButtons']['button1url']
button2=parser['CustomButtons']['button2']
button2url=parser['CustomButtons']['button2url']
partyid=parser['Advanced']['partyid']
partysize=parser['Advanced']['partysize']
chattoken=parser['Advanced']['chattoken']
gametoken=parser['Advanced']['gametoken']
spectatetoken=parser['Advanced']['spectatetoken']


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
		self.ui.IDTextBox.setText(id)
		self.ui.StatusTextBox.setText(state)
		self.ui.DetailsTextBox.setText(details)
		self.ui.StartTimeTextBox.setText(starttime)
		self.ui.EndTimeTextBox.setText(endtime)
		self.ui.LargeImageTextBox.setText(largeimage)
		self.ui.LargeImageTooltipTextBox.setText(largeimage_tooltip)
		self.ui.SmallImageTextBox.setText(smallimage)
		self.ui.SmallImageTooltipTextBox.setText(smallimage_tooltip)
		self.ui.FirstButtonTextBox.setText(button1)
		self.ui.FirstButtonLinkTextBox.setText(button1url)
		self.ui.SecondButtonTextBox.setText(button2)
		self.ui.SecondButtonLinkTextBox.setText(button2url)
		self.ui.PartyIDTextBox.setText(partyid)
		self.ui.PartySizeTextBox.setText(partysize)
		self.ui.GameTokenTextBox.setText(gametoken)
		self.ui.SpectateTokenTextBox.setText(spectatetoken)
		self.show()
		def StartStop():
			global started
			id=parser['RequiredOnes']['id']
			rpc=pypresence.Presence(client_id=id, pipe=0, loop=None, handler=None)
			rpc.connect()
			if started==False:
				print("started")
				started=True
				kwargs={}
				kwargs["buttons"]=[]
				if details!="":
					kwargs['details']=details
				if state!="":
					kwargs['state']=state
				if starttime!="":
					kwargs['starttime']=starttime
				if endtime!="":
					kwargs['endtime']=endtime
				if largeimage!="":
					kwargs['large_image']=largeimage
				if largeimage_tooltip!="":
					kwargs['large_text']=largeimage_tooltip
				if smallimage!="":
					kwargs['small_image']=smallimage
				if smallimage_tooltip!="":
					kwargs['small_text']=smallimage_tooltip
				if button1!="" and button1url!="":
					firstbutton={'label':str(button1),'url':str(button1url)}
					kwargs["buttons"].append(firstbutton)
				if button2!="" and button2url!="":
					secondbutton={'label':str(button2),'url':str(button2url)}
					kwargs["buttons"].append(secondbutton)
				try:
					rpc.update(**kwargs)
				except pypresence.exceptions.InvalidID:
					error_msg = QMessageBox()
					error_msg.setIcon(QMessageBox.Warning)
					error_msg.setText("You entered invalid ID. Please,check id again.")
					error_msg.setInformativeText("Invalid ID")
					error_msg.setStandardButtons(QMessageBox.Ok)
				except Exception as e:
					print(e)
			elif started==True:
				rpc.clear()
				rpc.close()
				started=False
				print("Stopped")
		self.ui.CustomButtons.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.ButtonsPage))
		self.ui.AdvancedToMain.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.MainPage))
		self.ui.ButtonsToMain.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.MainPage))
		self.ui.Advanced.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.AdvancedPage))
		self.ui.StartStop.clicked.connect(lambda: StartStop())



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()