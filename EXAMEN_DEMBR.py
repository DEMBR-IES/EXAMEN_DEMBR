#EXAMEN_DEMBR

import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "EXAMENdb"
)

cursor = conexion.cursor()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////

print('Bienvenid@ a el programa Menú')

while True:
    print('1. Agregar Plato ')
    print('2. Elimiar plato ')
    print('3. Menú')
    print('4. Salir ')

    opcion = input("Ingrese una de las opciones: ")

    if opcion == '1':
        plato = input("ingres el nombre del platillo a agregar: ").strip()
        sql = "INSERT INTO PLATILLOS (Nombre) VALUES (%s)"
        valor = plato
        cursor.execute(sql, valor)
        conexion.commit()
        if plato == "":
            print('El nombre del plato no puede estar vacio')
        else:
            print(f'El Plato {plato} se ha guardado correctamente ')

    elif opcion == '2':
        plato = input("ingres el nombre del platillo a eliminar: ").strip()
        sql = "DELETE FROM PLATILLOS WHRERE Nombre = %s;"
        valor = plato
        cursor.execute(sql, valor)
        conexion.commit()
        if plato.rowcount > 0:
            print(f'El Plato {plato} se elimino correctamente ')
        else:
            print(f'El Plato {plato} no se encuentra en el menu ')

    elif opcion == "3":
        print("|    Menu Restaurante    |")
        sql = "SELECT ID, Nombre FROM PLATILLOS;"
        cursor.execute(sql)
        conexion.commit()
        platos = cursor.fetchall()
        if len(platos) > 0 :
            for plato in platos:
                print(f'{plato[0]}. {plato[1]}')
                print()
        else:
            print('El menu esta vacio no hay platillos')
    elif opcion == "4":
        print('Gracias por probar mi programa, ¡Hasta pronto!')
        break
    else:
        print('opcion invalida selecione un numero del 1 al 4 ')

cursor.close()
conexion.close()