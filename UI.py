# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
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
        self.Buttons.setGeometry(QRect(0, 461, 491, 61))
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
"font: 9pt \"Roboto\";")
        self.StartStop.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.StartStop)

        self.Apply = QPushButton(self.Buttons)
        self.Apply.setObjectName(u"Apply")
        self.Apply.setCursor(QCursor(Qt.PointingHandCursor))
        self.Apply.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 14px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
"font: 9pt \"Roboto\";")
        self.Apply.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.Apply)

        self.Advanced = QPushButton(self.Buttons)
        self.Advanced.setObjectName(u"Advanced")
        self.Advanced.setCursor(QCursor(Qt.PointingHandCursor))
        self.Advanced.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:rgb(0, 0, 0) ;\n"
"padding: 4px;\n"
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.MainTitle.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This is the app that allows you to change your rich presence easily with GUI.</p></body></html>", None))
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
        self.StartStop.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.Apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
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
    # retranslateUi

