import json
from pprint import pformat
from .particula import Particula 


class Administrar:
    def __init__(self):
        self.administrar = []
        self.graf_dic = dict()

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.administrar
        )

    def __len__(self):
        return (len(self.administrar))
    
    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.administrar):
            particula = self.administrar[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
    
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
            return 1
        except:
     
           return 0

    def orden(self,des,ord):
        if ord == "id":
            self.administrar.sort(key=lambda particula: particula.id,reverse=des)
        if ord == "velocidad":
            self.administrar.sort(key=lambda particula: particula.velocidad,reverse=des)
        if ord == "distancia":
            self.administrar.sort(key=lambda particula: particula.distancia,reverse=des)
    
    def grafo(self):
        for particula in self.administrar:
            origen = (particula.origen_x,particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            if origen in self.graf_dic:
                if destino in self.graf_dic[origen]:
                    pass 
                else:
                    self.graf_dic[origen].append((destino,round(particula.distancia,2)))
            else:
                self.graf_dic[origen] = [(destino,round(particula.distancia,2))]

            if destino in self.graf_dic:
                if origen in self.graf_dic[destino]:
                    pass
                else:
                    self.graf_dic[destino].append((origen,round(particula.distancia,2)))
            else:
                self.graf_dic[destino] = [(origen,round(particula.distancia,2))]
        string = pformat(self.graf_dic, width=40) 
        return(string)
    
    def borrar(self):
        self.graf_dic.clear()