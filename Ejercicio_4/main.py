from clase_manejaEmpleados import ListaEmpleados
from clase_menu import Menu


from datetime import datetime

if __name__ == "__main__":
    
    cantidad = int(input("Ingrese cantidad de empleados a registrar: "))

    manejaEmpleados = ListaEmpleados(cantidad)   

    manejaEmpleados.carga()
    #manejaEmpleados.Muestra()
    
    menu = Menu(4)
    opciones = ["Registra Horas","Total Tarea", "Ayuda económica", "Mostrar Empleados"]
    menu.IngresaOpcion(opciones)
    
    
    menu.Muestra()
    
    op = int(input("Ingrese la opcion: "))
    
    while op != menu.getCantidad() + 1:
        if op == 1:
            dni = input("Ingrese dni de empleado: ")
            horas = int(input("Ingrese cantidad de horas a ingresar: "))
            empleado = manejaEmpleados.buscaDNI(dni)
            if empleado != -1:
                manejaEmpleados.cargaHoras(horas, empleado)
            else:
                print("No se encontró el empleado")
        elif op == 2:
            tarea = input("Ingrese tarea a buscar: ")
            año = input("Ingrese año actual: ")
            mes = input("Ingrese mes actual: ")
            dia = input("Ingrese dia actual: ")
            
            fecha = datetime(int(año), int(mes), int(dia))
            
            empleado = manejaEmpleados.buscaTarea(tarea, fecha)
            
            if empleado != -1:
                if empleado.getFechaFin() > fecha:
                    print("Costo total de la obra: " + str(empleado.getCosto()))
                else:
                    print("La tarea solicitada ya finalizo")                    
            else:
                print("No se encontro la tarea solicitada")
        elif op == 3:
            print("Les corresponde ayuda a: ")
            manejaEmpleados.ayudaEconomica()
        elif op == 4:
            manejaEmpleados.Muestra()
        else:
            print("Ingreso opcion incorrecta")
        
        menu.Muestra()
        op = int(input("Ingrese la opcion: "))
        