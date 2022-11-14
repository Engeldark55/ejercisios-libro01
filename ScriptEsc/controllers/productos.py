from PySide6.QtWidgets import QWidget
from views.ui_producto import Ui_Form_producto as ui_Producto

class Producto_main(QWidget, ui_Producto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
