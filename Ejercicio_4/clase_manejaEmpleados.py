import numpy as np

from clase_empleado import Empleado

from clase_empleadoContratado import EmpleadoContratado
from clase_empleadoExterno import EmpleadoExterno
from clase_empleadoPlanta import EmpleadoPlanta




import csv

class ListaEmpleados:
    
    def __init__(self, cantidad):
        self.__arreglo = np.empty(cantidad, dtype = Empleado)
    
    def carga(self):
        archivo = open("planta.csv")
        reader = csv.reader(archivo, delimiter = ";")
        i = 0
        for fila in reader: 
            
            empleado = EmpleadoPlanta(fila[0],fila[1], fila[2], fila[3], float(fila[4]), int(fila[5]))
            self.__arreglo[i] = empleado
            i = i + 1
        archivo.close()
        
        archivo = open("contratados.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader: 
            empleado = EmpleadoContratado(fila[0],fila[1], fila[2], fila[3], fila[4], fila[5], float(fila[6]), float(fila[7]))
            self.__arreglo[i]=empleado
            i = i + 1
        archivo.close()
        
        archivo = open("externos.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader: 
            empleado = EmpleadoExterno(fila[0],fila[1], fila[2], fila[3], fila[4], fila[5],fila[6],float(fila[7]), float(fila[8]), float(fila[9]))
            self.__arreglo[i]= empleado
            i = i + 1
        archivo.close()
    
    def Muestra(self):
        for obj in self.__arreglo:
            print(obj)
    
    def buscaDNI(self, dni):
        i = 0
        while i < self.__arreglo.size and dni != self.__arreglo[i].getDNI():
            i += 1
        if i < len(self.__arreglo):
            empleado = self.__arreglo[i]
        else:
            empleado = -1
        return empleado
    
    def cargaHoras(self, horas, empleado):
        print(empleado)
        empleado.incrementaHoras(horas)
        
    def buscaTarea(self, tarea, fecha):
        i = 0
        while i < self.__arreglo.size and tarea != self.__arreglo[i].getTarea():
            i += 1
        if i < len(self.__arreglo):
            empleado = self.__arreglo[i]
        else: 
            empleado = -1
        return empleado
    
    def ayudaEconomica(self):
        for empleado in self.__arreglo:
            if empleado.getSueldo()< 150000:
                cadena = "Nombre: " + str(empleado.getNombre()) + " "
                cadena += "Direccion: " + str(empleado.getDireccion()) + " "
                cadena += "DNI: " + str(empleado.getDNI()) + " "
                print(cadena)
    
