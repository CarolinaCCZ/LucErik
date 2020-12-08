# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ordenes.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 951, 71))
        self.frame.setStyleSheet("background-color: rgb(230, 233, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelOP = QtWidgets.QLabel(self.frame)
        self.labelOP.setGeometry(QtCore.QRect(30, 20, 101, 21))
        self.labelOP.setStyleSheet("color: rgb(85, 0, 127);\n"
"text-decoration: underline;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.labelOP.setObjectName("labelOP")
        self.labelSRV = QtWidgets.QLabel(self.frame)
        self.labelSRV.setGeometry(QtCore.QRect(430, 20, 101, 21))
        self.labelSRV.setStyleSheet("color: rgb(85, 0, 127);\n"
"text-decoration: underline;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.labelSRV.setTextFormat(QtCore.Qt.PlainText)
        self.labelSRV.setObjectName("labelSRV")
        self.labelHR = QtWidgets.QLabel(self.frame)
        self.labelHR.setGeometry(QtCore.QRect(730, 20, 61, 21))
        self.labelHR.setStyleSheet("color: rgb(85, 0, 127);\n"
"text-decoration: underline;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.labelHR.setObjectName("labelHR")
        self.nombreOP = QtWidgets.QLabel(self.frame)
        self.nombreOP.setGeometry(QtCore.QRect(150, 20, 211, 21))
        self.nombreOP.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.nombreOP.setTextFormat(QtCore.Qt.AutoText)
        self.nombreOP.setObjectName("nombreOP")
        self.servicio = QtWidgets.QLabel(self.frame)
        self.servicio.setGeometry(QtCore.QRect(540, 20, 111, 21))
        self.servicio.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.servicio.setObjectName("servicio")
        self.hora = QtWidgets.QLabel(self.frame)
        self.hora.setGeometry(QtCore.QRect(800, 20, 111, 21))
        self.hora.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.hora.setObjectName("hora")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 961, 561))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 951, 501))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 500, 951, 61))
        self.frame_3.setStyleSheet("background-color: rgb(230, 233, 236);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn_llevarMaterial = QtWidgets.QPushButton(self.frame_3)
        self.btn_llevarMaterial.setGeometry(QtCore.QRect(630, 10, 131, 41))
        self.btn_llevarMaterial.setStyleSheet("background-color:rgb(164, 164, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btn_llevarMaterial.setObjectName("btn_llevarMaterial")
        self.btn_buscarrMaterial = QtWidgets.QPushButton(self.frame_3)
        self.btn_buscarrMaterial.setGeometry(QtCore.QRect(140, 10, 141, 41))
        self.btn_buscarrMaterial.setStyleSheet("background-color:rgb(164, 164, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0)")
        self.btn_buscarrMaterial.setObjectName("btn_buscarrMaterial")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ordenes"))
        self.labelOP.setText(_translate("MainWindow", "OPERARIO:"))
        self.labelSRV.setText(_translate("MainWindow", "SERVICIO:"))
        self.labelHR.setText(_translate("MainWindow", "HORA:"))
        self.nombreOP.setText(_translate("MainWindow", "Carolina Colina Zamorano"))
        self.servicio.setText(_translate("MainWindow", "servicio"))
        self.hora.setText(_translate("MainWindow", "hora"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MÁQUINA"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MATERIAL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CARROS"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "UBICACIÓN"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DISPONIBLES"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CUBIERTAS"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "FABRICADAS"))
        self.btn_llevarMaterial.setText(_translate("MainWindow", "Llevar Material"))
        self.btn_buscarrMaterial.setText(_translate("MainWindow", "Buscar Material"))

