class Empleado:
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    def getSueldo(self):
        pass
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def incrementaHoras(self, horas):
        print("Este empleado no puede incrementar horas ")
    
    def getTarea(self):
        return None
    
    def __str__(self):
        cadena = "Nombre: " + self.__nombre + " "
        cadena += "Telefono: " + self.__telefono + " "
        cadena += "Sueldo: " + str(self.getSueldo())
        return cadena
    
