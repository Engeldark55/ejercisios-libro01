from PySide6.QtWidgets import QWidget
from views.ui_empleado import Ui_Form_empleado as ui_empleado

class Empleado_main(QWidget, ui_empleado):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        