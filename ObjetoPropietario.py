from Propietario import Propietario 


#instanciamos la clase Propietario
propietario1 = Propietario()
propietario2 = Propietario()
propietario3 = Propietario()
propietario4 = Propietario()
propietario5 = Propietario()


propietario1.propietarioid = 1
propietario1.propietarionombre = "Angel López"
propietario1.propietariotelefono = 12345678

propietario2.propietarioid = 2
propietario2.propietarionombre = "Juan Perez"
propietario2.propietariotelefono = 3232423423


propietario3.propietarioid = 3
propietario3.propietarionombre = "Maria Sosa"
propietario3.propietariotelefono = 12345555


propietario4.propietarioid = 4
propietario4.propietarionombre = "Manuel Díaz"
propietario4.propietariotelefono = 34223424342

propietario5.propietarioid = 5
propietario5.propietarionombre = "José Castillo"
propietario5.propietariotelefono = 133434


print(propietario1.mostrarDatosPropietario())
print(propietario2.mostrarDatosPropietario())
print(propietario3.mostrarDatosPropietario())
print(propietario4.mostrarDatosPropietario())
print(propietario5.mostrarDatosPropietario())