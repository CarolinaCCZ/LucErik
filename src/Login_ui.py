# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameLogin = QtWidgets.QFrame(self.centralwidget)
        self.frameLogin.setGeometry(QtCore.QRect(0, 0, 751, 511))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 233, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.frameLogin.setPalette(palette)
        self.frameLogin.setStyleSheet("background-color: rgb(230, 233, 236);")
        self.frameLogin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frameLogin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLogin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLogin.setObjectName("frameLogin")
        self.labelNOperario = QtWidgets.QLabel(self.frameLogin)
        self.labelNOperario.setGeometry(QtCore.QRect(130, 120, 131, 31))
        self.labelNOperario.setStyleSheet("font: bold 10pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 64, 128)")
        self.labelNOperario.setObjectName("labelNOperario")
        self.labelServicio = QtWidgets.QLabel(self.frameLogin)
        self.labelServicio.setGeometry(QtCore.QRect(150, 190, 91, 21))
        self.labelServicio.setStyleSheet("font: bold 10pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 64, 128)")
        self.labelServicio.setObjectName("labelServicio")
        self.btn_Login = QtWidgets.QPushButton(self.frameLogin)
        self.btn_Login.setGeometry(QtCore.QRect(470, 157, 93, 31))
        self.btn_Login.setStyleSheet("background-color:rgb(164, 164, 255);\n"
"color: rgb(0, 0, 0)")
        self.btn_Login.setObjectName("btn_Login")
        self.label_Nombre = QtWidgets.QLabel(self.frameLogin)
        self.label_Nombre.setEnabled(True)
        self.label_Nombre.setVisible(False)
        self.label_Nombre.setGeometry(QtCore.QRect(150, 270, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Nombre.setFont(font)
        self.label_Nombre.setStyleSheet("font: bold 20pt \"Century Gothic\";\n"
"color:rgb(0, 64, 128)")
        self.label_Nombre.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label_Nombre.setObjectName("label_Nombre")
        self.btn_acceder = QtWidgets.QPushButton(self.frameLogin)
        self.btn_acceder.setEnabled(True)
        self.btn_acceder.setVisible(False)
        self.btn_acceder.setGeometry(QtCore.QRect(330, 350, 93, 28))
        self.btn_acceder.setStyleSheet("background-color:rgb(164, 164, 255);\n"
"color: rgb(0, 0, 0)")
        self.btn_acceder.setObjectName("btn_acceder")
        self.servicio = QtWidgets.QLineEdit(self.frameLogin)
        self.servicio.setGeometry(QtCore.QRect(300, 190, 131, 21))
        self.servicio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 64, 128);\n"
"selection-color: rgb(0, 64, 128);")
        self.servicio.setObjectName("servicio")
        self.n_operario = QtWidgets.QLineEdit(self.frameLogin)
        self.n_operario.setGeometry(QtCore.QRect(300, 130, 131, 22))
        self.n_operario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_operario.setObjectName("n_operario")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.n_operario, self.servicio)
        MainWindow.setTabOrder(self.servicio, self.btn_Login)
        MainWindow.setTabOrder(self.btn_Login, self.btn_acceder)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LoginWindow"))
        self.labelNOperario.setText(_translate("MainWindow", "Nº OPERARIO"))
        self.labelServicio.setText(_translate("MainWindow", "SERVICIO"))
        self.btn_Login.setText(_translate("MainWindow", "Conectar"))
        self.label_Nombre.setText(_translate("MainWindow", "Nombre Usuario Base Datos"))
        self.btn_acceder.setText(_translate("MainWindow", "Acceder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

