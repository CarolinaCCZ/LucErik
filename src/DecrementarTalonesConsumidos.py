# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:00:08 2020

@author: Carolina Colina Zamorano
"""

import sqlite3


class DecrementarTalonesConsumidos:

    @staticmethod
    def decrementar():

        try:
            con = sqlite3.connect('Y:\LucErik.db')
            cursor = con.cursor()
        except sqlite3.OperationalError:
            sys.exit()

        cursor.execute("SELECT * FROM HUECOS ORDER BY ID ASC")
        talones = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]

        # print("Nombre columnas: ", field_names)
        print("talones: ", talones)

        cursor.execute("SELECT * FROM MAQUINAS ORDER BY ID ASC")
        cubiertas = cursor.fetchall()
        print("Cubiertas: ", cubiertas)

        print("")

        for i in range (len(talones)):
            # Si hay talones en la máquina para producir
            if talones[i][2] >= 2:
                print("")
                print("Hay talones en la máquina para producir cubiertas")
                print("Máquina en huecos", talones[i][0])
                # Compruebo si todavía hay que seguir produciendo
                if cubiertas[i][5] < cubiertas[i][4]:
                    print("Hay que seguir produciendo", cubiertas[i][5], "<", cubiertas[i][4])
                    sql = "UPDATE MAQUINAS SET PROD_ACTUAL=PROD_ACTUAL+1 WHERE ID='"+talones[i][0]+"'"# Incremento en 1 la producción de cubiertas
                    cursor.executescript(sql)
                    sql = "UPDATE HUECOS SET T1=T1-2 WHERE ID='"+talones[i][0]+"'" # Decremento en 2 el cosumo de talones
                    cursor.executescript(sql)
                    print("Incremento en 1 la produccion de cubiertas")
                    print("Decremento en 2 el consumo de talones")

                # Si ya se ha hecho todas las cubiertas de esa medida
                else:
                    print("Si ya se han hecho todas las cubiertas de esa medida", cubiertas[i][5], "=", cubiertas[i][4])
                    print("Cambio los materiales de la máquina")
                    sql = "UPDATE MAQUINAS SET MAT_ACTUAL=MAT_PROX WHERE ID='"+talones[i][0]+"'"
                    cursor.executescript(sql)
                    sql = "UPDATE MAQUINAS SET TOTALES_ACTUAL=TOTALES_PROX WHERE ID='"+talones[i][0]+"'"
                    cursor.executescript(sql)
                    sql = "UPDATE MAQUINAS SET PROD_ACTUAL=0 WHERE ID='" + talones[i][0] + "'"
                    cursor.executescript(sql)
                    sql = "UPDATE MAQUINAS SET MAT_PROX=NULL WHERE ID='"+talones[i][0]+"'"
                    cursor.executescript(sql)
                    sql = "UPDATE MAQUINAS SET TOTALES_PROX=0 WHERE ID= '" + talones[i][0] + "' "
                    cursor.executescript(sql)

                    sql = "SELECT * FROM MAQUINAS WHERE ID = '"+talones[i][0]+"' "
                    cursor.execute(sql)
                    cubiertas = cursor.fetchall()
                    print("MAQUINAS", cubiertas)

                    print("talones[i][1]", talones[i][1])
                    print("cubiertas[i][2]", cubiertas[i][2])
                    # Una vez cambiada la medida en la máquina, compruebo que tenga material en los huecos
                    if talones[i][1] != cubiertas[i][2]:
                        print("Una vez cambiada la medida, compruebo que tenga material en los huecos")
                        # Busco ese material en los huecos
                        columna = 1
                        encontrado = False

                        while columna < 11 and encontrado==False:
                            print("Columna: ", columna)
                            print("i: ", i)
                            sql = "SELECT * FROM HUECOS WHERE ID = '" + talones[i][0] + "' "
                            cursor.execute(sql)
                            talones = cursor.fetchall()
                            # Si la encuentro, la  coloco en el primer lugar, que es el hueco que se usa para decrementar y producir cubiertas
                            if talones[i][columna] == cubiertas[i][2]:
                                print("Si la encuentro la coloco en el primer lugar de la tabla huecos")
                                temp_material = talones[i][1]
                                temp_talones = talones[i][2]
                                sql = "UPDATE HUECOS SET H1= '" + talones[i][columna] + "' WHERE ID= '" + talones[i][0] + "' "
                                cursor.executescript(sql)
                                sql = "UPDATE HUECOS SET T1= '" + str(talones[i][columna+1]) + "' WHERE ID= '" + talones[i][0] + "' "
                                cursor.executescript(sql)
                                print("El que estaba en primer lugar le coloco donde estaba el otro")
                                sql = "UPDATE HUECOS SET '"+field_names[columna]+"' = '"+temp_material+"' WHERE ID = '" + talones[i][0] + "' "
                                cursor.executescript(sql)
                                sql = "UPDATE HUECOS SET '" +str(field_names[columna+1]) + "' = '" + str(temp_talones) + "' WHERE ID= '" + talones[i][0] + "' "
                                cursor.executescript(sql)

                                cursor.execute("SELECT * FROM HUECOS WHERE ID = '" + talones[i][0] + "' ")
                                print("talones: ", cursor.fetchall())
                                #sql = "SELECT * FROM HUECOS WHERE ID = '" + talones[i][0] + "' "
                                #cursor.execute(sql)
                                #talones = cursor.fetchall()

                                encontrado = True
                                columna = columna + 2

                            else:
                                columna = columna + 2

                        # Si no ha encontrado el material en la máquina dejo el primer hueco en vacío
                        if not encontrado:
                            print("Si no ha encontrado el material, dejo el primer hueco en vacío")
                            sql = "UPDATE HUECOS SET H1='VACIO'"
                            cursor.executescript(sql)
                            sql = "UPDATE HUECOS SET T1=0"
                            cursor.executescript(sql)

                            cursor.execute("SELECT * FROM HUECOS WHERE ID=?", (talones[i][0]))
                            print("HUECOS", cursor.fetchall())

            #Se han acabado los talones para producir, hay que buscar si hay más en la máquina
            else:
                print("Si se han acabado los talones para producir, busco en la máquina")
                # Busco ese material en los huecos
                encontrado = False
                columna = 3

                while columna < 11 and encontrado==False:
                    print("talones[i][columna]: ", talones[i][columna])
                    print("talones[i][columna+1]: ", talones[i][columna + 1])
                    print("i: ", i)
                    # Si la encuentro, la  coloco en el primer lugar, que es el hueco que se usa para decrementar y producir cubiertas
                    if talones[i][columna] == cubiertas[i][2]:
                        print("Si lo encuentro, lo coloco en el primer lugar")
                        sql = "UPDATE HUECOS SET H1= '" + talones[i][columna] + "' WHERE ID= '" + talones[i][0] + "' "
                        cursor.executescript(sql)
                        sql = "UPDATE HUECOS SET T1= '" + str(talones[i][columna+1]) + "' WHERE ID= '" + talones[i][0] + "' "
                        cursor.executescript(sql)

                        # sql = "SELECT * FROM HUECOS WHERE ID = '" + talones[i][0] + "' "
                        # cursor.execute(sql)

                        # Dejo vacío el hueco del que acabamos de quitar un carro
                        print("Dejo vacío el hueco del que acabamos de quitar un carro")

                        sql = "UPDATE HUECOS SET '" + field_names[columna] + "' = 'VACIO'"
                        cursor.executescript(sql)
                        sql = "UPDATE HUECOS SET '" + str(field_names[columna+1]) + "' = 0"
                        cursor.executescript(sql)

                        #sql = "SELECT * FROM HUECOS WHERE ID = '" + talones[i][0] + "' "
                        #cursor.execute(sql)

                        encontrado = True

                        break
                    else:
                        columna = columna + 2

                # Si no ha encontrado el material en la máquina dejo el primer hueco en vacío
                if not encontrado:
                    print("Si no ha encontrado el material en la máquina, dejo el primer hueco en vacío")
                    sql = "UPDATE HUECOS SET H1='VACIO' WHERE ID= '" + talones[i][0] + "' "
                    cursor.executescript(sql)
                    sql = "UPDATE HUECOS SET T1=0 WHERE ID= '" + talones[i][0] + "' "
                    cursor.executescript(sql)

                    cursor.execute("SELECT * FROM HUECOS WHERE ID=?", (talones[i][0],))
                    print("HUECOS", cursor.fetchall())

    # con.close()

if __name__ == "__main__":
    DecrementarTalonesConsumidos.decrementar()