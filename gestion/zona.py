class Zona:
    def __init__(self,nombre,zoo,animales=[]):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=animales

    def agregarAnimales(self,animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)

    #Metodos getters and setters
    def setNombre(self,nombre):
        self._nombre=nombre
    def getNombre(self):
        return self._nombre
    
    def setZoo(self,zoo):
        self._zoo=zoo
    def getZoo(self):
        return self._zoo
        
    def setAnimales(self,animal):
        self._animales=animal
    def getAnimales(self):
        return self._animales