from PySide6.QtWidgets import QWidget
from views.ui_Login import Ui_Form_log as ui_login

class Login_main(QWidget, ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #btn acceder    
        self.pushButton.clicked.connect(lambda: self.cap_data())
        
    def cap_data(self):
        user_name = self.lineEdit.text()
        pasword = self.lineEdit_2.text()
        data_log = [user_name, pasword]
        print(data_log)