# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(329, 362)
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei UI"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(59, 33, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text_box = QLineEdit(self.centralwidget)
        self.text_box.setObjectName(u"text_box")
        self.text_box.setGeometry(QRect(10, 10, 301, 41))
        self.text_box.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(169, 215, 255);\n"
"color: rgb(0, 0, 0);\n"
"border:3px solid;\n"
"")
        self.guess_btn = QPushButton(self.centralwidget)
        self.guess_btn.setObjectName(u"guess_btn")
        self.guess_btn.setGeometry(QRect(40, 270, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.guess_btn.setFont(font1)
        self.guess_btn.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(255, 255, 127);\n"
"\n"
"border:3px solid rgb(255, 85, 127);\n"
"\n"
"background-color: rgb(85, 0, 127);\n"
"")
        self.btn0 = QPushButton(self.centralwidget)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setGeometry(QRect(130, 210, 41, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(18)
        self.btn0.setFont(font2)
        self.btn0.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setGeometry(QRect(180, 160, 41, 41))
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(20)
        self.btn3.setFont(font3)
        self.btn3.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setGeometry(QRect(80, 60, 41, 41))
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        self.btn7.setFont(font2)
        self.btn7.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setGeometry(QRect(130, 60, 41, 41))
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        self.btn8.setFont(font2)
        self.btn8.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setGeometry(QRect(180, 60, 41, 41))
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        self.btn9.setFont(font2)
        self.btn9.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setGeometry(QRect(80, 110, 41, 41))
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setFont(font2)
        self.btn4.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setGeometry(QRect(130, 110, 41, 41))
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setFont(font2)
        self.btn5.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(80, 160, 41, 41))
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setFont(font2)
        self.btn1.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setGeometry(QRect(180, 110, 41, 41))
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        self.btn6.setFont(font2)
        self.btn6.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(130, 160, 41, 41))
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setFont(font2)
        self.btn2.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(0, 0, 127);\n"
"\n"
"border:3px solid ;\n"
"background-color: rgb(170, 255, 0);\n"
"hover {\n"
"  color: red;\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 329, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Guess Number", None))
        self.text_box.setText("")
        self.guess_btn.setText(QCoreApplication.translate("MainWindow", u"Guess", None))
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
    # retranslateUi

