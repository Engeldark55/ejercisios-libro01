from PySide6.QtWidgets import QWidget
from views.ui_empleado import Ui_Form_empleado as ui_empleado

class Empleado_main(QWidget, ui_empleado):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #boton 
        self.btn_agregar.clicked.connect(lambda: self.add_empleado())
        
    def add_empleado(self):
        
        clave_emp = self.line_clave_empleado.text()
        nombre_comp = self.line_nombreCompleto.text()
        edad = self.line_edad.text()
        
        ine = self.line_ine.text()
        domicilio = self.line_domicilio.text()
        contrato = self.line_contrato.text()
        
        sueldo = self.line_sueldo.text()
        horario = self.line_horario.text()
        
        data_form = [clave_emp, nombre_comp, edad, ine, domicilio, contrato, sueldo, horario]
        
        print(data_form)
        
        