from PySide6.QtWidgets import QApplication

import sys

if __name__ == '__main__':
    app: object = QApplication(sys.argv)
    #app_init: object = Admin()
    #app_init.show()
    sys.exit(app.exec())
    