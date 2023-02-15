import sys
import string
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import *   # برای وسطچین کردن متن
from main_ui import Ui_MainWindow  # فایل یوآی که تبدیل به فایل پایتونی کردیم

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # همون فایل پایتونی بالااست
        self.ui.setupUi(self)
        self.ui.textbox_password.setAlignment(Qt.AlignHCenter) # برای وسطچین کردن متن 
        self.ui.ganerate_btn.clicked.connect(self.generate_password)

    def generate_password(self):
        if self.ui.textbox_password.text() != "":
             self.ui.textbox_password.setText("")

        uppercase_character = random.choice(string.ascii_uppercase)
        rand_number = random.randint(0, 9)
        special_character = random.choice(string.punctuation)
        
        if self.ui.radio_btn_standard.isChecked():  #حالت استاندارد هشت کاراکتر
            password_list = [uppercase_character, rand_number, special_character]  # لیست شامل حرف بزرگ و عددرندم و کاراکتر سیمبل
            for password in password_list: #برای حرف  بزرگ و عدد رندم و کاراکتر سیمبل
                self.ui.textbox_password.setText(self.ui.textbox_password.text()+str(password))

            for i in range(1, 6):     # برای پنج تا کاراکتر حروف کوچک
                self.ui.textbox_password.setText(self.ui.textbox_password.text()+random.choice(string.ascii_lowercase))
                    
        if self.ui.radio_btn_extra.isChecked():  #حالت استاندارد دوازده کاراکتر
            password_list = [uppercase_character, rand_number, special_character, rand_number+1]  # لیست شامل حرف بزرگ و عددرندم و کاراکتر سیمبل
            for password in password_list: #برای حرف  بزرگ و عدد رندم و کاراکتر سیمبل
                self.ui.textbox_password.setText(self.ui.textbox_password.text()+str(password))

            for i in range(1, 9):     # برای هشت تا کاراکتر حروف کوچک
                self.ui.textbox_password.setText(self.ui.textbox_password.text()+random.choice(string.ascii_lowercase))
                                
        if self.ui.radio_btn_super.isChecked():  #حالت استاندارد بیست کاراکتر
            password_list = [uppercase_character, rand_number, special_character, rand_number+1, rand_number+2]  # لیست شامل حرف بزرگ و عددرندم و کاراکتر سیمبل
            for password in password_list: #برای حرف  بزرگ و عدد رندم و کاراکتر سیمبل
                self.ui.textbox_password.setText(self.ui.textbox_password.text()+str(password))

            for i in range(1, 16):     # برای پانزده تا کاراکتر حروف کوچک
                self.ui.textbox_password.setText(self.ui.textbox_password.text()+random.choice(string.ascii_lowercase))
                                            
app = QApplication(sys.argv)    
 
main_window = MainWindow()
main_window.show()



app.exec()