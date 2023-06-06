from clase_empleado import Empleado

from datetime import datetime

class EmpleadoExterno(Empleado):
    def __init__(self, dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_fin, monto_viatico, costo_obra, monto_seguro_vida):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__monto_viatico = monto_viatico 
        self.__costo_obra = costo_obra
        self.__monto_seguro_vida = monto_seguro_vida
    
    def getSueldo(self):
        return (self.__costo_obra - self.__monto_viatico - self.__monto_seguro_vida)

    def getTarea(self):
        return self.__tarea
    
    def getFechaFin(self):
        arreglo = self.__fecha_fin.split("-")
        fecha = datetime(int(arreglo[0]), int(arreglo[1]), int(arreglo[2]))
        return fecha
            
    
    
    def getCosto(self):
        return self.__costo_obra