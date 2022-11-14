# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form_log(object):
    def setupUi(self, Form_log):
        if not Form_log.objectName():
            Form_log.setObjectName(u"Form_log")
        Form_log.resize(420, 500)
        Form_log.setMinimumSize(QSize(420, 500))
        Form_log.setMaximumSize(QSize(420, 500))
        Form_log.setSizeIncrement(QSize(420, 500))
        Form_log.setBaseSize(QSize(420, 500))
        self.gridLayout = QGridLayout(Form_log)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(Form_log)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"background-color: rgb(1, 95, 167);\n"
"color:white;")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_segundo_main = QFrame(self.frame_main)
        self.frame_segundo_main.setObjectName(u"frame_segundo_main")
        self.frame_segundo_main.setGeometry(QRect(90, 30, 241, 321))
        self.frame_segundo_main.setFrameShape(QFrame.StyledPanel)
        self.frame_segundo_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_segundo_main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_segundo_main)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_segundo_main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(15)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaxLength(15)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.pushButton = QPushButton(self.frame_main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 383, 100, 41))
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"\n"
"background-color: rgb(7, 64, 118);\n"
"")

        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)


        self.retranslateUi(Form_log)

        QMetaObject.connectSlotsByName(Form_log)
    # setupUi

    def retranslateUi(self, Form_log):
        Form_log.setWindowTitle(QCoreApplication.translate("Form_log", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Form_log", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Bienvenido a : </span></p><p align=\"center\"><span style=\" font-size:14pt;\">Tienda - Moreno</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form_log", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Identificate</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form_log", u"User -Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form_log", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Form_log", u"Aceder", None))
    # retranslateUi

