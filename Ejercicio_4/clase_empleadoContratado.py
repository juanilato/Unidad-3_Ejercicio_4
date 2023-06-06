from clase_empleado import Empleado

class EmpleadoContratado(Empleado):
    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, cantidad_horas, valor_por_hora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__cantidad_horas = cantidad_horas
        self.__valor_por_hora = valor_por_hora
    
    def getSueldo(self):
        return (self.__cantidad_horas * self.__valor_por_hora)
    
    def getHoras(self):
        return self.__cantidad_horas
    
    def incrementaHoras(self,horas):
        self.__cantidad_horas += horas
        print("Horas incrementadas con éxito " + str(self.__cantidad_horas))
    
        
