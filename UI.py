# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIwUNgWF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 527)
        MainWindow.setMinimumSize(QSize(507, 527))
        MainWindow.setMaximumSize(QSize(507, 527))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(507, 527))
        self.centralwidget.setMaximumSize(QSize(507, 527))
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(0, 0, 507, 527))
        self.MainFrame.setMinimumSize(QSize(507, 527))
        self.MainFrame.setMaximumSize(QSize(507, 527))
        self.MainFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(239, 41, 41, 255), stop:1 rgba(114, 159, 207, 255));")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.Pages = QStackedWidget(self.MainFrame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setGeometry(QRect(10, 0, 491, 527))
        self.Pages.setMaximumSize(QSize(507, 527))
        font = QFont()
        font.setFamily(u"Roboto Condensed")
        self.Pages.setFont(font)
        self.Pages.setCursor(QCursor(Qt.ArrowCursor))
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.MainTitle = QLabel(self.MainPage)
        self.MainTitle.setObjectName(u"MainTitle")
        self.MainTitle.setGeometry(QRect(150, 0, 199, 31))
        self.MainTitle.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 14pt \"Raleway\";")
        self.MainDetails = QFrame(self.MainPage)
        self.MainDetails.setObjectName(u"MainDetails")
        self.MainDetails.setGeometry(QRect(80, 30, 341, 441))
        self.MainDetails.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;\n"
