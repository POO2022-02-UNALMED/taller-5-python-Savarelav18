from zooAnimales.Animal import Animal
class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado=[]
    def __init__(self, nombre, edad, habitat, genero, zona,colorEscamas,cantidadAletas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)
    
    @classmethod
    def cantidadPeces(cls):
        if cls._listado !=None:
            return len(cls._listado)
        else:
            return 0
        
    def movimiento():
        return"nadar"
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero,zona):
        salmon=cls(nombre,edad,"oceano",genero,zona,"rojo",6)
        cls._listado.append(salmon)
        cls.salmones+=1
        return salmon

    @classmethod
    def crearBacalao(cls,nombre,edad,genero,zona):
        bacalao=cls(nombre,edad,"oceano",genero,zona,"gris",6)
        cls._listado.append(bacalao)
        cls.bacalaos+=1
        return bacalao
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls,lista):
        cls._listado=lista
    
    def getColorEscamas(self):
        return self._colorEscamas
    def getColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas
    
    def getColorEscamas(self):
        return self._cantidadAletas
    def getColorEscamas(self,cantidadAletas):
        self._cantidadAletas=cantidadAletas
    
