# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ordenes.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 656)
        MainWindow.setWindowTitle("Ordenes")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1055, 71))
        self.frame.setStyleSheet("background-color: rgb(230, 233, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.labelOP = QtWidgets.QLabel(self.frame)
        self.labelOP.setGeometry(QtCore.QRect(60, 20, 101, 21))
        self.labelOP.setStyleSheet("color: rgb(85, 0, 127);\n"
                                   "text-decoration: underline;\n"
                                   "font: 75 12pt \"MS Shell Dlg 2\";")
        self.labelOP.setObjectName("labelOP")

        self.labelSRV = QtWidgets.QLabel(self.frame)
        self.labelSRV.setGeometry(QtCore.QRect(470, 20, 101, 21))
        self.labelSRV.setStyleSheet("color: rgb(85, 0, 127);\n"
                                    "text-decoration: underline;\n"
                                    "font: 75 12pt \"MS Shell Dlg 2\";")
        self.labelSRV.setTextFormat(QtCore.Qt.PlainText)
        self.labelSRV.setObjectName("labelSRV")

        self.labelHR = QtWidgets.QLabel(self.frame)
        self.labelHR.setGeometry(QtCore.QRect(770, 20, 61, 21))
        self.labelHR.setStyleSheet("color: rgb(85, 0, 127);\n"
                                   "text-decoration: underline;\n"
                                   "font: 75 12pt \"MS Shell Dlg 2\";")
        self.labelHR.setObjectName("labelHR")

        self.nombreOP = QtWidgets.QLabel(self.frame)
        self.nombreOP.setGeometry(QtCore.QRect(170, 20, 211, 21))
        self.nombreOP.setStyleSheet("color: rgb(85, 0, 127);\n"
                                    "font: 11pt \"MS Shell Dlg 2\";")
        self.nombreOP.setTextFormat(QtCore.Qt.AutoText)
        self.nombreOP.setObjectName("nombreOP")

        self.servicio = QtWidgets.QLabel(self.frame)
        self.servicio.setGeometry(QtCore.QRect(570, 20, 111, 21))
        self.servicio.setStyleSheet("color: rgb(85, 0, 127);\n"
                                    "font: 11pt \"MS Shell Dlg 2\";")
        self.servicio.setObjectName("servicio")

        self.hora = QtWidgets.QLabel(self.frame)
        self.hora.setGeometry(QtCore.QRect(840, 20, 111, 21))
        self.hora.setStyleSheet("color: rgb(85, 0, 127);\n"
                                "font: 11pt \"MS Shell Dlg 2\";")
        self.hora.setObjectName("hora")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(230, 233, 236);")
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 1055, 561))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(15, 0, 1023, 501))
        self.tableWidget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)

        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 500, 1051, 61))
        self.frame_3.setStyleSheet("background-color: rgb(230, 233, 236);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.btn_llevarMaterial = QtWidgets.QPushButton(self.frame_3)
        self.btn_llevarMaterial.setText("Llevar Material")
        self.btn_llevarMaterial.setGeometry(QtCore.QRect(780, 10, 131, 41))
        self.btn_llevarMaterial.setStyleSheet("background-color:\"steelblue\";\n"
                                              "color: \"white\";\n"
                                              "font: 11pt \"MS Shell Dlg 2\";")
        self.btn_llevarMaterial.setObjectName("btn_llevarMaterial")

        self.btn_buscarMaterial = QtWidgets.QPushButton(self.frame_3)
        self.btn_buscarMaterial.setText("Buscar Material")
        self.btn_buscarMaterial.setGeometry(QtCore.QRect(200, 10, 141, 41))
        self.btn_buscarMaterial.setStyleSheet("background-color:\"steelblue\";\n"
                                              "color: \"white\";\n"
                                              "font: 11pt \"MS Shell Dlg 2\";")
        self.btn_buscarMaterial.setObjectName("btn_buscarMaterial")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Deshabilitar edición
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tableWidget.setDragDropOverwriteMode(False)

        # Seleccionar toda la fila
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Alineación del texto del encabezado
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                                Qt.AlignCenter)

        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tableWidget.horizontalHeader().setHighlightSections(False)

        # Ocultar encabezado vertical
        self.tableWidget.verticalHeader().setVisible(False)

        nombreColumnas = (
        "MÁQUINA", "MATERIAL", "CARROS", "UBICACIÓN", "DISPONIBLES", "CUBIERTAS", "PENDIENTES", "PRIORIDAD")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)

        # Color del encabezado
        style = "::section {""background-color: steelblue; color: white; }"
        self.tableWidget.horizontalHeader().setStyleSheet(style)

        # Color de fondo de la tabla
        self.tableWidget.setStyleSheet("background-color: ghostwhite; color: black;")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ordenes"))
        self.labelOP.setText(_translate("MainWindow", "OPERARIO:"))
        self.labelSRV.setText(_translate("MainWindow", "SERVICIO:"))
        self.labelHR.setText(_translate("MainWindow", "HORA:"))


