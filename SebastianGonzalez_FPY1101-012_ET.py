import os
import random
import csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_trabajadores = []

def limpiar_pantalla():
    os.system('cls')

def menu():
    print('¡Bienvenido!'
          '\n1. Asignar sueldos aleatorios'
          '\n2. Clasificar sueldos'
          '\n3. Ver estadisticas'
          '\n4. Reporte de sueldos'
          '\n5. Salir del programa')
    
    #Controlar ingreso
    validar_op = True
    while validar_op:
        try:
            op = int(input(('¿Que deseas?: ')))
            if op not in range(1,6):
                print('¡Error! Ingresa un valor entre 1 y 5\n')
            else:
                validar_op = False
        except ValueError:
            print('¡Error! Ingresa un numero entero\n')
    return op

def asignar_sueldos_aleatorios(trabajadores):
    limpiar_pantalla()
    print('Seleccionaste asignar los sueldos de forma aleatoria...\n')

    if len(sueldos_trabajadores) == 10:
        print('Ya seleccionaste asignar los sueldos de forma aleatoria previamente...no puedes asignarlo dos veces')
        input('\nPresione enter para continuar')
        limpiar_pantalla()
    else:
        for nombre in trabajadores:
            trabajador = {}
            trabajador['nombre'] = nombre
            trabajador['sueldo'] = int(random.randint(300000,2500000))
            sueldos_trabajadores.append(trabajador)
        
        print('Sueldos asignados con exito')
        input('\nPresione enter para continuar')
        limpiar_pantalla()
    return sueldos_trabajadores
        
def clasificar_sueldos(sueldos):
    if len(sueldos_trabajadores) == 0:
        print('\nPrimero selecciona asignar los sueldos aleatorios...')
        input('Presiona enter para continuar')
        limpiar_pantalla()
    else:
        limpiar_pantalla()
        plantilla = f'{{:<{20}}}  {{:<{20}}}'
        sueldos_menores_a_800000 = []
        sueldos_entre_800000_y_2000000 = []
        sueldos_mayores_a_2000000 = []
        lista_sueldos = []

        for trabajador in sueldos_trabajadores:
            lista_sueldos.append(int(trabajador['sueldo']))
            if int(trabajador['sueldo']) < 800000:
                sueldos_menores_a_800000.append(trabajador)
            elif int(trabajador['sueldo']) > 2000000:
                sueldos_mayores_a_2000000.append(trabajador)
            else:
                sueldos_entre_800000_y_2000000.append(trabajador)
        
        print('Seleccionaste clasificar sueldos\n')

        print(f'Sueldos menores a $800.000\nTOTAL: {len(sueldos_menores_a_800000)}\n')
        print(plantilla.format('Nombre empleado', 'Sueldo'))
        for trabajador in sueldos_menores_a_800000:
            print(plantilla.format(trabajador['nombre'], trabajador['sueldo']))

        print(f'\nSueldos entre $800.000 y $2.000.000\nTOTAL: {len(sueldos_entre_800000_y_2000000)}\n')
        print(plantilla.format('Nombre empleado', 'Sueldo'))
        for trabajador in sueldos_entre_800000_y_2000000:
            print(plantilla.format(trabajador['nombre'], trabajador['sueldo']))


        print(f'\nSueldos superiores a $2.000.000\nTOTAL: {len(sueldos_mayores_a_2000000)}\n')
        print(plantilla.format('Nombre empleado', 'Sueldo'))
        for trabajador in sueldos_mayores_a_2000000:
            print(plantilla.format(trabajador['nombre'], trabajador['sueldo']))


        print(f'\nTOTAL SUELDOS: ${sum(lista_sueldos)}')


        input('\nPresione enter para continuar')
        limpiar_pantalla()
    