"")
        self.MainDetails.setFrameShape(QFrame.StyledPanel)
        self.MainDetails.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainDetails)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ID = QFrame(self.MainDetails)
        self.ID.setObjectName(u"ID")
        self.ID.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.ID.setFrameShape(QFrame.StyledPanel)
        self.ID.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ID)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.IDText = QLabel(self.ID)
        self.IDText.setObjectName(u"IDText")
        self.IDText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_3.addWidget(self.IDText)

        self.IDTextBox = QLineEdit(self.ID)
        self.IDTextBox.setObjectName(u"IDTextBox")
        self.IDTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_3.addWidget(self.IDTextBox)


        self.verticalLayout.addWidget(self.ID)

        self.Status = QFrame(self.MainDetails)
        self.Status.setObjectName(u"Status")
        self.Status.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.Status.setFrameShape(QFrame.StyledPanel)
        self.Status.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Status)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.StatusText = QLabel(self.Status)
        self.StatusText.setObjectName(u"StatusText")
        self.StatusText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout.addWidget(self.StatusText)

        self.StatusTextBox = QLineEdit(self.Status)
        self.StatusTextBox.setObjectName(u"StatusTextBox")
        self.StatusTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout.addWidget(self.StatusTextBox)


        self.verticalLayout.addWidget(self.Status)

        self.Details = QFrame(self.MainDetails)
        self.Details.setObjectName(u"Details")
        self.Details.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.Details.setFrameShape(QFrame.StyledPanel)
        self.Details.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Details)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.DetailsText = QLabel(self.Details)
        self.DetailsText.setObjectName(u"DetailsText")
        self.DetailsText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_5.addWidget(self.DetailsText)

        self.DetailsTextBox = QLineEdit(self.Details)
        self.DetailsTextBox.setObjectName(u"DetailsTextBox")
        self.DetailsTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_5.addWidget(self.DetailsTextBox)


        self.verticalLayout.addWidget(self.Details)

        self.StartTime = QFrame(self.MainDetails)
        self.StartTime.setObjectName(u"StartTime")
        self.StartTime.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.StartTime.setFrameShape(QFrame.StyledPanel)
        self.StartTime.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.StartTime)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.StartTimeText = QLabel(self.StartTime)
        self.StartTimeText.setObjectName(u"StartTimeText")
        self.StartTimeText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_2.addWidget(self.StartTimeText)

        self.StartTimeTextBox = QLineEdit(self.StartTime)
        self.StartTimeTextBox.setObjectName(u"StartTimeTextBox")
        self.StartTimeTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_2.addWidget(self.StartTimeTextBox)


        self.verticalLayout.addWidget(self.StartTime)

        self.EndTime = QFrame(self.MainDetails)
        self.EndTime.setObjectName(u"EndTime")
        self.EndTime.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.EndTime.setFrameShape(QFrame.StyledPanel)
        self.EndTime.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.EndTime)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.EndTimeText = QLabel(self.EndTime)
        self.EndTimeText.setObjectName(u"EndTimeText")
        self.EndTimeText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_4.addWidget(self.EndTimeText)

        self.EndTimeTextBox = QLineEdit(self.EndTime)
        self.EndTimeTextBox.setObjectName(u"EndTimeTextBox")
        self.EndTimeTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_4.addWidget(self.EndTimeTextBox)


        self.verticalLayout.addWidget(self.EndTime)

        self.LargeImage = QFrame(self.MainDetails)
        self.LargeImage.setObjectName(u"LargeImage")
        self.LargeImage.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.LargeImage.setFrameShape(QFrame.StyledPanel)
        self.LargeImage.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.LargeImage)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LargeImageText = QLabel(self.LargeImage)
        self.LargeImageText.setObjectName(u"LargeImageText")
        self.LargeImageText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_7.addWidget(self.LargeImageText)

        self.LargeImageTextBox = QLineEdit(self.LargeImage)
        self.LargeImageTextBox.setObjectName(u"LargeImageTextBox")
        self.LargeImageTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_7.addWidget(self.LargeImageTextBox)


        self.verticalLayout.addWidget(self.LargeImage)

        self.LargeImageTooltip = QFrame(self.MainDetails)
        self.LargeImageTooltip.setObjectName(u"LargeImageTooltip")
        self.LargeImageTooltip.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.LargeImageTooltip.setFrameShape(QFrame.StyledPanel)
        self.LargeImageTooltip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.LargeImageTooltip)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LargeImageTooltipText = QLabel(self.LargeImageTooltip)
        self.LargeImageTooltipText.setObjectName(u"LargeImageTooltipText")
        self.LargeImageTooltipText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_6.addWidget(self.LargeImageTooltipText)

        self.LargeImageTooltipTextBox = QLineEdit(self.LargeImageTooltip)
        self.LargeImageTooltipTextBox.setObjectName(u"LargeImageTooltipTextBox")
        self.LargeImageTooltipTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_6.addWidget(self.LargeImageTooltipTextBox)


        self.verticalLayout.addWidget(self.LargeImageTooltip)

        self.SmallImage = QFrame(self.MainDetails)
        self.SmallImage.setObjectName(u"SmallImage")
        self.SmallImage.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.SmallImage.setFrameShape(QFrame.StyledPanel)
        self.SmallImage.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.SmallImage)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.SmallImageText = QLabel(self.SmallImage)
        self.SmallImageText.setObjectName(u"SmallImageText")
        self.SmallImageText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_8.addWidget(self.SmallImageText)

        self.SmallImageTextBox = QLineEdit(self.SmallImage)
        self.SmallImageTextBox.setObjectName(u"SmallImageTextBox")
        self.SmallImageTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_8.addWidget(self.SmallImageTextBox)


        self.verticalLayout.addWidget(self.SmallImage)

        self.SmallImageTooltip = QFrame(self.MainDetails)
        self.SmallImageTooltip.setObjectName(u"SmallImageTooltip")
        self.SmallImageTooltip.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.SmallImageTooltip.setFrameShape(QFrame.StyledPanel)
        self.SmallImageTooltip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.SmallImageTooltip)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.SmallImageTooltipText = QLabel(self.SmallImageTooltip)
        self.SmallImageTooltipText.setObjectName(u"SmallImageTooltipText")
        self.SmallImageTooltipText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_9.addWidget(self.SmallImageTooltipText)

        self.SmallImageTooltipTextBox = QLineEdit(self.SmallImageTooltip)
        self.SmallImageTooltipTextBox.setObjectName(u"SmallImageTooltipTextBox")
        self.SmallImageTooltipTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_9.addWidget(self.SmallImageTooltipTextBox)


        self.verticalLayout.addWidget(self.SmallImageTooltip)

        self.Buttons = QFrame(self.MainPage)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setGeometry(QRect(0, 451, 481, 71))
        self.Buttons.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:none;")
        self.Buttons.setFrameShape(QFrame.StyledPanel)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.Buttons)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.CustomButtons = QPushButton(self.Buttons)
        self.CustomButtons.setObjectName(u"CustomButtons")
        self.CustomButtons.setCursor(QCursor(Qt.PointingHandCursor))
        self.CustomButtons.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 14px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")
        icon = QIcon()
        icon.addFile(u":/Arrows/buttons.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CustomButtons.setIcon(icon)
        self.CustomButtons.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.CustomButtons)

        self.StartStop = QPushButton(self.Buttons)
        self.StartStop.setObjectName(u"StartStop")
        self.StartStop.setCursor(QCursor(Qt.PointingHandCursor))
        self.StartStop.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 14px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"border-radius: 12px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")
        self.StartStop.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.StartStop)

        self.Apply = QPushButton(self.Buttons)
        self.Apply.setObjectName(u"Apply")
        self.Apply.setCursor(QCursor(Qt.PointingHandCursor))
        self.Apply.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 12px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")
        self.Apply.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.Apply)

        self.MainToEpoch = QPushButton(self.Buttons)
        self.MainToEpoch.setObjectName(u"MainToEpoch")
        self.MainToEpoch.setCursor(QCursor(Qt.PointingHandCursor))
        self.MainToEpoch.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 12px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")

        self.horizontalLayout_20.addWidget(self.MainToEpoch)

        self.Advanced = QPushButton(self.Buttons)
        self.Advanced.setObjectName(u"Advanced")
        self.Advanced.setCursor(QCursor(Qt.PointingHandCursor))
        self.Advanced.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")
        icon1 = QIcon()
        icon1.addFile(u":/Arrows/Settings icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Advanced.setIcon(icon1)
        self.Advanced.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.Advanced)

        self.Pages.addWidget(self.MainPage)
        self.AdvancedPage = QWidget()
        self.AdvancedPage.setObjectName(u"AdvancedPage")
        self.AdvancedTitle = QLabel(self.AdvancedPage)
        self.AdvancedTitle.setObjectName(u"AdvancedTitle")
        self.AdvancedTitle.setGeometry(QRect(170, 30, 171, 21))
        self.AdvancedTitle.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 14pt \"Raleway\";")
        self.AdvancedToMain = QPushButton(self.AdvancedPage)
        self.AdvancedToMain.setObjectName(u"AdvancedToMain")
        self.AdvancedToMain.setGeometry(QRect(29, 20, 81, 41))
        self.AdvancedToMain.setCursor(QCursor(Qt.PointingHandCursor))
        self.AdvancedToMain.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")
        icon2 = QIcon()
        icon2.addFile(u":/Arrows/Left arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AdvancedToMain.setIcon(icon2)
        self.AdvancedToMain.setIconSize(QSize(20, 20))
        self.AdvancedDetails = QFrame(self.AdvancedPage)
        self.AdvancedDetails.setObjectName(u"AdvancedDetails")
        self.AdvancedDetails.setGeometry(QRect(38, 67, 441, 221))
        self.AdvancedDetails.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.AdvancedDetails.setFrameShape(QFrame.StyledPanel)
        self.AdvancedDetails.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.AdvancedDetails)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.PartyID = QFrame(self.AdvancedDetails)
        self.PartyID.setObjectName(u"PartyID")
        self.PartyID.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.PartyID.setFrameShape(QFrame.StyledPanel)
        self.PartyID.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.PartyID)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.PartyIDText = QLabel(self.PartyID)
        self.PartyIDText.setObjectName(u"PartyIDText")
        self.PartyIDText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_10.addWidget(self.PartyIDText)

        self.PartyIDTextBox = QLineEdit(self.PartyID)
        self.PartyIDTextBox.setObjectName(u"PartyIDTextBox")
        self.PartyIDTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_10.addWidget(self.PartyIDTextBox)


        self.verticalLayout_2.addWidget(self.PartyID)

        self.PartySize = QFrame(self.AdvancedDetails)
        self.PartySize.setObjectName(u"PartySize")
        self.PartySize.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.PartySize.setFrameShape(QFrame.StyledPanel)
        self.PartySize.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.PartySize)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.PartySizeText = QLabel(self.PartySize)
        self.PartySizeText.setObjectName(u"PartySizeText")
        self.PartySizeText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_11.addWidget(self.PartySizeText)

        self.PartySizeTextBox = QLineEdit(self.PartySize)
        self.PartySizeTextBox.setObjectName(u"PartySizeTextBox")
        self.PartySizeTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_11.addWidget(self.PartySizeTextBox)


        self.verticalLayout_2.addWidget(self.PartySize)

        self.ChatToken = QFrame(self.AdvancedDetails)
        self.ChatToken.setObjectName(u"ChatToken")
        self.ChatToken.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.ChatToken.setFrameShape(QFrame.StyledPanel)
        self.ChatToken.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.ChatToken)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ChatTokeText = QLabel(self.ChatToken)
        self.ChatTokeText.setObjectName(u"ChatTokeText")
        self.ChatTokeText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_12.addWidget(self.ChatTokeText)

        self.ChatTokenTextBox = QLineEdit(self.ChatToken)
        self.ChatTokenTextBox.setObjectName(u"ChatTokenTextBox")
        self.ChatTokenTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_12.addWidget(self.ChatTokenTextBox)


        self.verticalLayout_2.addWidget(self.ChatToken)

        self.GameToken = QFrame(self.AdvancedDetails)
        self.GameToken.setObjectName(u"GameToken")
        self.GameToken.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.GameToken.setFrameShape(QFrame.StyledPanel)
        self.GameToken.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.GameToken)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.GameTokenText = QLabel(self.GameToken)
        self.GameTokenText.setObjectName(u"GameTokenText")
        self.GameTokenText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_14.addWidget(self.GameTokenText)

        self.GameTokenTextBox = QLineEdit(self.GameToken)
        self.GameTokenTextBox.setObjectName(u"GameTokenTextBox")
        self.GameTokenTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_14.addWidget(self.GameTokenTextBox)


        self.verticalLayout_2.addWidget(self.GameToken)

        self.SpectateToken = QFrame(self.AdvancedDetails)
        self.SpectateToken.setObjectName(u"SpectateToken")
        self.SpectateToken.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.SpectateToken.setFrameShape(QFrame.StyledPanel)
        self.SpectateToken.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.SpectateToken)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.SpectateTokeText = QLabel(self.SpectateToken)
        self.SpectateTokeText.setObjectName(u"SpectateTokeText")
        self.SpectateTokeText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_13.addWidget(self.SpectateTokeText)

        self.SpectateTokenTextBox = QLineEdit(self.SpectateToken)
        self.SpectateTokenTextBox.setObjectName(u"SpectateTokenTextBox")
        self.SpectateTokenTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_13.addWidget(self.SpectateTokenTextBox)


        self.verticalLayout_2.addWidget(self.SpectateToken)

        self.Note = QLabel(self.AdvancedPage)
        self.Note.setObjectName(u"Note")
        self.Note.setGeometry(QRect(10, 290, 493, 23))
        self.Note.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 63 italic 12pt \"Open Sans\";")
        self.Pages.addWidget(self.AdvancedPage)
        self.ButtonsPage = QWidget()
        self.ButtonsPage.setObjectName(u"ButtonsPage")
        self.ButtonsTitle = QLabel(self.ButtonsPage)
        self.ButtonsTitle.setObjectName(u"ButtonsTitle")
        self.ButtonsTitle.setGeometry(QRect(180, 30, 141, 23))
        self.ButtonsTitle.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 14pt \"Raleway\";")
        self.ButtonsToMain = QPushButton(self.ButtonsPage)
        self.ButtonsToMain.setObjectName(u"ButtonsToMain")
        self.ButtonsToMain.setGeometry(QRect(30, 20, 81, 41))
        self.ButtonsToMain.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonsToMain.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")
        self.ButtonsToMain.setIcon(icon2)
        self.ButtonsToMain.setIconSize(QSize(20, 20))
        self.ButtonDetails = QFrame(self.ButtonsPage)
        self.ButtonDetails.setObjectName(u"ButtonDetails")
        self.ButtonDetails.setGeometry(QRect(29, 79, 431, 301))
        self.ButtonDetails.setStyleSheet(u"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));")
        self.ButtonDetails.setFrameShape(QFrame.StyledPanel)
        self.ButtonDetails.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.ButtonDetails)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.FirstButtonFrame = QFrame(self.ButtonDetails)
        self.FirstButtonFrame.setObjectName(u"FirstButtonFrame")
        self.FirstButtonFrame.setStyleSheet(u"border:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));")
        self.FirstButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.FirstButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.FirstButtonFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.FirstButton = QFrame(self.FirstButtonFrame)
        self.FirstButton.setObjectName(u"FirstButton")
        self.FirstButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.FirstButton.setFrameShape(QFrame.StyledPanel)
        self.FirstButton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.FirstButton)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.FirstButtonText = QLabel(self.FirstButton)
        self.FirstButtonText.setObjectName(u"FirstButtonText")
        self.FirstButtonText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_18.addWidget(self.FirstButtonText)

        self.FirstButtonTextBox = QLineEdit(self.FirstButton)
        self.FirstButtonTextBox.setObjectName(u"FirstButtonTextBox")
        self.FirstButtonTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_18.addWidget(self.FirstButtonTextBox)


        self.verticalLayout_4.addWidget(self.FirstButton)

        self.FirstButtonLinkFrame = QFrame(self.FirstButtonFrame)
        self.FirstButtonLinkFrame.setObjectName(u"FirstButtonLinkFrame")
        self.FirstButtonLinkFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.FirstButtonLinkFrame.setFrameShape(QFrame.StyledPanel)
        self.FirstButtonLinkFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.FirstButtonLinkFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.FirstButtonLinkText = QLabel(self.FirstButtonLinkFrame)
        self.FirstButtonLinkText.setObjectName(u"FirstButtonLinkText")
        self.FirstButtonLinkText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_19.addWidget(self.FirstButtonLinkText)

        self.FirstButtonLinkTextBox = QLineEdit(self.FirstButtonLinkFrame)
        self.FirstButtonLinkTextBox.setObjectName(u"FirstButtonLinkTextBox")
        self.FirstButtonLinkTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_19.addWidget(self.FirstButtonLinkTextBox)


        self.verticalLayout_4.addWidget(self.FirstButtonLinkFrame)


        self.verticalLayout_5.addWidget(self.FirstButtonFrame)

        self.SecondButtonFrame = QFrame(self.ButtonDetails)
        self.SecondButtonFrame.setObjectName(u"SecondButtonFrame")
        self.SecondButtonFrame.setStyleSheet(u"border:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));")
        self.SecondButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.SecondButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.SecondButtonFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SecondButton = QFrame(self.SecondButtonFrame)
        self.SecondButton.setObjectName(u"SecondButton")
        self.SecondButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.SecondButton.setFrameShape(QFrame.StyledPanel)
        self.SecondButton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.SecondButton)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.SecondButtonText = QLabel(self.SecondButton)
        self.SecondButtonText.setObjectName(u"SecondButtonText")
        self.SecondButtonText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_15.addWidget(self.SecondButtonText)

        self.SecondButtonTextBox = QLineEdit(self.SecondButton)
        self.SecondButtonTextBox.setObjectName(u"SecondButtonTextBox")
        self.SecondButtonTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_15.addWidget(self.SecondButtonTextBox)


        self.verticalLayout_3.addWidget(self.SecondButton)

        self.SecondButtonLinkFrame = QFrame(self.SecondButtonFrame)
        self.SecondButtonLinkFrame.setObjectName(u"SecondButtonLinkFrame")
        self.SecondButtonLinkFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:None;")
        self.SecondButtonLinkFrame.setFrameShape(QFrame.StyledPanel)
        self.SecondButtonLinkFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.SecondButtonLinkFrame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.SecondButtonLinkText = QLabel(self.SecondButtonLinkFrame)
        self.SecondButtonLinkText.setObjectName(u"SecondButtonLinkText")
        self.SecondButtonLinkText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Roboto\";")

        self.horizontalLayout_17.addWidget(self.SecondButtonLinkText)

        self.SecondButtonLinkTextBox = QLineEdit(self.SecondButtonLinkFrame)
        self.SecondButtonLinkTextBox.setObjectName(u"SecondButtonLinkTextBox")
        self.SecondButtonLinkTextBox.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"padding:2px;\n"
