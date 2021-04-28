# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Layout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(425, 362)
        MainWindow.setMaximumSize(QSize(425, 500))
        MainWindow.setBaseSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u":/newPrefix/Cal.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.990000000000000)
        MainWindow.setStyleSheet(u"@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;500;600&display=swap');\n"
"*{\n"
"  padding: 0;\n"
"  margin: 0%;\n"
"  outline:  none;/*tirar celesao dquando ao o click*/\n"
"  font-family: 'Roboto',sans-serif;\n"
"  font-size: 18px;\n"
"  font-weight: 500;\n"
"background-color: rgb(37, 4, 68);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(185, 185, 185);\n"
"	border-radius: 3px;\n"
"	border: none;\n"
"	 width: 100px;\n"
"  height: 50px;\n"
"\n"
"}\n"
"QPushButton#Buttonigu{\n"
" background-color: rgb(59, 56, 230);\n"
"}\n"
"QPushButton#Buttonigu:hover{\n"
"	background-color: rgb(35, 34, 138);\n"
"}\n"
"QPushButton#Buttoncle{\n"
" border-bottom-left-radius: 35px;  \n"
"background-color: rgb(194, 49, 12);\n"
"}\n"
"QPushButton#Buttoncle:hover{\n"
"	background-color:  rgb(180, 40, 10);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(140, 140, 140);\n"
"}\n"
"QPushButton:pressed, QPushButton#Buttoncle:pressed, QPushButton#Buttonigu:pressed{\n"
"	background-color: rgba(140, "
                        "140, 140,50);\n"
"}\n"
"QLineEdit{\n"
"width: calc(100% - 4px);\n"
"height: 40%;\n"
"background-color: rgb(245, 245, 245);\n"
"border-radius: 3px;\n"
"border: none;\n"
"  margin-top: 15%;\n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 3, -1, 10)
        self.Buttonmas = QPushButton(self.centralwidget)
        self.Buttonmas.setObjectName(u"Buttonmas")
        self.Buttonmas.setCursor(QCursor(Qt.PointingHandCursor))
        self.Buttonmas.setStyleSheet(u"*{\n"
" border-bottom-right-radius: 35px; \n"
"}")

        self.gridLayout_2.addWidget(self.Buttonmas, 3, 3, 1, 1)

        self.Buttonmul = QPushButton(self.centralwidget)
        self.Buttonmul.setObjectName(u"Buttonmul")
        self.Buttonmul.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Buttonmul, 1, 3, 1, 1)

        self.Button1 = QPushButton(self.centralwidget)
        self.Button1.setObjectName(u"Button1")
        self.Button1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button1, 2, 0, 1, 1)

        self.Button4 = QPushButton(self.centralwidget)
        self.Button4.setObjectName(u"Button4")
        self.Button4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button4, 1, 0, 1, 1)

        self.Button9 = QPushButton(self.centralwidget)
        self.Button9.setObjectName(u"Button9")
        self.Button9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button9, 0, 2, 1, 1)

        self.Buttondiv = QPushButton(self.centralwidget)
        self.Buttondiv.setObjectName(u"Buttondiv")
        self.Buttondiv.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Buttondiv, 0, 3, 1, 1)

        self.Button3 = QPushButton(self.centralwidget)
        self.Button3.setObjectName(u"Button3")
        self.Button3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button3, 2, 2, 1, 1)

        self.Button7 = QPushButton(self.centralwidget)
        self.Button7.setObjectName(u"Button7")
        self.Button7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button7, 0, 0, 1, 1)

        self.Button6 = QPushButton(self.centralwidget)
        self.Button6.setObjectName(u"Button6")
        self.Button6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button6, 1, 2, 1, 1)

        self.Button8 = QPushButton(self.centralwidget)
        self.Button8.setObjectName(u"Button8")
        self.Button8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button8, 0, 1, 1, 1)

        self.Buttoncle = QPushButton(self.centralwidget)
        self.Buttoncle.setObjectName(u"Buttoncle")
        self.Buttoncle.setCursor(QCursor(Qt.PointingHandCursor))
        self.Buttoncle.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.Buttoncle, 3, 0, 1, 1)

        self.Button5 = QPushButton(self.centralwidget)
        self.Button5.setObjectName(u"Button5")
        self.Button5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button5, 1, 1, 1, 1)

        self.Buttonmen = QPushButton(self.centralwidget)
        self.Buttonmen.setObjectName(u"Buttonmen")
        self.Buttonmen.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Buttonmen, 2, 3, 1, 1)

        self.Button0 = QPushButton(self.centralwidget)
        self.Button0.setObjectName(u"Button0")
        self.Button0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button0, 3, 1, 1, 1)

        self.Button2 = QPushButton(self.centralwidget)
        self.Button2.setObjectName(u"Button2")
        self.Button2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Button2, 2, 1, 1, 1)

        self.Buttonigu = QPushButton(self.centralwidget)
        self.Buttonigu.setObjectName(u"Buttonigu")
        self.Buttonigu.setCursor(QCursor(Qt.PointingHandCursor))
        self.Buttonigu.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.Buttonigu, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Buttoncle, self.Button0)
        QWidget.setTabOrder(self.Button0, self.Buttonigu)
        QWidget.setTabOrder(self.Buttonigu, self.Buttonmas)
        QWidget.setTabOrder(self.Buttonmas, self.Button1)
        QWidget.setTabOrder(self.Button1, self.Button2)
        QWidget.setTabOrder(self.Button2, self.Button3)
        QWidget.setTabOrder(self.Button3, self.Buttonmen)
        QWidget.setTabOrder(self.Buttonmen, self.Button4)
        QWidget.setTabOrder(self.Button4, self.Button5)
        QWidget.setTabOrder(self.Button5, self.Button6)
        QWidget.setTabOrder(self.Button6, self.Buttonmul)
        QWidget.setTabOrder(self.Buttonmul, self.Button7)
        QWidget.setTabOrder(self.Button7, self.Button8)
        QWidget.setTabOrder(self.Button8, self.Button9)
        QWidget.setTabOrder(self.Button9, self.Buttondiv)
        QWidget.setTabOrder(self.Buttondiv, self.lineEdit)

        self.retranslateUi(MainWindow)
        self.Buttoncle.clicked.connect(self.lineEdit.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Buttonmas.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Buttonmul.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.Button1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Button4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Button9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Buttondiv.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.Button3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Button7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Button6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Button8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Buttoncle.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Button5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Buttonmen.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Button0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Buttonigu.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

