import json
from .particula import Particula 


class Administrar:
    def __init__(self):
        self.administrar = []

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.administrar
        )
    def agregar_inicio(self,particula):
        self.administrar.insert(0,particula)

    def agregar_final(self,particula):
        self.administrar.append(particula)

    def mostrar(self):
        for particula in self.administrar:
         print(particula)

    def  guardar(self, ubicacion):
        try: 
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.administrar]
                json.dump(lista, archivo, indent=5 )
            return 1
        except:
            return 0

    def abrir(self,ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.administrar = [Particula(**particula) for particula in lista]
        except:
           return 0

        
    
