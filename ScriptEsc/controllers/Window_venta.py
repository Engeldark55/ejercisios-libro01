from PySide6.QtWidgets import QWidget
from views.ui_venta_emp import Ui_Main_form as win__venta_emp

class Window_emp_venta(QWidget, win__venta_emp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)