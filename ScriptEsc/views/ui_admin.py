# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_admin.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form_main(object):
    def setupUi(self, Form_main):
        if not Form_main.objectName():
            Form_main.setObjectName(u"Form_main")
        Form_main.resize(700, 600)
        Form_main.setMinimumSize(QSize(700, 600))
        Form_main.setMaximumSize(QSize(700, 600))
        Form_main.setSizeIncrement(QSize(700, 600))
        Form_main.setBaseSize(QSize(700, 600))
        self.gridLayout = QGridLayout(Form_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_tittle = QFrame(Form_main)
        self.frame_tittle.setObjectName(u"frame_tittle")
        self.frame_tittle.setStyleSheet(u"background-color: rgb(1, 112, 197);\n"
"color:white;")
        self.frame_tittle.setFrameShape(QFrame.StyledPanel)
        self.frame_tittle.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_tittle)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_titulo = QLabel(self.frame_tittle)
        self.label_titulo.setObjectName(u"label_titulo")

        self.gridLayout_2.addWidget(self.label_titulo, 0, 0, 1, 1)

        self.label_user = QLabel(self.frame_tittle)
        self.label_user.setObjectName(u"label_user")

        self.gridLayout_2.addWidget(self.label_user, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_tittle, 0, 0, 1, 1)

        self.frame_body = QFrame(Form_main)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setStyleSheet(u"QFrame{\n"
"background-color: rgb(1, 112, 197);\n"
"color:white;\n"
"}\n"
"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.frame_botones_opc = QFrame(self.frame_body)
        self.frame_botones_opc.setObjectName(u"frame_botones_opc")
        self.frame_botones_opc.setGeometry(QRect(310, 0, 361, 78))
        self.frame_botones_opc.setFrameShape(QFrame.StyledPanel)
        self.frame_botones_opc.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_botones_opc)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_productos = QPushButton(self.frame_botones_opc)
        self.btn_productos.setObjectName(u"btn_productos")
        self.btn_productos.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/settings_generic/producto.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_productos.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_productos)

        self.btn_ventas = QPushButton(self.frame_botones_opc)
        self.btn_ventas.setObjectName(u"btn_ventas")
        self.btn_ventas.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"./assets/settings_generic/ventas.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ventas.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_ventas)

        self.btn_personal = QPushButton(self.frame_botones_opc)
        self.btn_personal.setObjectName(u"btn_personal")
        self.btn_personal.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"./assets/settings_generic/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_personal.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_personal)

        self.frame_3 = QFrame(self.frame_body)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 50, 211, 321))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.tableWidget_top10 = QTableWidget(self.frame_3)
        self.tableWidget_top10.setObjectName(u"tableWidget_top10")

        self.gridLayout_3.addWidget(self.tableWidget_top10, 1, 0, 1, 1)

        self.frame_estadistica = QFrame(self.frame_body)
        self.frame_estadistica.setObjectName(u"frame_estadistica")
        self.frame_estadistica.setGeometry(QRect(280, 90, 381, 131))
        self.frame_estadistica.setStyleSheet(u"")
        self.frame_estadistica.setFrameShape(QFrame.StyledPanel)
        self.frame_estadistica.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_estadistica)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(self.frame_estadistica)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_estadistica)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 1, 1, 1)

        self.frame_num_sta = QFrame(self.frame_estadistica)
        self.frame_num_sta.setObjectName(u"frame_num_sta")
        self.frame_num_sta.setFrameShape(QFrame.StyledPanel)
        self.frame_num_sta.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_num_sta)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_venta_dia = QLabel(self.frame_num_sta)
        self.label_venta_dia.setObjectName(u"label_venta_dia")

        self.horizontalLayout_2.addWidget(self.label_venta_dia)

        self.label_total_venta = QLabel(self.frame_num_sta)
        self.label_total_venta.setObjectName(u"label_total_venta")
        self.label_total_venta.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_total_venta)


        self.gridLayout_5.addWidget(self.frame_num_sta, 1, 0, 1, 2)

        self.btn_refrescar = QPushButton(self.frame_body)
        self.btn_refrescar.setObjectName(u"btn_refrescar")
        self.btn_refrescar.setGeometry(QRect(660, 440, 31, 24))
        icon3 = QIcon()
        icon3.addFile(u"./assets/settings_generic/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refrescar.setIcon(icon3)

        self.gridLayout.addWidget(self.frame_body, 1, 0, 1, 1)

        self.frame_footer = QFrame(Form_main)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setStyleSheet(u"background-color: rgb(1, 112, 197);\n"
"color:white;")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.label_fecha = QLabel(self.frame_footer)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(540, 20, 121, 21))
        self.btn_close = QPushButton(self.frame_footer)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(30, 20, 75, 24))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"background-color: rgb(8, 74, 124);")
        icon4 = QIcon()
        icon4.addFile(u"./assets/settings_generic/close_secion.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)

        self.gridLayout.addWidget(self.frame_footer, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 8)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 8)
        self.gridLayout.setRowMinimumHeight(2, 1)

        self.retranslateUi(Form_main)

        QMetaObject.connectSlotsByName(Form_main)
    # setupUi

    def retranslateUi(self, Form_main):
        Form_main.setWindowTitle(QCoreApplication.translate("Form_main", u"Admin", None))
        self.label_titulo.setText(QCoreApplication.translate("Form_main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Titulo</span></p></body></html>", None))
        self.label_user.setText(QCoreApplication.translate("Form_main", u"<html><head/><body><p align=\"center\">Bienvenido :user</p></body></html>", None))
        self.btn_productos.setText(QCoreApplication.translate("Form_main", u"Productos", None))
        self.btn_ventas.setText(QCoreApplication.translate("Form_main", u"Ventas", None))
        self.btn_personal.setText(QCoreApplication.translate("Form_main", u"Personal", None))
        self.label_2.setText(QCoreApplication.translate("Form_main", u"<html><head/><body><p><span style=\" font-size:18pt;\">Top Producto [+]</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form_main", u"<html><head/><body><p><span style=\" font-size:16pt;\">Ventas del dia</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form_main", u"<html><head/><body><p><span style=\" font-size:16pt;\">Total vendido $</span></p></body></html>", None))
        self.label_venta_dia.setText(QCoreApplication.translate("Form_main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#20ff33;\">0</span></p></body></html>", None))
        self.label_total_venta.setText(QCoreApplication.translate("Form_main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#14ff4b;\">0</span></p></body></html>", None))
        self.btn_refrescar.setText("")
        self.label_fecha.setText(QCoreApplication.translate("Form_main", u"<html><head/><body><p align=\"center\">Fecha</p></body></html>", None))
        self.btn_close.setText(QCoreApplication.translate("Form_main", u"close", None))
    # retranslateUi

