# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ventas.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form_ventas(object):
    def setupUi(self, Form_ventas):
        if not Form_ventas.objectName():
            Form_ventas.setObjectName(u"Form_ventas")
        Form_ventas.resize(600, 400)
        Form_ventas.setMinimumSize(QSize(600, 400))
        Form_ventas.setMaximumSize(QSize(600, 400))
        Form_ventas.setSizeIncrement(QSize(600, 400))
        Form_ventas.setBaseSize(QSize(600, 400))
        Form_ventas.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(1, 112, 197);\n"
"color:white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout = QGridLayout(Form_ventas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form_ventas)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_imprimir = QPushButton(self.frame_2)
        self.btn_imprimir.setObjectName(u"btn_imprimir")
        icon = QIcon()
        icon.addFile(u"./assets/settings_generic/imprimir.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_imprimir.setIcon(icon)

        self.gridLayout_3.addWidget(self.btn_imprimir, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 267, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.btn_estadistica = QPushButton(self.frame_2)
        self.btn_estadistica.setObjectName(u"btn_estadistica")
        icon1 = QIcon()
        icon1.addFile(u"./assets/settings_generic/estadistica.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_estadistica.setIcon(icon1)

        self.gridLayout_3.addWidget(self.btn_estadistica, 1, 0, 1, 1)

        self.btn_refrecar = QPushButton(self.frame_2)
        self.btn_refrecar.setObjectName(u"btn_refrecar")
        icon2 = QIcon()
        icon2.addFile(u"./assets/settings_generic/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refrecar.setIcon(icon2)

        self.gridLayout_3.addWidget(self.btn_refrecar, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_busqueda = QLineEdit(self.frame_3)
        self.line_busqueda.setObjectName(u"line_busqueda")

        self.gridLayout_2.addWidget(self.line_busqueda, 0, 0, 1, 1)

        self.comboBox_opc = QComboBox(self.frame_3)
        self.comboBox_opc.setObjectName(u"comboBox_opc")

        self.gridLayout_2.addWidget(self.comboBox_opc, 0, 1, 1, 1)

        self.btn_buscar = QPushButton(self.frame_3)
        self.btn_buscar.setObjectName(u"btn_buscar")
        icon3 = QIcon()
        icon3.addFile(u"./assets/settings_generic/buscar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon3)

        self.gridLayout_2.addWidget(self.btn_buscar, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.frame_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.label_total = QLabel(self.frame_3)
        self.label_total.setObjectName(u"label_total")

        self.gridLayout_2.addWidget(self.label_total, 2, 1, 1, 2)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form_ventas)

        QMetaObject.connectSlotsByName(Form_ventas)
    # setupUi

    def retranslateUi(self, Form_ventas):
        Form_ventas.setWindowTitle(QCoreApplication.translate("Form_ventas", u"Ventas", None))
        self.btn_imprimir.setText(QCoreApplication.translate("Form_ventas", u"Imprimir", None))
        self.btn_estadistica.setText(QCoreApplication.translate("Form_ventas", u"Estadistica", None))
        self.btn_refrecar.setText("")
        self.btn_buscar.setText("")
        self.label_total.setText(QCoreApplication.translate("Form_ventas", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#15ff1d;\">Total</span></p></body></html>", None))
    # retranslateUi

