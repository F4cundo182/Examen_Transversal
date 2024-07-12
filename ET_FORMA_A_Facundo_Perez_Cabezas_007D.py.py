import random
import csv



lista_trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
opc = 0
sueldo = 0




def Sueldos_Aleatarios(lista_trabajadores, sueldo_minimo, sueldo_maximo):
            trabajadores = []
            for nombre in lista_trabajadores:
                sueldo = random.uniform(sueldo_minimo, sueldo_maximo)
                lista_trabajadores.append((nombre, sueldo))
            return lista_trabajadores
     
def mostrar_listado(trabajadores):
        for nombre, sueldo in trabajadores:
                print(f"{nombre}: ${sueldo:.2f}")   
while True:
        print("\nMenu: ")
        print("1. Asignar Sueldos Aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del Programa")

        opc = input("Opcion: ")

        if opc == 1:
                    sueldo_minimo = 300000
                    sueldo_maximo = 2500000
                    lista_trabajadores = Sueldos_Aleatarios(lista_trabajadores, sueldo_minimo, sueldo_maximo)
                    print("Sueldos Aletarios:")
                    mostrar_listado(lista_trabajadores)
        elif opc == 5:
                    break
            

     
     
     
  


            
                
     

        

