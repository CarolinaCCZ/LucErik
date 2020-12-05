# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:45:35 2020

@author: carol
"""

from Login_ui import *
import sqlite3


class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # Método encargado de generar la interfaz
        self.setupUi(self)
        self.btn_Login.clicked.connect(self.conectarBD)
        

        
    def conectarBD(self):
        con = sqlite3.connect('Z:\LucErik.db')
        
        nop = int(self.n_operario.text())
        
        cursorObj = con.cursor()
        cursorObj.execute('SELECT NOMBRE, NUM_OPERARIO FROM OPERARIOS')
        lista = cursorObj.fetchall()
        
        for i in lista:
            if(i[1] == nop):
                self.label_Nombre.setText(i[0])
                self.label_Nombre.setVisible(True)
                self.btn_acceder.setVisible(True)
        
        #self.btn_acceder.clicked.connect(Nueva Ventana)
       
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()