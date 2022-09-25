from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio

class Animal:
    _totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero,zona):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal._totalAnimales+=1
    
    def movimiento():
        return "desplazarse"
    @classmethod
    def totalPorTipo():
        return "Mamiferos: "+Mamifero.cantidadMamiferos()+'\n'+"Aves: "+Ave.cantidadAves()+'\n'+"Reptiles: "+Reptil.cantidadReptiles()+'\n'+"Peces: "+Pez.cantidadPeces()+'\n'+"Anfibios: "+Anfibio.cantidadAnfibios()

    def __str__(self):
        if self._zona ==None:
            return "Mi nombre es "+self.nombre+", tengo una edad de "+self.edad+", habito en " +self.habitat+" y mi genero es " +self.genero
        else:
            return "Mi nombre es "+self.nombre+", tengo una edad de "+self.edad+", habito en " +self.habitat+" y mi genero es " +self.genero+", la zona en la que me ubico es "+self.zona+", en el "+self.zona.getZoo()
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def setTotalAnimales(self,totalAnimales):
        self._totalAnimales = totalAnimales
    

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    

    def setEdad(self,edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self,habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self,zona):
        self.zona = zona
    