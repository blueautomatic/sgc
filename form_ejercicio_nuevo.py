# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_ejercicio_nuevo.ui'
#
# Created: Wed Feb 14 21:24:42 2018
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_ejercicio_nuevo(object):
    def setupUi(self, form_ejercicio_nuevo):
        form_ejercicio_nuevo.setObjectName("form_ejercicio_nuevo")
        form_ejercicio_nuevo.resize(616, 256)
        form_ejercicio_nuevo.setStyleSheet("color: rgb(3, 3, 3);\n"
"background-color: rgb(44, 43, 58);\n"
"font: 10pt \"Liberation Sans\";\n"
"color: rgb(252, 252, 252);\n"
"selection-background-color: rgb(155, 155, 185);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_ejercicio_nuevo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(form_ejercicio_nuevo)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.lne_cuit = QtWidgets.QLineEdit(form_ejercicio_nuevo)
        self.lne_cuit.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.verticalLayout_2.addWidget(self.lne_cuit)
        self.horizontalLayout_15.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(form_ejercicio_nuevo)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.lne_razon_social = QtWidgets.QLineEdit(form_ejercicio_nuevo)
        self.lne_razon_social.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.verticalLayout_3.addWidget(self.lne_razon_social)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.btn_buscar = QtWidgets.QPushButton(form_ejercicio_nuevo)
        self.btn_buscar.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_buscar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_buscar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_15.addWidget(self.btn_buscar)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(form_ejercicio_nuevo)
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"background-color: rgb(123, 121, 143);\n"
"}\n"
"QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(133, 0))
        self.label_2.setMaximumSize(QtCore.QSize(133, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lne_descripcion = QtWidgets.QLineEdit(self.tab)
        self.lne_descripcion.setMinimumSize(QtCore.QSize(300, 0))
        self.lne_descripcion.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lne_descripcion.setObjectName("lne_descripcion")
        self.horizontalLayout_5.addWidget(self.lne_descripcion)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cbx_tipo = QtWidgets.QComboBox(self.tab)
        self.cbx_tipo.setObjectName("cbx_tipo")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.horizontalLayout_3.addWidget(self.cbx_tipo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(75, 0))
        self.label.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dte_fec_inic = QtWidgets.QDateEdit(self.tab)
        self.dte_fec_inic.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dte_fec_inic.setObjectName("dte_fec_inic")
        self.horizontalLayout.addWidget(self.dte_fec_inic)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMinimumSize(QtCore.QSize(75, 0))
        self.label_3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dte_fec_fin = QtWidgets.QDateEdit(self.tab)
        self.dte_fec_fin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dte_fec_fin.setObjectName("dte_fec_fin")
        self.horizontalLayout_2.addWidget(self.dte_fec_fin)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.btn_guardar = QtWidgets.QPushButton(self.tab)
        self.btn_guardar.setMinimumSize(QtCore.QSize(75, 50))
        self.btn_guardar.setMaximumSize(QtCore.QSize(75, 50))
        self.btn_guardar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_guardar.setIconSize(QtCore.QSize(50, 50))
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout_4.addWidget(self.btn_guardar)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(form_ejercicio_nuevo)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_ejercicio_nuevo)
        form_ejercicio_nuevo.setTabOrder(self.lne_cuit, self.lne_razon_social)
        form_ejercicio_nuevo.setTabOrder(self.lne_razon_social, self.btn_buscar)
        form_ejercicio_nuevo.setTabOrder(self.btn_buscar, self.tabWidget)
        form_ejercicio_nuevo.setTabOrder(self.tabWidget, self.lne_descripcion)
        form_ejercicio_nuevo.setTabOrder(self.lne_descripcion, self.cbx_tipo)
        form_ejercicio_nuevo.setTabOrder(self.cbx_tipo, self.dte_fec_inic)
        form_ejercicio_nuevo.setTabOrder(self.dte_fec_inic, self.dte_fec_fin)
        form_ejercicio_nuevo.setTabOrder(self.dte_fec_fin, self.btn_guardar)

    def retranslateUi(self, form_ejercicio_nuevo):
        _translate = QtCore.QCoreApplication.translate
        form_ejercicio_nuevo.setWindowTitle(_translate("form_ejercicio_nuevo", "Ejercicio Nuevo"))
        self.label_15.setText(_translate("form_ejercicio_nuevo", "CUIT / CUIL: "))
        self.label_16.setText(_translate("form_ejercicio_nuevo", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_ejercicio_nuevo", "Buscar"))
        self.label_2.setText(_translate("form_ejercicio_nuevo", "Descripción o Nombre: "))
        self.label_4.setText(_translate("form_ejercicio_nuevo", "Tipo de Asiento:"))
        self.cbx_tipo.setItemText(0, _translate("form_ejercicio_nuevo", "Compras"))
        self.cbx_tipo.setItemText(1, _translate("form_ejercicio_nuevo", "Ventas"))
        self.label.setText(_translate("form_ejercicio_nuevo", "Fecha Inicio: "))
        self.dte_fec_inic.setDisplayFormat(_translate("form_ejercicio_nuevo", "dd/MM/yyyy"))
        self.label_3.setText(_translate("form_ejercicio_nuevo", "Fecha Fin : "))
        self.dte_fec_fin.setDisplayFormat(_translate("form_ejercicio_nuevo", "dd/MM/yyyy"))
        self.btn_guardar.setText(_translate("form_ejercicio_nuevo", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_ejercicio_nuevo", "Nuevo Ejercicio"))

