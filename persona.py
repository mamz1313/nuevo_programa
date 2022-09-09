class Persona:
    
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
    
    def __str__(self):
        return f"Nombre {self._nombre} Apellido {self._apellido}"
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getApellido(self):
        return self._apellido
    def setApellido(self, apellido):
        self._apellido = apellido
        
    def hablar(self, texto):
        print(f"{self._nombre}: {texto}")