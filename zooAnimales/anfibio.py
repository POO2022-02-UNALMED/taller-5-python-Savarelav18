from zooAnimales.animal import Animal


class Anfibio(Animal):
    ranas=0
    salamandras=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,zona,colorPiel,venenoso):
        super.__init__(nombre,edad,habitat,genero,zona)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    
    @classmethod
    def cantidadAnfibios(cls):
        if cls._listado !=None:
            return len(cls._listado)
        else:
            return 0
    
    def movimiento():
        return "saltar"
    
    @classmethod
    def crearRana(cls,nombre,edad,genero,zona):
        rana=cls(nombre,edad,"selva",genero,zona,"rojo",True)
        cls._listado.append(rana)
        cls.ranas+=1
        return rana

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero,zona):
        salamandra=cls(nombre,edad,"selva",genero,zona,"negro y amarillo",False)
        cls._listado.append(salamandra)
        cls.ranas+=1
        return salamandra
    

    #getters and setters methods
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls,lista):
        cls._listado=lista
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self,color):
        self._colorPiel=color
    
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso

    


        