def ver_estadisticas():
    if len(sueldos_trabajadores) == 0:
        print('\nPrimero selecciona asignar los sueldos aleatorios...')
        input('Presiona enter para continuar')
        limpiar_pantalla()
    else:
        limpiar_pantalla()
        op = 0
        while op != 5:
            print('Seleccionaste ver las estadisticas:'
            '\n1. Sueldo mas alto'
            '\n2. Sueldos mas bajo'
            '\n3. Promedio de sueldos'
            '\n4. Media geometrica'
            '\n5. Volver al menu')
            validar_op = True
            while validar_op:
                try:
                    op = int(input(('¿Que deseas?: ')))
                    if op not in range(1,6):
                        print('¡Error! Ingresa un valor entre 1 y 5\n')
                    else:
                        validar_op = False
                except ValueError:
                    print('¡Error! Ingresa un numero entero\n')
        
            if op == 1:
                sueldo_mas_alto = 0
                for trabajador in sueldos_trabajadores:
                    if trabajador['sueldo'] > sueldo_mas_alto:
                        sueldo_mas_alto = trabajador['sueldo']
                print(f'\nSueldo mas alto: ${sueldo_mas_alto}')
                input('\nPresiona enter para continuar')
                limpiar_pantalla()

            if op == 2:
                sueldo_mas_bajo = 2500001
                for trabajador in sueldos_trabajadores:
                    if trabajador['sueldo'] < sueldo_mas_bajo:
                        sueldo_mas_bajo = trabajador['sueldo']
                print(f'\nSueldo mas bajo: ${sueldo_mas_bajo}')
                input('\nPresiona enter para continuar')
                limpiar_pantalla()

            if op == 3:
                suma_sueldos = 0
                for trabajador in sueldos_trabajadores:
                    suma_sueldos += int(trabajador['sueldo'])
                promedio_sueldos = suma_sueldos//len(sueldos_trabajadores)
                print(f'\nPromedio de sueldos: ${promedio_sueldos}')
                input('\nPresiona enter para continuar')
                limpiar_pantalla()

            if op == 4:
                lista_sueldos = []
                for trabajador in sueldos_trabajadores:
                    lista_sueldos.append(int(trabajador['sueldo']))
                
                producto = 1
                for sueldo in lista_sueldos:
                    producto *= sueldo

                media_geometrica = int((producto)**(1/len(lista_sueldos)))
                print(f'\nMedia geometrica: {media_geometrica}')
                input('\nPresiona enter para continuar')
                limpiar_pantalla()
                    
            if op == 5:
                limpiar_pantalla()

def reporte_de_sueldos(sueldos):
    if len(sueldos_trabajadores) == 0:
        print('\nPrimero selecciona asignar los sueldos aleatorios...')
        input('Presiona enter para continuar')
        limpiar_pantalla()
    else:
        limpiar_pantalla()
        print('Seleccionaste reportar los sueldos\n')
        plantilla = f'{{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}} {{:<{20}}}'
        
        print(plantilla.format('Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'))
        for trabajador in sueldos_trabajadores:
            nombre = trabajador['nombre']
            sueldo_base = int(trabajador['sueldo'])
            descuento_salud = int(trabajador['sueldo']*0.07)
            descuento_afp = int(trabajador['sueldo']*0.12)
            sueldo_liquido = int(trabajador['sueldo']*0.81)
            print(plantilla.format(nombre, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido))

        with open('ReporteDeSueldos', 'w', newline='') as archivo:
            escribir = csv.writer(archivo)
            escribir.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'])
            for trabajador in sueldos_trabajadores:
                nombre = trabajador['nombre']
                sueldo_base = int(trabajador['sueldo'])
                descuento_salud = int(trabajador['sueldo']*0.07)
                descuento_afp = int(trabajador['sueldo']*0.12)
                sueldo_liquido = int(trabajador['sueldo']*0.81)
                lista = [nombre, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido]
                escribir.writerow(lista)

            print('\nArchivo CSV creado con exito')
            input('\nPresiona enter para continuar')
            limpiar_pantalla()

def salir_del_programa():
    limpiar_pantalla()
    print('Finalizando programa...\nDesarrollado por Sebastián González Pino\nRUT 19.423.324-8')

op = 0
limpiar_pantalla()
while op != 5:
    op = menu()

    if op == 1:
        sueldos_trabajadores = asignar_sueldos_aleatorios(trabajadores)

    if op == 2:
        clasificar_sueldos(sueldos_trabajadores)

    if op == 3:
        ver_estadisticas()

    if op == 4:
        reporte_de_sueldos(sueldos_trabajadores)

    if op == 5:
        salir_del_programa()
