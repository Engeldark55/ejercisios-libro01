# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_producto.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form_producto(object):
    def setupUi(self, Form_producto):
        if not Form_producto.objectName():
            Form_producto.setObjectName(u"Form_producto")
        Form_producto.resize(700, 420)
        Form_producto.setMinimumSize(QSize(700, 420))
        Form_producto.setMaximumSize(QSize(700, 420))
        Form_producto.setSizeIncrement(QSize(700, 420))
        Form_producto.setBaseSize(QSize(700, 420))
        Form_producto.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(1, 112, 197);\n"
"color:white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout = QGridLayout(Form_producto)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form_producto)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_formulario = QFrame(self.frame)
        self.frame_formulario.setObjectName(u"frame_formulario")
        self.frame_formulario.setFrameShape(QFrame.StyledPanel)
        self.frame_formulario.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_formulario)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_precio_com = QLineEdit(self.frame_formulario)
        self.line_precio_com.setObjectName(u"line_precio_com")
        self.line_precio_com.setMaxLength(5)
        self.line_precio_com.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_precio_com, 6, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_formulario)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_agregar = QPushButton(self.frame_3)
        self.btn_agregar.setObjectName(u"btn_agregar")
        icon = QIcon()
        icon.addFile(u"./assets/settings_generic/agregar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_agregar)

        self.btn_cancelar = QPushButton(self.frame_3)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        icon1 = QIcon()
        icon1.addFile(u"./assets/settings_generic/cancelar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_cancelar)


        self.gridLayout_2.addWidget(self.frame_3, 9, 0, 1, 1)

        self.line_cantidad_pro = QLineEdit(self.frame_formulario)
        self.line_cantidad_pro.setObjectName(u"line_cantidad_pro")
        self.line_cantidad_pro.setMaxLength(3)
        self.line_cantidad_pro.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_cantidad_pro, 3, 0, 1, 1)

        self.line_calve = QLineEdit(self.frame_formulario)
        self.line_calve.setObjectName(u"line_calve")
        self.line_calve.setMaxLength(15)
        self.line_calve.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_calve, 1, 0, 1, 1)

        self.line_nombre = QLineEdit(self.frame_formulario)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setMaxLength(30)
        self.line_nombre.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_nombre, 2, 0, 1, 1)

        self.label = QLabel(self.frame_formulario)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.line_precio_venta = QLineEdit(self.frame_formulario)
        self.line_precio_venta.setObjectName(u"line_precio_venta")
        self.line_precio_venta.setMaxLength(5)
        self.line_precio_venta.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_precio_venta, 7, 0, 1, 1)

        self.comboBox_tipo = QComboBox(self.frame_formulario)
        self.comboBox_tipo.setObjectName(u"comboBox_tipo")

        self.gridLayout_2.addWidget(self.comboBox_tipo, 5, 0, 1, 1)

        self.line_desc = QLineEdit(self.frame_formulario)
        self.line_desc.setObjectName(u"line_desc")
        self.line_desc.setMaxLength(35)
        self.line_desc.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_desc, 8, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_formulario, 0, 0, 2, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tableWidget_prod = QTableWidget(self.frame_4)
        self.tableWidget_prod.setObjectName(u"tableWidget_prod")

        self.verticalLayout.addWidget(self.tableWidget_prod)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_editar = QPushButton(self.frame_5)
        self.btn_editar.setObjectName(u"btn_editar")
        icon2 = QIcon()
        icon2.addFile(u"./assets/settings_generic/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editar.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(self.frame_5)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        icon3 = QIcon()
        icon3.addFile(u"./assets/settings_generic/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eliminar.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_eliminar)

        self.btn_refrescar = QPushButton(self.frame_5)
        self.btn_refrescar.setObjectName(u"btn_refrescar")
        icon4 = QIcon()
        icon4.addFile(u"./assets/settings_generic/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refrescar.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_refrescar)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout_4.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_generar_cod = QFrame(self.frame)
        self.frame_generar_cod.setObjectName(u"frame_generar_cod")
        self.frame_generar_cod.setFrameShape(QFrame.StyledPanel)
        self.frame_generar_cod.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_generar_cod)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame_generar_cod)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.line_clave = QLineEdit(self.frame_generar_cod)
        self.line_clave.setObjectName(u"line_clave")
        self.line_clave.setMaxLength(15)
        self.line_clave.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.line_clave, 1, 0, 1, 1)

        self.line_cantidad = QLineEdit(self.frame_generar_cod)
        self.line_cantidad.setObjectName(u"line_cantidad")
        self.line_cantidad.setMaxLength(3)
        self.line_cantidad.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.line_cantidad, 1, 1, 1, 1)

        self.btn_crear = QPushButton(self.frame_generar_cod)
        self.btn_crear.setObjectName(u"btn_crear")
        self.btn_crear.setIcon(icon)

        self.gridLayout_3.addWidget(self.btn_crear, 1, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_generar_cod, 1, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 8)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form_producto)

        QMetaObject.connectSlotsByName(Form_producto)
    # setupUi

    def retranslateUi(self, Form_producto):
        Form_producto.setWindowTitle(QCoreApplication.translate("Form_producto", u"Productos", None))
        self.line_precio_com.setPlaceholderText(QCoreApplication.translate("Form_producto", u"$ compra", None))
        self.btn_agregar.setText(QCoreApplication.translate("Form_producto", u"Agregar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Form_producto", u"cancelar", None))
        self.line_cantidad_pro.setPlaceholderText(QCoreApplication.translate("Form_producto", u"Cantidad", None))
        self.line_calve.setPlaceholderText(QCoreApplication.translate("Form_producto", u"Clave", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("Form_producto", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("Form_producto", u"<html><head/><body><p>Agregar Producto</p></body></html>", None))
        self.line_precio_venta.setPlaceholderText(QCoreApplication.translate("Form_producto", u"$ venta", None))
        self.line_desc.setPlaceholderText(QCoreApplication.translate("Form_producto", u"Descripcion", None))
        self.label_3.setText(QCoreApplication.translate("Form_producto", u"<html><head/><body><p>Productos [existencia]</p></body></html>", None))
        self.btn_editar.setText(QCoreApplication.translate("Form_producto", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Form_producto", u"Eliminar", None))
        self.btn_refrescar.setText("")
        self.label_2.setText(QCoreApplication.translate("Form_producto", u"<html><head/><body><p>Generar Codigos</p></body></html>", None))
        self.line_clave.setPlaceholderText(QCoreApplication.translate("Form_producto", u"clave", None))
        self.line_cantidad.setPlaceholderText(QCoreApplication.translate("Form_producto", u"Cantidad", None))
        self.btn_crear.setText(QCoreApplication.translate("Form_producto", u"Crear", None))
    # retranslateUi

