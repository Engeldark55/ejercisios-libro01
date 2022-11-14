from PySide6.QtWidgets import QWidget
from views.ui_Login import Ui_Form_log as ui_login

class Login_main(QWidget, ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)