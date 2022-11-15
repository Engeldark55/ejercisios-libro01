from PySide6.QtWidgets import QWidget
from views.ui_producto import Ui_Form_producto as ui_Producto

from  db.metodos import insert_prod as add_pro_new

class Producto_main(QWidget, ui_Producto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #boton add
        self.btn_agregar.clicked.connect(lambda: self.add_pro())
        #boton crete_code
        self.btn_crear.clicked.connect(lambda: self.create_codo())
        #btn cancel
        self.btn_cancelar.clicked.connect(lambda: self.limpiar_cancel())
        
        #opc del combobox
        self.comboBox_tipo.addItems(["antiviotico", "analgecico", "patente" , "cimilar"])
       
    def add_pro(self):
        
        clave: str = self.line_calve.text()
        nombre: str = self.line_nombre.text()
        cantidad_pro: float = self.line_cantidad_pro.text()
        tipo = 0
        pre_compra: float = self.line_precio_com.text()
        pre_venta: float = self.line_precio_venta.text()
        description: str = self.line_desc.text()
        fecha: str ="25/25/99"
        data_pro = [clave,nombre,cantidad_pro,tipo,pre_compra,pre_venta,description, fecha]

        add_pro_new(data_pro)

        print(data_pro) 
        
    def create_codo(self):
        
        clave_code = self.line_clave.text()
        cantidad_cod = self.line_cantidad.text()
        
        data_cod = [clave_code, cantidad_cod]
        
        print(data_cod)
        
    
  

    def limpiar_cancel(self):
        clave = self.line_calve.clear()
        nombre = self.line_nombre.clear()
        cantidad_pro = self.line_cantidad_pro.clear()
        pre_compra = self.line_precio_com.clear()
        pre_venta = self.line_precio_venta.clear()
        description = self.line_desc.clear()
        
        clave_code = self.line_clave.clear()
        cantidad_cod = self.line_cantidad.clear()
        
        