"border-radius:4px;")

        self.horizontalLayout_17.addWidget(self.SecondButtonLinkTextBox)


        self.verticalLayout_3.addWidget(self.SecondButtonLinkFrame)


        self.verticalLayout_5.addWidget(self.SecondButtonFrame)

        self.Pages.addWidget(self.ButtonsPage)
        self.HumanToEpoch = QWidget()
        self.HumanToEpoch.setObjectName(u"HumanToEpoch")
        self.EpochTitle = QLabel(self.HumanToEpoch)
        self.EpochTitle.setObjectName(u"EpochTitle")
        self.EpochTitle.setGeometry(QRect(170, 20, 148, 23))
        self.EpochTitle.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 14pt \"Raleway\";")
        self.EpochInfo = QLabel(self.HumanToEpoch)
        self.EpochInfo.setObjectName(u"EpochInfo")
        self.EpochInfo.setGeometry(QRect(80, 70, 321, 37))
        self.EpochInfo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Raleway\";")
        self.Selector = QFrame(self.HumanToEpoch)
        self.Selector.setObjectName(u"Selector")
        self.Selector.setGeometry(QRect(90, 170, 321, 71))
        self.Selector.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:none;\n"
"}\n"
"QComboBox{\n"
"color:rgb(246, 245, 244);\n"
"}")
        self.Selector.setFrameShape(QFrame.StyledPanel)
        self.Selector.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Selector)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Hour = QComboBox(self.Selector)
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.addItem("")
        self.Hour.setObjectName(u"Hour")

        self.horizontalLayout_16.addWidget(self.Hour)

        self.Minute = QComboBox(self.Selector)
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.addItem("")
        self.Minute.setObjectName(u"Minute")

        self.horizontalLayout_16.addWidget(self.Minute)

        self.Second = QComboBox(self.Selector)
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.addItem("")
        self.Second.setObjectName(u"Second")

        self.horizontalLayout_16.addWidget(self.Second)

        self.indicator = QLabel(self.HumanToEpoch)
        self.indicator.setObjectName(u"indicator")
        self.indicator.setGeometry(QRect(100, 150, 301, 19))
        self.indicator.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 11pt \"Raleway\";")
        self.EpochToMain = QPushButton(self.HumanToEpoch)
        self.EpochToMain.setObjectName(u"EpochToMain")
        self.EpochToMain.setGeometry(QRect(20, 20, 81, 41))
        self.EpochToMain.setCursor(QCursor(Qt.PointingHandCursor))
        self.EpochToMain.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")
        self.EpochToMain.setIcon(icon2)
        self.EpochToMain.setIconSize(QSize(20, 20))
        self.ConvertButton = QPushButton(self.HumanToEpoch)
        self.ConvertButton.setObjectName(u"ConvertButton")
        self.ConvertButton.setGeometry(QRect(180, 340, 111, 31))
        self.ConvertButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ConvertButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"color:rgb(0, 0, 0);\n"
