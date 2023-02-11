import sys
from random import randint
from functools import partial
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow  # فایل یوآی که تبدیل به فایل پایتونی کردیم

rand_number = randint(1, 50)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # همون فایل پایتونی بالااست
        self.ui.setupUi(self)
        self.ui.btn0.clicked.connect(partial(self.show_textbox, "0"))
        self.ui.btn1.clicked.connect(partial(self.show_textbox, "1"))
        self.ui.btn2.clicked.connect(partial(self.show_textbox, "2"))
        self.ui.btn3.clicked.connect(partial(self.show_textbox, "3"))
        self.ui.btn4.clicked.connect(partial(self.show_textbox, "4"))
        self.ui.btn5.clicked.connect(partial(self.show_textbox, "5"))
        self.ui.btn6.clicked.connect(partial(self.show_textbox, "6"))
        self.ui.btn7.clicked.connect(partial(self.show_textbox, "7"))
        self.ui.btn8.clicked.connect(partial(self.show_textbox, "8"))
        self.ui.btn9.clicked.connect(partial(self.show_textbox, "9"))
        
        self.ui.guess_btn.clicked.connect(self.user_number)

    def user_number(self):
         user_number = self.ui.text_box.text()
         self.Comparison(user_number)
        

    def show_textbox(self, num):
        if self.ui.text_box.text() == "برو پایین" or self.ui.text_box.text() == "برو بالا" or self.ui.text_box.text() == "تبریک * شما برنده شدید" :
                self.ui.text_box.setText("")
        self.ui.text_box.setText(self.ui.text_box.text()+num)

    def Comparison(self, user_number):
        if rand_number > int(user_number) :
            self.ui.text_box.setAlignment(Qt.AlignHCenter)     
            self.ui.text_box.setText("برو بالا")
       
        elif rand_number < int(user_number) : 
            self.ui.text_box.setAlignment(Qt.AlignHCenter)     
            self.ui.text_box.setText("برو پایین")
        
        elif rand_number == int(user_number) :    
            self.ui.text_box.setAlignment(Qt.AlignHCenter)     
            self.ui.text_box.setText("تبریک * شما برنده شدید")

app = QApplication(sys.argv)    
 
main_window = MainWindow()
main_window.show()



app.exec()