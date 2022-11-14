# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_empleado.ui'
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

class Ui_Form_empleado(object):
    def setupUi(self, Form_empleado):
        if not Form_empleado.objectName():
            Form_empleado.setObjectName(u"Form_empleado")
        Form_empleado.resize(800, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_empleado.sizePolicy().hasHeightForWidth())
        Form_empleado.setSizePolicy(sizePolicy)
        Form_empleado.setMinimumSize(QSize(800, 450))
        Form_empleado.setMaximumSize(QSize(800, 450))
        Form_empleado.setSizeIncrement(QSize(800, 450))
        Form_empleado.setBaseSize(QSize(800, 450))
        Form_empleado.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(1, 112, 197);\n"
"color:white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout = QGridLayout(Form_empleado)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form_empleado)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_formulario = QFrame(self.frame)
        self.frame_formulario.setObjectName(u"frame_formulario")
        self.frame_formulario.setFrameShape(QFrame.StyledPanel)
        self.frame_formulario.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_formulario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_formulario)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label)

        self.line_clave_empleado = QLineEdit(self.frame_formulario)
        self.line_clave_empleado.setObjectName(u"line_clave_empleado")
        self.line_clave_empleado.setMaxLength(15)
        self.line_clave_empleado.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.line_clave_empleado)

        self.line_nombreCompleto = QLineEdit(self.frame_formulario)
        self.line_nombreCompleto.setObjectName(u"line_nombreCompleto")
        self.line_nombreCompleto.setMaxLength(50)
        self.line_nombreCompleto.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.line_nombreCompleto)

        self.line_edad = QLineEdit(self.frame_formulario)
        self.line_edad.setObjectName(u"line_edad")
        self.line_edad.setMaxLength(2)
        self.line_edad.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.line_edad)

        self.frame_5 = QFrame(self.frame_formulario)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_ine = QLineEdit(self.frame_5)
        self.line_ine.setObjectName(u"line_ine")
        self.line_ine.setMaxLength(40)
        self.line_ine.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_ine, 0, 0, 1, 1)

        self.btn_ine = QPushButton(self.frame_5)
        self.btn_ine.setObjectName(u"btn_ine")
        icon = QIcon()
        icon.addFile(u"./assets/settings_generic/buscar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ine.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_ine, 0, 1, 1, 1)

        self.line_domicilio = QLineEdit(self.frame_5)
        self.line_domicilio.setObjectName(u"line_domicilio")
        self.line_domicilio.setMaxLength(40)
        self.line_domicilio.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_domicilio, 1, 0, 1, 1)

        self.btn_domicilio = QPushButton(self.frame_5)
        self.btn_domicilio.setObjectName(u"btn_domicilio")
        self.btn_domicilio.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_domicilio, 1, 1, 1, 1)

        self.line_contrato = QLineEdit(self.frame_5)
        self.line_contrato.setObjectName(u"line_contrato")
        self.line_contrato.setMaxLength(35)
        self.line_contrato.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_contrato, 2, 0, 1, 1)

        self.btn_contrato = QPushButton(self.frame_5)
        self.btn_contrato.setObjectName(u"btn_contrato")
        self.btn_contrato.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_contrato, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_5)

        self.comboBox_genero = QComboBox(self.frame_formulario)
        self.comboBox_genero.setObjectName(u"comboBox_genero")

        self.verticalLayout.addWidget(self.comboBox_genero)

        self.line_sueldo = QLineEdit(self.frame_formulario)
        self.line_sueldo.setObjectName(u"line_sueldo")
        self.line_sueldo.setMaxLength(4)
        self.line_sueldo.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.line_sueldo)

        self.line_horario = QLineEdit(self.frame_formulario)
        self.line_horario.setObjectName(u"line_horario")
        self.line_horario.setMaxLength(10)
        self.line_horario.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.line_horario)

        self.comboBox_estatus = QComboBox(self.frame_formulario)
        self.comboBox_estatus.setObjectName(u"comboBox_estatus")

        self.verticalLayout.addWidget(self.comboBox_estatus)

        self.frame_4 = QFrame(self.frame_formulario)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_agregar = QPushButton(self.frame_4)
        self.btn_agregar.setObjectName(u"btn_agregar")
        icon1 = QIcon()
        icon1.addFile(u"./assets/settings_generic/agregar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_agregar)

        self.btn_cancelar_form = QPushButton(self.frame_4)
        self.btn_cancelar_form.setObjectName(u"btn_cancelar_form")
        icon2 = QIcon()
        icon2.addFile(u"./assets/settings_generic/cancelar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar_form.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_cancelar_form)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_formulario)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_buscar = QPushButton(self.frame_6)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setIcon(icon)

        self.gridLayout_3.addWidget(self.btn_buscar, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.frame_6)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_editar = QPushButton(self.frame_7)
        self.line_editar.setObjectName(u"line_editar")
        icon3 = QIcon()
        icon3.addFile(u"./assets/settings_generic/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.line_editar.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.line_editar)

        self.btn_eliminar = QPushButton(self.frame_7)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        icon4 = QIcon()
        icon4.addFile(u"./assets/settings_generic/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eliminar.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.btn_eliminar)


        self.gridLayout_3.addWidget(self.frame_7, 2, 0, 1, 1)

        self.line_busqueda_empleado = QLineEdit(self.frame_6)
        self.line_busqueda_empleado.setObjectName(u"line_busqueda_empleado")
        self.line_busqueda_empleado.setMaxLength(30)
        self.line_busqueda_empleado.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.line_busqueda_empleado, 0, 0, 1, 1)

        self.comboBox_busqueda = QComboBox(self.frame_6)
        self.comboBox_busqueda.setObjectName(u"comboBox_busqueda")

        self.gridLayout_3.addWidget(self.comboBox_busqueda, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_cancelar_sesion = QPushButton(self.frame_8)
        self.btn_cancelar_sesion.setObjectName(u"btn_cancelar_sesion")
        self.btn_cancelar_sesion.setIcon(icon2)

        self.gridLayout_4.addWidget(self.btn_cancelar_sesion, 2, 2, 1, 1)

        self.btn_crear = QPushButton(self.frame_8)
        self.btn_crear.setObjectName(u"btn_crear")
        self.btn_crear.setIcon(icon1)

        self.gridLayout_4.addWidget(self.btn_crear, 2, 1, 1, 1)

        self.line_calve_e_sesion = QLineEdit(self.frame_8)
        self.line_calve_e_sesion.setObjectName(u"line_calve_e_sesion")
        self.line_calve_e_sesion.setMaxLength(15)
        self.line_calve_e_sesion.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.line_calve_e_sesion, 1, 0, 1, 1)

        self.line_user_name = QLineEdit(self.frame_8)
        self.line_user_name.setObjectName(u"line_user_name")
        self.line_user_name.setMaxLength(15)
        self.line_user_name.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.line_user_name, 1, 1, 1, 1)

        self.line_password = QLineEdit(self.frame_8)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setMaxLength(15)
        self.line_password.setEchoMode(QLineEdit.Password)
        self.line_password.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.line_password, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_8, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form_empleado)

        QMetaObject.connectSlotsByName(Form_empleado)
    # setupUi

    def retranslateUi(self, Form_empleado):
        Form_empleado.setWindowTitle(QCoreApplication.translate("Form_empleado", u"Empleados", None))
        self.label.setText(QCoreApplication.translate("Form_empleado", u"<html><head/><body><p>Formulario</p></body></html>", None))
        self.line_clave_empleado.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Clave", None))
        self.line_nombreCompleto.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Nombre Completo", None))
        self.line_edad.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Edad", None))
        self.line_ine.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Ine (actualizada) ", None))
        self.btn_ine.setText("")
        self.line_domicilio.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Domicilio", None))
        self.btn_domicilio.setText("")
        self.line_contrato.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Contrato", None))
        self.btn_contrato.setText("")
        self.line_sueldo.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Sueldo (Quincenal)", None))
        self.line_horario.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Horario", None))
        self.comboBox_estatus.setCurrentText("")
        self.btn_agregar.setText(QCoreApplication.translate("Form_empleado", u"Agregar", None))
        self.btn_cancelar_form.setText(QCoreApplication.translate("Form_empleado", u"Cancelar", None))
        self.btn_buscar.setText("")
        self.line_editar.setText(QCoreApplication.translate("Form_empleado", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Form_empleado", u"Eliminar", None))
        self.line_busqueda_empleado.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Buscar por ....", None))
        self.btn_cancelar_sesion.setText(QCoreApplication.translate("Form_empleado", u"Cancelar", None))
        self.btn_crear.setText(QCoreApplication.translate("Form_empleado", u"Crear", None))
        self.line_calve_e_sesion.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"Clave", None))
        self.line_user_name.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"User-Name", None))
        self.line_password.setPlaceholderText(QCoreApplication.translate("Form_empleado", u"password", None))
        self.label_2.setText(QCoreApplication.translate("Form_empleado", u"<html><head/><body><p>Generar usuario Secion:</p></body></html>", None))
    # retranslateUi