"font: 9pt \"Roboto\";")
        self.ConvertButton.setIconSize(QSize(20, 20))
        self.EpochResult = QLineEdit(self.HumanToEpoch)
        self.EpochResult.setObjectName(u"EpochResult")
        self.EpochResult.setGeometry(QRect(102, 281, 291, 31))
        self.EpochResult.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:none;")
        self.EpochResult.setEchoMode(QLineEdit.Normal)
        self.EpochResult.setReadOnly(True)
        self.Pages.addWidget(self.HumanToEpoch)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.MainTitle.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This is the app that allows you to change your rich presence easyly with GUI.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.MainTitle.setText(QCoreApplication.translate("MainWindow", u"Custom Rich Presence", None))
        self.IDText.setText(QCoreApplication.translate("MainWindow", u"ID of RP Application:", None))
#if QT_CONFIG(whatsthis)
        self.IDTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.IDTextBox.setText("")
        self.StatusText.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
#if QT_CONFIG(whatsthis)
        self.StatusTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.StatusTextBox.setText("")
        self.DetailsText.setText(QCoreApplication.translate("MainWindow", u"Details:", None))
#if QT_CONFIG(whatsthis)
        self.DetailsTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.DetailsTextBox.setText("")
        self.StartTimeText.setText(QCoreApplication.translate("MainWindow", u"Start time:", None))
