# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscarMaterial.ui'
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
        global comboBox
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 600)
        MainWindow.setWindowTitle("Buscar Material")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -40, 500, 610))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Botón VOLVER
        self.btn_Volver = QtWidgets.QPushButton(self.frame)
        self.btn_Volver.setText("  Volver")
        self.btn_Volver.setGeometry(QtCore.QRect(70, 570, 111, 41))
        self.btn_Volver.setIcon(QtGui.QIcon("back.png"))
        self.btn_Volver.setStyleSheet("background-color:steelblue;\n"
                                       "font: 11pt \"MS Shell Dlg 2\";\n"
                                       "color: white")
        self.btn_Volver.setObjectName("btn_Volver")

        # Botón RECOGER
        self.btn_Recoger = QtWidgets.QPushButton(self.frame)
        self.btn_Recoger.setText("Recoger")
        self.btn_Recoger.setGeometry(QtCore.QRect(345, 570, 111, 41))
        self.btn_Recoger.setStyleSheet("background-color:steelblue;\n"
                                       "font: 11pt \"MS Shell Dlg 2\";\n"
                                       "color: white")
        self.btn_Recoger.setObjectName("btn_Recoger")


        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setColumnCount(4)
        #self.tableWidget.setRowCount(9)

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

        # Establecer el número de columnas
        self.tableWidget.setColumnCount(4)

        # Establecer el número de filas
        #self.tableWidget.setRowCount(11)

        nombreColumnas = ("MATERIAL", "UBICACIÓN", "STOCK", "QUITAR")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)

        # Color del encabezado
        style = "::section {""background-color: steelblue; color: white; }"
        self.tableWidget.horizontalHeader().setStyleSheet(style)
        # Establecer altura de las filas
        self.tableWidget.verticalHeader().setDefaultSectionSize(42)

        # Color de fondo de la tabla
        self.tableWidget.setStyleSheet("background-color: ghostwhite; color: black;")



        # Establecer ancho de las columnas
        for indice, ancho in enumerate((100, 150, 120, 110), start=0):
            self.tableWidget.setColumnWidth(indice, ancho)

        self.tableWidget.resize(700, 491)
        self.tableWidget.move(20, 56)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



