from PySide6.QtWidgets import QWidget
from views.ui_ventas import Ui_Form_ventas as ui_venta

class Venta_main(QWidget, ui_venta):
    def __init__(self):
        super().__init__()
        self.setupUi(self)