#if QT_CONFIG(whatsthis)
        self.StartTimeTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.StartTimeTextBox.setText("")
        self.EndTimeText.setText(QCoreApplication.translate("MainWindow", u"End time:", None))
#if QT_CONFIG(whatsthis)
        self.EndTimeTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EndTimeTextBox.setText("")
        self.LargeImageText.setText(QCoreApplication.translate("MainWindow", u"Large image's name:", None))
#if QT_CONFIG(whatsthis)
        self.LargeImageTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.LargeImageTextBox.setText("")
        self.LargeImageTooltipText.setText(QCoreApplication.translate("MainWindow", u"Large image's info(Tooltip)", None))
#if QT_CONFIG(whatsthis)
        self.LargeImageTooltipTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.LargeImageTooltipTextBox.setText("")
        self.SmallImageText.setText(QCoreApplication.translate("MainWindow", u"Small image's name:", None))
#if QT_CONFIG(whatsthis)
        self.SmallImageTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.SmallImageTextBox.setText("")
        self.SmallImageTooltipText.setText(QCoreApplication.translate("MainWindow", u"Small image's info(Tooltip)", None))
#if QT_CONFIG(whatsthis)
        self.SmallImageTooltipTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.SmallImageTooltipTextBox.setText("")
        self.CustomButtons.setText(QCoreApplication.translate("MainWindow", u"Custom Buttons", None))
        self.StartStop.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.MainToEpoch.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.Advanced.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.AdvancedTitle.setText(QCoreApplication.translate("MainWindow", u"Advanced Settings", None))
        self.AdvancedToMain.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.PartyIDText.setText(QCoreApplication.translate("MainWindow", u"Party ID of room/lobby:", None))
