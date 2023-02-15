# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(562, 416)
        MainWindow.setStyleSheet(u"background-color: rgb(173, 170, 244);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 30, 521, 331))
        self.frame.setStyleSheet(u"\n"
"border-radius:20;\n"
"border: 2px solid ;\n"
"border-color: rgb(153, 153, 153);\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.radio_btn_standard = QRadioButton(self.frame)
        self.radio_btn_standard.setObjectName(u"radio_btn_standard")
        self.radio_btn_standard.setGeometry(QRect(20, 20, 391, 20))
        self.radio_btn_standard.setStyleSheet(u"border-color: rgb(173, 170, 244);")
        self.radio_btn_standard.setCheckable(True)
        self.radio_btn_standard.setChecked(False)
        self.radio_btn_extra = QRadioButton(self.frame)
        self.radio_btn_extra.setObjectName(u"radio_btn_extra")
        self.radio_btn_extra.setGeometry(QRect(20, 80, 361, 20))
        self.radio_btn_extra.setStyleSheet(u"border-color: rgb(173, 170, 244);")
        self.radio_btn_super = QRadioButton(self.frame)
        self.radio_btn_super.setObjectName(u"radio_btn_super")
        self.radio_btn_super.setGeometry(QRect(20, 140, 421, 20))
        self.radio_btn_super.setStyleSheet(u"border-color: rgb(173, 170, 244);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 40, 471, 22))
        self.lineEdit.setStyleSheet(u"border-color: rgb(173, 170, 244);")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 100, 471, 22))
        self.lineEdit_2.setStyleSheet(u"border-color: rgb(173, 170, 244);")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(40, 160, 471, 22))
        self.lineEdit_3.setStyleSheet(u"border-color: rgb(173, 170, 244);")
        self.ganerate_btn = QPushButton(self.frame)
        self.ganerate_btn.setObjectName(u"ganerate_btn")
        self.ganerate_btn.setGeometry(QRect(190, 210, 131, 41))
        self.ganerate_btn.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"border-radius:15px;\n"
"")
        self.textbox_password = QLineEdit(self.frame)
        self.textbox_password.setObjectName(u"textbox_password")
        self.textbox_password.setGeometry(QRect(40, 270, 441, 41))
        font = QFont()
        font.setPointSize(14)
        self.textbox_password.setFont(font)
        self.textbox_password.setStyleSheet(u"border-color: rgb(0, 68, 100);\n"
"color: rgb(0, 68, 100);\n"
"border-radius:10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 562, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"password_generator", None))
        self.radio_btn_standard.setText(QCoreApplication.translate("MainWindow", u"Generate a Standard Strength Password", None))
        self.radio_btn_extra.setText(QCoreApplication.translate("MainWindow", u"Generate an Extra Strong Password", None))
        self.radio_btn_super.setText(QCoreApplication.translate("MainWindow", u"Generate a Super Strong Password", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"(8 characters long including a number, a special character and an uppercase letter)", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"(12 characters long with multiple numbers, special characters and uppercase letters)  ", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"(20 characters long with multiple numbers, special characters and uppercase letters)  ", None))
        self.ganerate_btn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.textbox_password.setText("")
    # retranslateUi

