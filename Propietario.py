from CentroEducativo import CentroEducativo




class Propietario(CentroEducativo):

    #atributos
    propietarioid = 0
    propietarionombre= 0
    propietariotelefono = 0


    



    #métodos
    def mostrarDatosPropietario(self):
        super().mostrarDatosCentro()
        print("ID Propietario", self.propietarioid)
        print("Nombre Propietario", self.propietarionombre)
        print("Telefono propietario", self.propietariotelefono)