#if QT_CONFIG(whatsthis)
        self.PartyIDTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PartyIDTextBox.setText("")
        self.PartySizeText.setText(QCoreApplication.translate("MainWindow", u"Party size", None))
#if QT_CONFIG(whatsthis)
        self.PartySizeTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.PartySizeTextBox.setText("")
        self.ChatTokeText.setText(QCoreApplication.translate("MainWindow", u"Link or token for joining(Chats):", None))
#if QT_CONFIG(whatsthis)
        self.ChatTokenTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ChatTokenTextBox.setText("")
        self.GameTokenText.setText(QCoreApplication.translate("MainWindow", u"Link or token for joining(Games):", None))
#if QT_CONFIG(whatsthis)
        self.GameTokenTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.GameTokenTextBox.setText("")
        self.SpectateTokeText.setText(QCoreApplication.translate("MainWindow", u"Link or token for spectating:", None))
#if QT_CONFIG(whatsthis)
        self.SpectateTokenTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.SpectateTokenTextBox.setText("")
        self.Note.setText(QCoreApplication.translate("MainWindow", u"Note:If you set these buttons,then you will not able to set custom buttons.", None))
        self.ButtonsTitle.setText(QCoreApplication.translate("MainWindow", u"Custom buttons", None))
        self.ButtonsToMain.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.FirstButtonText.setText(QCoreApplication.translate("MainWindow", u"First custom button:", None))
#if QT_CONFIG(whatsthis)
        self.FirstButtonTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FirstButtonTextBox.setText("")
        self.FirstButtonLinkText.setText(QCoreApplication.translate("MainWindow", u"Link of custom button:", None))
#if QT_CONFIG(whatsthis)
        self.FirstButtonLinkTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FirstButtonLinkTextBox.setText("")
        self.SecondButtonText.setText(QCoreApplication.translate("MainWindow", u"Second custom button:", None))
