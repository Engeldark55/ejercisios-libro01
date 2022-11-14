from PySide6.QtWidgets import QApplication
from controllers.Admin import AdminMain as Admin
from controllers.Window_venta import win__venta_emp as Sale
from controllers.Log import Login_main as Login

import sys

if __name__ == '__main__':
    app: object = QApplication(sys.argv)
    app_init: object = Admin()
    app_init.show()
    sys.exit(app.exec())
    