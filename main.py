from PySide2.QtCore import *
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets
import UI
import time
import Resources
import json
import sys
import pypresence
conf=open("config.json")
config=json.load(conf)
conf.close()
global started
started=False


id=config['RequiredOnes']['id']
state=config['RequiredOnes']['state']
details=config['OptionalOnes']['details']
starttime=config['OptionalOnes']['starttime']
endtime=config['OptionalOnes']['endtime']
largeimage=config['OptionalOnes']['largeimage']
largeimage_tooltip=config['OptionalOnes']['largeimage_tooltip']
smallimage=config['OptionalOnes']['smallimage']
smallimage_tooltip=config['OptionalOnes']['smallimage_tooltip']
button1=config['CustomButtons']['button1']
button1url=config['CustomButtons']['button1url']
button2=config['CustomButtons']['button2']
button2url=config['CustomButtons']['button2url']
partyid=config['Advanced']['partyid']
partysize=config['Advanced']['partysize']
chattoken=config['Advanced']['chattoken']
gametoken=config['Advanced']['gametoken']
spectatetoken=config['Advanced']['spectatetoken']

def get_text(LineEdit):
	return LineEdit.text()
	
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
		self.shadow.setColor(QtGui.QColor(0, 92, 157, 150))
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
			id=get_text(self.ui.IDTextBox)
			state=get_text(self.ui.StatusTextBox)
			details=get_text(self.ui.DetailsTextBox)
			starttime=get_text(self.ui.StartTimeTextBox)
			endtime=get_text(self.ui.EndTimeTextBox)
			largeimage=get_text(self.ui.LargeImageTextBox)
			largeimage_tooltip=get_text(self.ui.LargeImageTooltipTextBox)
			smallimage=get_text(self.ui.SmallImageTextBox)
			smallimage_tooltip=get_text(self.ui.SmallImageTooltipTextBox)
			button1=get_text(self.ui.FirstButtonTextBox)
			button1url=get_text(self.ui.FirstButtonLinkTextBox)
			button2=get_text(self.ui.SecondButtonTextBox)
			button2url=get_text(self.ui.SecondButtonLinkTextBox)
			partyid=get_text(self.ui.PartyIDTextBox)
			partysize=get_text(self.ui.PartySizeTextBox)
			chattoken=get_text(self.ui.ChatTokenTextBox)
			gametoken=get_text(self.ui.GameTokenTextBox)
			spectatetoken=get_text(self.ui.SpectateTokenTextBox)
			global rpc
			rpc=pypresence.Presence(client_id=id, pipe=0, loop=None, handler=None)
			rpc.connect()
			if started==False:
				kwargs={}
				if details!="":
					kwargs['details']=details
				if state!="":
					kwargs['state']=state
				if starttime!="":
					kwargs['start']=int(starttime)
				if endtime!="":
					kwargs['end']=int(endtime)
				if largeimage!="":
					kwargs['large_image']=largeimage
				if largeimage_tooltip!="":
					kwargs['large_text']=largeimage_tooltip
				if smallimage!="":
					kwargs['small_image']=smallimage
				if smallimage_tooltip!="":
					kwargs['small_text']=smallimage_tooltip
				if button1!="" or button2!="":
					kwargs['buttons']=[]
					if button1!="" and button1url!="":
						firstbutton={'label':str(button1),'url':str(button1url)}
						kwargs["buttons"].append(firstbutton)
					if button2!="" and button2url!="":
						secondbutton={'label':str(button2),'url':str(button2url)}
						kwargs["buttons"].append(secondbutton)
				try:
					rpc.update(**kwargs)
					started=True
					config['RequiredOnes']['id']=id
					config['RequiredOnes']['state']=state
					config['OptionalOnes']['details']=details
					config['OptionalOnes']['starttime']=starttime
					config['OptionalOnes']['endtime']=endtime
					config['OptionalOnes']['largeimage']=largeimage
					config['OptionalOnes']['largeimage_tooltip']=largeimage_tooltip
					config['OptionalOnes']['smallimage']=smallimage
					config['OptionalOnes']['smallimage_tooltip']=smallimage_tooltip
					config['CustomButtons']['button1']=button1
					config['CustomButtons']['button1url']=button1url
					config['CustomButtons']['button2']=button2
					config['CustomButtons']['button2url']=button2url
					config['Advanced']['partyid']=partyid
					config['Advanced']['partysize']=partysize
					config['Advanced']['chattoken']=chattoken
					config['Advanced']['gametoken']=gametoken
					config['Advanced']['spectatetoken']=spectatetoken
					with open("config.json","w") as new_config:
						json.dump(config,new_config)
					print("started")
				except pypresence.exceptions.InvalidID:
					error_msg = QMessageBox()
					error_msg.setIcon(QMessageBox.Warning)
					error_msg.setText("You entered invalid ID. Please,check id again.")
					error_msg.setInformativeText("Invalid ID")
					error_msg.setStandardButtons(QMessageBox.Ok)
				except Exception as e:
					print(e)
			elif started==True:
				messagebox = QtWidgets.QMessageBox.warning(self, 'Custom Presence', 'Service already running. Use "Apply" button for applying changes.', QtWidgets.QMessageBox.Ok)



		def update():
			global started
			id=get_text(self.ui.IDTextBox)
			state=get_text(self.ui.StatusTextBox)
			details=get_text(self.ui.DetailsTextBox)
			starttime=get_text(self.ui.StartTimeTextBox)
			endtime=get_text(self.ui.EndTimeTextBox)
			largeimage=get_text(self.ui.LargeImageTextBox)
			largeimage_tooltip=get_text(self.ui.LargeImageTooltipTextBox)
			smallimage=get_text(self.ui.SmallImageTextBox)
			smallimage_tooltip=get_text(self.ui.SmallImageTooltipTextBox)
			button1=get_text(self.ui.FirstButtonTextBox)
			button1url=get_text(self.ui.FirstButtonLinkTextBox)
			button2=get_text(self.ui.SecondButtonTextBox)
			button2url=get_text(self.ui.SecondButtonLinkTextBox)
			partyid=get_text(self.ui.PartyIDTextBox)
			partysize=get_text(self.ui.PartySizeTextBox)
			chattoken=get_text(self.ui.ChatTokenTextBox)
			gametoken=get_text(self.ui.GameTokenTextBox)
			spectatetoken=get_text(self.ui.SpectateTokenTextBox)
			global rpc
			if started==True:
				kwargs={}
				if details!="":
					kwargs['details']=details
				if state!="":
					kwargs['state']=state
				if starttime!="":
					kwargs['start']=starttime
				if endtime!="":
					kwargs['end']=endtime
				if largeimage!="":
					kwargs['large_image']=largeimage
				if largeimage_tooltip!="":
					kwargs['large_text']=largeimage_tooltip
				if smallimage!="":
					kwargs['small_image']=smallimage
				if smallimage_tooltip!="":
					kwargs['small_text']=smallimage_tooltip
				if button1!="" or button2!="":
					kwargs['buttons']=[]
					if button1!="" and button1url!="":
						firstbutton={'label':str(button1),'url':str(button1url)}
						kwargs["buttons"].append(firstbutton)
					if button2!="" and button2url!="":
						secondbutton={'label':str(button2),'url':str(button2url)}
						kwargs["buttons"].append(secondbutton)
				try:
					rpc.update(**kwargs)
					started=True
					config['RequiredOnes']['id']=id
					config['RequiredOnes']['state']=state
					config['OptionalOnes']['details']=details
					config['OptionalOnes']['starttime']=starttime
					config['OptionalOnes']['endtime']=endtime
					config['OptionalOnes']['largeimage']=largeimage
					config['OptionalOnes']['largeimage_tooltip']=largeimage_tooltip
					config['OptionalOnes']['smallimage']=smallimage
					config['OptionalOnes']['smallimage_tooltip']=smallimage_tooltip
					config['CustomButtons']['button1']=button1
					config['CustomButtons']['button1url']=button1url
					config['CustomButtons']['button2']=button2
					config['CustomButtons']['button2url']=button2url
					config['Advanced']['partyid']=partyid
					config['Advanced']['partysize']=partysize
					config['Advanced']['chattoken']=chattoken
					config['Advanced']['gametoken']=gametoken
					config['Advanced']['spectatetoken']=spectatetoken
					with open("config.json","w") as new_config:
						json.dump(config,new_config)
					print("Updated.")
				except Exception as e:
					print(e)
			elif started==False:
				messagebox = QtWidgets.QMessageBox.warning(self, 'Custom Presence', 'You need to start service first.', QtWidgets.QMessageBox.Ok)
		self.ui.CustomButtons.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.ButtonsPage))
		self.ui.AdvancedToMain.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.MainPage))
		self.ui.ButtonsToMain.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.MainPage))
		self.ui.Advanced.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.AdvancedPage))
		self.ui.StartStop.clicked.connect(lambda: StartStop())
		self.ui.Apply.clicked.connect(lambda: update())



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
QtGui.QFontDatabase.addApplicationFont('./fonts/OpenSans-Regular.ttf')
QtGui.QFontDatabase.addApplicationFont('./fonts/Raleway-Regular.ttf')
QtGui.QFontDatabase.addApplicationFont('./fonts/Roboto-Regular.ttf')
window.show()
app.exec_()