# -*- coding: utf-8 -*-
"""
Clase que incrementa el número de talones fabricados
Cada 20 minutos se incrementa en 1 el número de carros que se están produciendo en cada RTB

@author: Carolina Colina Zamorano
"""

import sqlite3
import os
import sys


class IncrementarTalonesFabricados:
    def __init__(self):
        super().__init__()

    @staticmethod
    def incrementar():

        # Conexión con la base de datos
        global con, cursor
        try:
            con = sqlite3.connect('sqlite/LucErik.db')
            cursor = con.cursor()
        except sqlite3.OperationalError:
            sys.exit()

        sql = "SELECT * FROM LISTADO_RTBS"
        cursor.execute(sql)
        listadoRTBS = cursor.fetchall()
        print("Listado RTBS: ", listadoRTBS)

        # Recorro el listado de RTB'S
        for i in range(len(listadoRTBS)):
            print("i: ", i)
            sql = "SELECT ID FROM PRODUCCION_TALONES WHERE ID= '" + str(listadoRTBS[i][0]) + "' "
            cursor.execute(sql)
            rtb = cursor.fetchall()
            print("")
            print("rtb", rtb)

            # Para cada una de las máquinas voy incrementando el número de carros que se producen.
            # Se incrementa en 1 cada 20 minutos
            for a in range(len(rtb)):
                print("a: ", a)
                print("rtb[0][0]", rtb[0][0])
                sql = "SELECT * FROM PRODUCCION_TALONES WHERE ID= '"+rtb[a][0]+"' "
                cursor.execute(sql)
                ped = cursor.fetchall()
                print("ped: ", ped)

                # Si los que se han producido son menos que los totales incremento
                if ped[a][3] < ped[a][4]:
                    print("ped[a][1]: ", ped[a][1])
                    sql = "UPDATE PRODUCCION_TALONES SET PRODUCIDOS=PRODUCIDOS+1 WHERE ID_MATERIAL= '"+str(ped[a][1])+"' AND ID= '"+rtb[a][0]+"'"
                    cursor.executescript(sql)

                    # He incrementado el número de carros en uno del material con el que está trabajando
                    # Tengo que incrementarlo en la tabla MATERIALES
                    # Obtengo lo que está produciendo la RTB
                    sql = "SELECT * FROM PRODUCCION_TALONES WHERE ID= '"+rtb[a][0]+"' "
                    cursor.execute(sql)
                    prod = cursor.fetchall()
                    print("")
                    print("prod", prod)

                    # Incremento los materiales
                    IncrementarTalonesFabricados.IncrementarMateriales(a, i, cursor, listadoRTBS, prod)

                    """cursor.execute("SELECT * FROM MATERIALES")
                    mat = cursor.fetchall()
                    print("MATERIALES", mat)"""

                    break

        con.close()

    """ Método que incrementa en la tabla materiales a medida que se producen talones en las rtb's """
    @staticmethod
    def IncrementarMateriales(a, i, cur, listadoRTBS, prod):
        # Busco en la tabla MATERIALES si existe un material con ese código
        cur.execute("SELECT count(*) FROM MATERIALES WHERE CODIGO=?;", (prod[a][1],))
        coinc_material = cur.fetchall()
        print("coinc_material", coinc_material[0][0])
        # Si NO EXISTE ese código en la tabla materiales, lo inserto
        if coinc_material[0][0] == 0:
            print("Insertamos nuevo resgistro")
            sql = "INSERT INTO MATERIALES (CODIGO, ORIGEN, STOCK) VALUES ('" + str(prod[a][1]) + "', '" + str(
                listadoRTBS[i][0]) + "', '" + str(1) + "')"
            cur.executescript(sql)

        # SI EXISTE ese código en la tabla MATERIALES
        else:
            # Busco en la tabla que coincidan el material y la ubicación
            cursor.execute("SELECT count(*) FROM MATERIALES WHERE CODIGO=? AND ORIGEN=?;",
                           (prod[a][1], listadoRTBS[i][0],))
            coinc_ubicacion = cursor.fetchall()
            print("coinc_origen", coinc_ubicacion[0][0])

            # Si NO EXISTE inserta un nuevo registro
            if coinc_ubicacion[0][0] == 0:
                print("Insertamos nuevo resgistro -> Existe pero no en la misma ubicación")
                sql = "INSERT INTO MATERIALES (CODIGO, ORIGEN, STOCK) VALUES ('" + str(prod[a][1]) + "', '" + str(
                    listadoRTBS[i][0]) + "', '" + str(1) + "')"
                cursor.executescript(sql)

            else:
                # SI EXISTE ese material y en la misma ubicación, incremento el STOCK
                print("Incrementamos el stock")
                cursor.execute("SELECT ID FROM MATERIALES WHERE CODIGO=? AND ORIGEN=?;",
                               (prod[a][1], listadoRTBS[i][0],))
                id = cursor.fetchall()
                print("id", id[0][0])
                sql = "UPDATE MATERIALES SET STOCK=STOCK+1 WHERE ID= '" + (str(id[0][0])) + "'"
                cursor.executescript(sql)


if __name__ == "__main__":
    IncrementarTalonesFabricados.incrementar()
