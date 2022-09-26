from zooAnimales.animal import Animal

class Ave(Animal):
    halcones=0
    aguilas=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,zona,colorPlumas):
        super.__init__(nombre,edad,habitat,genero,zona)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        if cls._listado !=None:
            return len(cls._listado)
        else:
            return 0

    def movimiento():
        return "volar"
    
    @classmethod
    def crearHalcon(cls,nombre,edad,genero,zona):
        halcon=cls(nombre,edad,"montanas",genero,zona,"cafe glorioso")
        cls._listado.append(halcon)
        cls.halcones+=1
        return halcon

    @classmethod
    def crearAguila(cls,nombre,edad,genero,zona):
        aguila=cls(nombre,edad,"montanas",genero,zona,"blanco y amarillo")
        cls._listado.append(aguila)
        cls.aguilas+=1
        return aguila
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls,lista):
        cls._listado=lista
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self,color):
        self._colorPlumas=color