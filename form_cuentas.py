# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuentas.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_cuentas(object):
    def setupUi(self, form_cuentas):
        form_cuentas.setObjectName("form_cuentas")
        form_cuentas.resize(658, 591)
        form_cuentas.setStyleSheet("color: rgb(3, 3, 3);\n"
"background-color: rgb(44, 43, 58);\n"
"font: 10pt \"Liberation Sans\";\n"
"color: rgb(252, 252, 252);\n"
"selection-background-color: rgb(155, 155, 185);")
        self.layoutWidget = QtWidgets.QWidget(form_cuentas)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 7, 598, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.lne_cuit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_cuit.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.verticalLayout_3.addWidget(self.lne_cuit)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_4.addWidget(self.label_16)
        self.lne_razon_social = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_razon_social.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.verticalLayout_4.addWidget(self.lne_razon_social)
        self.horizontalLayout_15.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.btn_buscar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_buscar.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_buscar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_buscar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_15.addWidget(self.btn_buscar, 0, QtCore.Qt.AlignBottom)
        self.line = QtWidgets.QFrame(form_cuentas)
        self.line.setGeometry(QtCore.QRect(7, 52, 602, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.cbx_ejercicio = QtWidgets.QComboBox(form_cuentas)
        self.cbx_ejercicio.setGeometry(QtCore.QRect(402, 64, 110, 22))
        self.cbx_ejercicio.setMinimumSize(QtCore.QSize(110, 0))
        self.cbx_ejercicio.setMaximumSize(QtCore.QSize(110, 16777215))
        self.cbx_ejercicio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_ejercicio.setObjectName("cbx_ejercicio")
        self.label_21 = QtWidgets.QLabel(form_cuentas)
        self.label_21.setGeometry(QtCore.QRect(354, 66, 41, 16))
        self.label_21.setObjectName("label_21")
        self.btn_buscar_asiento = QtWidgets.QPushButton(form_cuentas)
        self.btn_buscar_asiento.setGeometry(QtCore.QRect(523, 66, 80, 17))
        self.btn_buscar_asiento.setObjectName("btn_buscar_asiento")
        self.line_2 = QtWidgets.QFrame(form_cuentas)
        self.line_2.setGeometry(QtCore.QRect(7, 85, 602, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tw_asiento = QtWidgets.QTableWidget(form_cuentas)
        self.tw_asiento.setGeometry(QtCore.QRect(10, 130, 401, 192))
        self.tw_asiento.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_asiento.setObjectName("tw_asiento")
        self.tw_asiento.setColumnCount(2)
        self.tw_asiento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_asiento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_asiento.setHorizontalHeaderItem(1, item)
        self.tw_asiento.horizontalHeader().setDefaultSectionSize(200)
        self.label_4 = QtWidgets.QLabel(form_cuentas)
        self.label_4.setGeometry(QtCore.QRect(7, 110, 37, 16))
        self.label_4.setObjectName("label_4")
        self.tw_cuentas = QtWidgets.QTableWidget(form_cuentas)
        self.tw_cuentas.setGeometry(QtCore.QRect(10, 350, 581, 192))
        self.tw_cuentas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_cuentas.setObjectName("tw_cuentas")
        self.tw_cuentas.setColumnCount(4)
        self.tw_cuentas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_cuentas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_cuentas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_cuentas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_cuentas.setHorizontalHeaderItem(3, item)
        self.tw_cuentas.horizontalHeader().setDefaultSectionSize(150)
        self.line_3 = QtWidgets.QFrame(form_cuentas)
        self.line_3.setGeometry(QtCore.QRect(10, 330, 602, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.btn_nueva_cuenta = QtWidgets.QPushButton(form_cuentas)
        self.btn_nueva_cuenta.setGeometry(QtCore.QRect(10, 550, 80, 17))
        self.btn_nueva_cuenta.setObjectName("btn_nueva_cuenta")

        self.retranslateUi(form_cuentas)
        QtCore.QMetaObject.connectSlotsByName(form_cuentas)

    def retranslateUi(self, form_cuentas):
        _translate = QtCore.QCoreApplication.translate
        form_cuentas.setWindowTitle(_translate("form_cuentas", "Cuentas"))
        self.label_15.setText(_translate("form_cuentas", "CUIT / CUIL: "))
        self.label_16.setText(_translate("form_cuentas", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_cuentas", "Buscar"))
        self.label_21.setText(_translate("form_cuentas", "Ejercicio:"))
        self.btn_buscar_asiento.setText(_translate("form_cuentas", "Buscar"))
        item = self.tw_asiento.horizontalHeaderItem(0)
        item.setText(_translate("form_cuentas", "Fecha"))
        item = self.tw_asiento.horizontalHeaderItem(1)
        item.setText(_translate("form_cuentas", "Descripción"))
        self.label_4.setText(_translate("form_cuentas", "Asiento:"))
        item = self.tw_cuentas.horizontalHeaderItem(0)
        item.setText(_translate("form_cuentas", "Código"))
        item = self.tw_cuentas.horizontalHeaderItem(1)
        item.setText(_translate("form_cuentas", "Descripción"))
        item = self.tw_cuentas.horizontalHeaderItem(2)
        item.setText(_translate("form_cuentas", "Debe"))
        item = self.tw_cuentas.horizontalHeaderItem(3)
        item.setText(_translate("form_cuentas", "Haber"))
        self.btn_nueva_cuenta.setText(_translate("form_cuentas", "Nueva Cuenta"))

