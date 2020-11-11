from .algoritmos import distancia_euclidiana
class Particula:

   def __init__(self,Id, x_1,y_1,x_2,y_2,velocidad,red,green,blue):
      self.__id = Id
      self.__origen_x= x_1
      self.__origen_y= y_1
      self.__destino_x= x_2
      self.__destino_y= y_2
      self.__velocidad = velocidad
      self.__red = red
      self.__green = green 
      self.__blue = blue 
      self.__distancia = distancia_euclidiana(x_1,y_1,x_2,y_2)



   def __str__(self):
      return (
         'Id: '+str(self.__id)+'\n'
         'Origen en y: '+str(self.__origen_y)+'\n'+
         'Origen en y: '+str(self.__origen_y)+'\n'+
         'Destino en x: '+str(self.__destino_x)+'\n'+
         'Destino en y: '+str(self.__destino_y)+'\n'+
         'Velocidad: '+str(self.__velocidad)+'\n'+
         'Red: '+str(self.__red)+'\n'+
         'Green: '+str(self.__green)+'\n'+
         'Blue: '+str(self.__blue)+'\n'+
         'Distancia: '+str(self.__distancia)+'\n'
            )
   
   @property
   def id(self):
      return self.__id

   @property
   def origen_x(self):
      return self.__origen_x

   @property
   def origen_y(self):
      return self.__origen_y

   @property
   def destino_x(self):
      return self.__destino_x
   
   @property
   def destino_y(self):
      return self.__destino_y

   @property
   def velocidad(self):
      return self.__velocidad

   @property
   def green(self):
      return self.__green
   
   @property
   def red(self):
      return self.__red

   @property
   def blue(self):
      return self.__blue

   @property
   def distancia(self):
      return self.__distancia
   
   def to_dict(self):
      return{
         "Id": self.__id,
         "x_1":self.__origen_x,
         "y_1": self.__origen_y,
         "x_2": self.__destino_x,
         "y_2": self.__destino_y,
         "velocidad": self.__velocidad,
         "red": self.__red,
         "green": self.__green,
         "blue": self.__blue
         }