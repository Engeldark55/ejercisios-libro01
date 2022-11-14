# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_venta_emp.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Main_form(object):
    def setupUi(self, Main_form):
        if not Main_form.objectName():
            Main_form.setObjectName(u"Main_form")
        Main_form.resize(1200, 700)
        Main_form.setMinimumSize(QSize(1200, 700))
        Main_form.setMaximumSize(QSize(1200, 700))
        Main_form.setSizeIncrement(QSize(1200, 700))
        Main_form.setBaseSize(QSize(1200, 700))
        Main_form.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Main_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_priimary = QFrame(Main_form)
        self.frame_priimary.setObjectName(u"frame_priimary")
        self.frame_priimary.setStyleSheet(u"")
        self.frame_priimary.setFrameShape(QFrame.StyledPanel)
        self.frame_priimary.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_priimary)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(750, 100, 281, 101))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_priimary)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(80, 100, 671, 511))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_priimary)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(1050, 220, 95, 74))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.frame_4 = QFrame(self.frame_priimary)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(1050, 110, 95, 101))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.frame_5 = QFrame(self.frame_priimary)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(770, 210, 261, 81))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_priimary)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 20, 621, 51))

        self.gridLayout.addWidget(self.frame_priimary, 0, 0, 1, 1)


        self.retranslateUi(Main_form)

        QMetaObject.connectSlotsByName(Main_form)
    # setupUi

    def retranslateUi(self, Main_form):
        Main_form.setWindowTitle(QCoreApplication.translate("Main_form", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Main_form", u"clave", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Main_form", u"cantidad", None))
        self.pushButton_3.setText(QCoreApplication.translate("Main_form", u"Pagar", None))
        self.pushButton_4.setText(QCoreApplication.translate("Main_form", u"Cancelar", None))
        self.pushButton.setText(QCoreApplication.translate("Main_form", u"Agregar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Main_form", u"Quitar", None))
        self.pushButton_5.setText(QCoreApplication.translate("Main_form", u"Cotizar", None))
        self.label.setText(QCoreApplication.translate("Main_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">0</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Main_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Titulo</span></p></body></html>", None))
    # retranslateUi

