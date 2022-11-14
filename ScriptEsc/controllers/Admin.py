from PySide6.QtWidgets import QWidget
from views.ui_admin import Ui_Form_main as ui_Admin
from .productos import Producto_main
from .Empleado import Empleado_main
from .Ventas import Venta_main

class AdminMain(QWidget, ui_Admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        window_producto = Producto_main()
        window_empleado = Empleado_main()
        window_venta = Venta_main()
        
        #titulo
        self.label_titulo.setText('Tienda - Moreno')
        #boton open productos
        self.btn_productos.clicked.connect(lambda: window_producto.show())
        #boton open empleados
        self.btn_personal.clicked.connect(lambda: window_empleado.show())
        #boton open ventas
        self.btn_ventas.clicked.connect(lambda: window_venta.show())
    