#if QT_CONFIG(whatsthis)
        self.SecondButtonTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.SecondButtonTextBox.setText("")
        self.SecondButtonLinkText.setText(QCoreApplication.translate("MainWindow", u"Link of custom button:", None))
#if QT_CONFIG(whatsthis)
        self.SecondButtonLinkTextBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Can be empty</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.SecondButtonLinkTextBox.setText("")
        self.EpochTitle.setText(QCoreApplication.translate("MainWindow", u"Epoch Converter", None))
        self.EpochInfo.setText(QCoreApplication.translate("MainWindow", u"This converts human time to Epoch(Unix) time. \n"
"You will use it in start time and end time.", None))
        self.Hour.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.Hour.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.Hour.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.Hour.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.Hour.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.Hour.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.Hour.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.Hour.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.Hour.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.Hour.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.Hour.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.Hour.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.Hour.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.Hour.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.Hour.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.Hour.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.Hour.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.Hour.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.Hour.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.Hour.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.Hour.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))
        self.Hour.setItemText(21, QCoreApplication.translate("MainWindow", u"21", None))
        self.Hour.setItemText(22, QCoreApplication.translate("MainWindow", u"22", None))
        self.Hour.setItemText(23, QCoreApplication.translate("MainWindow", u"23", None))

        self.Minute.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.Minute.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.Minute.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.Minute.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.Minute.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.Minute.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.Minute.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.Minute.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.Minute.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.Minute.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.Minute.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.Minute.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.Minute.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.Minute.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.Minute.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.Minute.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.Minute.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.Minute.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.Minute.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.Minute.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.Minute.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))
        self.Minute.setItemText(21, QCoreApplication.translate("MainWindow", u"21", None))
        self.Minute.setItemText(22, QCoreApplication.translate("MainWindow", u"22", None))
        self.Minute.setItemText(23, QCoreApplication.translate("MainWindow", u"23", None))
        self.Minute.setItemText(24, QCoreApplication.translate("MainWindow", u"24", None))
        self.Minute.setItemText(25, QCoreApplication.translate("MainWindow", u"25", None))
        self.Minute.setItemText(26, QCoreApplication.translate("MainWindow", u"26", None))
        self.Minute.setItemText(27, QCoreApplication.translate("MainWindow", u"27", None))
        self.Minute.setItemText(28, QCoreApplication.translate("MainWindow", u"28", None))
        self.Minute.setItemText(29, QCoreApplication.translate("MainWindow", u"29", None))
        self.Minute.setItemText(30, QCoreApplication.translate("MainWindow", u"30", None))
        self.Minute.setItemText(31, QCoreApplication.translate("MainWindow", u"31", None))
        self.Minute.setItemText(32, QCoreApplication.translate("MainWindow", u"32", None))
        self.Minute.setItemText(33, QCoreApplication.translate("MainWindow", u"33", None))
        self.Minute.setItemText(34, QCoreApplication.translate("MainWindow", u"34", None))
        self.Minute.setItemText(35, QCoreApplication.translate("MainWindow", u"35", None))
        self.Minute.setItemText(36, QCoreApplication.translate("MainWindow", u"36", None))
        self.Minute.setItemText(37, QCoreApplication.translate("MainWindow", u"37", None))
        self.Minute.setItemText(38, QCoreApplication.translate("MainWindow", u"38", None))
        self.Minute.setItemText(39, QCoreApplication.translate("MainWindow", u"39", None))
        self.Minute.setItemText(40, QCoreApplication.translate("MainWindow", u"40", None))
        self.Minute.setItemText(41, QCoreApplication.translate("MainWindow", u"41", None))
        self.Minute.setItemText(42, QCoreApplication.translate("MainWindow", u"42", None))
        self.Minute.setItemText(43, QCoreApplication.translate("MainWindow", u"43", None))
        self.Minute.setItemText(44, QCoreApplication.translate("MainWindow", u"44", None))
        self.Minute.setItemText(45, QCoreApplication.translate("MainWindow", u"45", None))
        self.Minute.setItemText(46, QCoreApplication.translate("MainWindow", u"46", None))
        self.Minute.setItemText(47, QCoreApplication.translate("MainWindow", u"47", None))
        self.Minute.setItemText(48, QCoreApplication.translate("MainWindow", u"48", None))
        self.Minute.setItemText(49, QCoreApplication.translate("MainWindow", u"49", None))
        self.Minute.setItemText(50, QCoreApplication.translate("MainWindow", u"50", None))
        self.Minute.setItemText(51, QCoreApplication.translate("MainWindow", u"51", None))
        self.Minute.setItemText(52, QCoreApplication.translate("MainWindow", u"52", None))
        self.Minute.setItemText(53, QCoreApplication.translate("MainWindow", u"53", None))
        self.Minute.setItemText(54, QCoreApplication.translate("MainWindow", u"54", None))
        self.Minute.setItemText(55, QCoreApplication.translate("MainWindow", u"55", None))
        self.Minute.setItemText(56, QCoreApplication.translate("MainWindow", u"56", None))
        self.Minute.setItemText(57, QCoreApplication.translate("MainWindow", u"57", None))
        self.Minute.setItemText(58, QCoreApplication.translate("MainWindow", u"58", None))
        self.Minute.setItemText(59, QCoreApplication.translate("MainWindow", u"59", None))

        self.Second.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.Second.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.Second.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.Second.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.Second.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.Second.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.Second.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.Second.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.Second.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.Second.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.Second.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.Second.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.Second.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.Second.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.Second.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.Second.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.Second.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.Second.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.Second.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.Second.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.Second.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))
        self.Second.setItemText(21, QCoreApplication.translate("MainWindow", u"21", None))
        self.Second.setItemText(22, QCoreApplication.translate("MainWindow", u"22", None))
        self.Second.setItemText(23, QCoreApplication.translate("MainWindow", u"23", None))
        self.Second.setItemText(24, QCoreApplication.translate("MainWindow", u"24", None))
        self.Second.setItemText(25, QCoreApplication.translate("MainWindow", u"25", None))
        self.Second.setItemText(26, QCoreApplication.translate("MainWindow", u"26", None))
        self.Second.setItemText(27, QCoreApplication.translate("MainWindow", u"27", None))
        self.Second.setItemText(28, QCoreApplication.translate("MainWindow", u"28", None))
        self.Second.setItemText(29, QCoreApplication.translate("MainWindow", u"29", None))
        self.Second.setItemText(30, QCoreApplication.translate("MainWindow", u"30", None))
        self.Second.setItemText(31, QCoreApplication.translate("MainWindow", u"31", None))
        self.Second.setItemText(32, QCoreApplication.translate("MainWindow", u"32", None))
        self.Second.setItemText(33, QCoreApplication.translate("MainWindow", u"33", None))
        self.Second.setItemText(34, QCoreApplication.translate("MainWindow", u"34", None))
        self.Second.setItemText(35, QCoreApplication.translate("MainWindow", u"35", None))
        self.Second.setItemText(36, QCoreApplication.translate("MainWindow", u"36", None))
        self.Second.setItemText(37, QCoreApplication.translate("MainWindow", u"37", None))
        self.Second.setItemText(38, QCoreApplication.translate("MainWindow", u"38", None))
        self.Second.setItemText(39, QCoreApplication.translate("MainWindow", u"39", None))
        self.Second.setItemText(40, QCoreApplication.translate("MainWindow", u"40", None))
        self.Second.setItemText(41, QCoreApplication.translate("MainWindow", u"41", None))
        self.Second.setItemText(42, QCoreApplication.translate("MainWindow", u"42", None))
        self.Second.setItemText(43, QCoreApplication.translate("MainWindow", u"43", None))
        self.Second.setItemText(44, QCoreApplication.translate("MainWindow", u"44", None))
        self.Second.setItemText(45, QCoreApplication.translate("MainWindow", u"45", None))
        self.Second.setItemText(46, QCoreApplication.translate("MainWindow", u"46", None))
        self.Second.setItemText(47, QCoreApplication.translate("MainWindow", u"47", None))
        self.Second.setItemText(48, QCoreApplication.translate("MainWindow", u"48", None))
        self.Second.setItemText(49, QCoreApplication.translate("MainWindow", u"49", None))
        self.Second.setItemText(50, QCoreApplication.translate("MainWindow", u"50", None))
        self.Second.setItemText(51, QCoreApplication.translate("MainWindow", u"51", None))
        self.Second.setItemText(52, QCoreApplication.translate("MainWindow", u"52", None))
        self.Second.setItemText(53, QCoreApplication.translate("MainWindow", u"53", None))
        self.Second.setItemText(54, QCoreApplication.translate("MainWindow", u"54", None))
        self.Second.setItemText(55, QCoreApplication.translate("MainWindow", u"55", None))
        self.Second.setItemText(56, QCoreApplication.translate("MainWindow", u"56", None))
        self.Second.setItemText(57, QCoreApplication.translate("MainWindow", u"57", None))
        self.Second.setItemText(58, QCoreApplication.translate("MainWindow", u"58", None))
        self.Second.setItemText(59, QCoreApplication.translate("MainWindow", u"59", None))

        self.indicator.setText(QCoreApplication.translate("MainWindow", u"Hour:               Minute:             Second:", None))
        self.EpochToMain.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.ConvertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.EpochResult.setText("")
    # retranslateUi

