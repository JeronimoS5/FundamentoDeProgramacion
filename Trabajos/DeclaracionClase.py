class persona:

    def inicializar(self,nom,edad):
        self.nombre=nom
        self.edad=edad
    def imprimir(self):
        print("Nombre",self.nombre)
        print("Edad",self.edad)

#Bloque principal

persona1=persona()
persona1.inicializar("Pedro", 27)
persona1.imprimir()

persona2=persona()
persona2.inicializar("Carla", 24)
persona2.imprimir()



