from PySide6.QtWidgets import QApplication
from controllers.Admin import AdminMain

import sys

if __name__ == '__main__':
    app: object = QApplication(sys.argv)
    app_init: object = AdminMain()
    app_init.show()
    sys.exit(app.exec())
    