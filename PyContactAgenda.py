#!C:\Program Files\Python37\python.exe

#
# FICHERO: PyContactAgenda.py
#
# AUTOR:
#     - Daniel Belmonte Urbano
#
# OBSERVACIONES:
#	- Este archivo contiene la implementación de la vista de una Agenda de Contactos implementada
#  	  en Python

from src import Controller as kernel
from src import Contacto as contacto

def main():
	#Inicializamos la conexión a la base de datos
	controller = kernel.Controller()
	controller.initDB()

	#Mostramos la cabecera de la aplicación y el menú inicial
	cabecera()
	menu()

	#Capturamos la primera opción seleccionada
	opcion = input()

	while(opcion != '6'):
		#Listar todos los contactos
		if(opcion == '1'):
			listarContactos(controller)

		#Buscar contacto
		if(opcion == '2'):
			buscarContacto(controller)

		#Añadir contacto
		if(opcion == '3'):
			anyadirContacto(controller)

		#Modificar contacto
		if(opcion == '4'):
			modificarContacto(controller)

		#Eliminar contacto
		if(opcion == '5'):
			eliminarContacto(controller)

		#Volvemos a mostrar el menú de opciones
		cabecera()
		menu()
		opcion = input()

	#El usuario ha elegido salir del programa, mostramos mensaje de despedida
	msgSalir()

def cabecera():
	print("=======================================================")
	print("==> PyContactAgenda - Agenda de Contactos en Python <==")
	print("=======================================================")
	print("")

def menu():
	print("---> MENÚ <---")
	print("")
	print("1.- Listar todos los contactos")
	print("2.- Buscar contacto ->")
	print("3.- Añadir contacto")
	print("4.- Modificar contacto")
	print("5.- Eliminar contacto")
	print("6.- Salir")
	print("")
	print("=> Introduce una opción: ")

def subMenuBuscar():
	print("---> BÚSQUEDA DE CONTACTOS <---")
	print("")
	print("1.- Buscar por nombre")
	print("2.- Buscar por apellidos")
	print("3.- Buscar nombre completo")
	print("4.- Salir")
	print("")
	print("=> Introduce una opción: ")

def listarContactos(controller):
	#Mostramos la cabecera de la aplicación y la cabecera de la opción
	cabecera()
	print("---> LISTADO DE CONTACTOS <---")
	print("")

	#Ejecutamos el SELECT * sobre la tabla Contacto
	result = controller.selectAll()

	#Mostramos los resultados por pantalla
	if (len(result) == 0):
		"No hay contactos en la agenda"
	else:
		mostrarResultados(result)

	#A la espera de salir...
	print("")
	print("Pulsa una tecla para continuar")
	input()

def buscarContacto(controller):
	#Mostramos la cabecera de la aplicación, la cabecera de la opción y el menú Buscar Contacto
	cabecera()
	subMenuBuscar()

	#Capturamos la primera opción seleccionada
	opcionB = input()

	while(opcionB != '4'):
		cabecera()

		#Buscar por nombre
		if(opcionB == '1'):
			print("---> BÚSQUEDA DE CONTACTOS > BUSCAR POR NOMBRE <---")
			print("")
			print("¿Qué nombre deseas buscar?")
			nombre = input()
			#Ejecutamos el SELECT por nombre sobre la tabla Contacto
			result = controller.selectContactoPorNombre(nombre)

		#Buscar por apellidos
		if(opcionB == '2'):
			print("---> BÚSQUEDA DE CONTACTOS > BUSCAR POR APELLIDOS <---")
			print("")
			print("¿Qué apellido deseas buscar?")
			apellido = input()
			#Ejecutamos el SELECT por apellido sobre la tabla Contacto
			result = controller.selectContactoPorApellido(apellido)

		#Buscar por nombre completo
		if(opcionB == '3'):
			print("---> BÚSQUEDA DE CONTACTOS > BUSCAR POR NOMBRE COMPLETO <---")
			print("")
			print("¿Qué nombre deseas buscar?")
			nombre = input()
			print("¿Qué apellido 1 deseas buscar?")
			apellido1 = input()
			print("¿Qué apellido 2 deseas buscar?")
			apellido2 = input()
			#Ejecutamos el SELECT por nombre y apellidos sobre la tabla Contacto
			result = controller.selectContactoPorNomCompleto(nombre, apellido1, apellido2)

		#Mostramos los resultados por pantalla
		if(len(result) == 0):
			print("No se han encontrado coincidencias")
		else:
			mostrarResultados(result)

		print("")
		print("Pulsa una tecla para continuar")
		input()

		#Volvemos a mostrar el menú de opciones
		cabecera()
		subMenuBuscar()
		opcionB = input()

	#A la espera de salir...
	print("")
	print("Volviendo al menú principal. Pulsa una tecla para continuar")
	input()

def anyadirContacto(controller):
	#Mostramos la cabecera de la aplicación y la cabecera de la opción
	cabecera()
	print("---> AÑADIR CONTACTO A LA AGENDA <---")
	print("")
	nombre = ""
	apellido1 = ""
	apellido2 = ""
	telefono = ""
	cp = ""

	#Comprobamos que se ha introducido una cadena para el nombre
	while(nombre == ""):
		print("Introduce el nombre del nuevo contacto:")
		nombre = input()

	#Comprobamos que se ha introducido una cadena para el primer apellido
	while(apellido1 == ""):
		print("Introduce el primer apellido del nuevo contacto:")
		apellido1 = input()

	#Comprobamos que se ha introducido una cadena para el segundo apellido
	while(apellido2 == ""):
		print("Introduce el segundo apellido del nuevo contacto:")
		apellido2 = input()

	#Comprobamos que se ha introducido una sucesión de dígitos para el teléfono
	while(telefono.isdigit() == False):
		print("Introduce el teléfono del nuevo contacto:")
		telefono = input()

	#Solicitamos introducir la dirección
	print("Introduce la dirección del nuevo contacto:")
	direccion = input()

	#Comprobamos que se ha introducido una sucesión de dígitos para el código postal
	while(cp.isdigit() == False):
		print("Introduce el código postal del nuevo contacto:")
		cp = input()

	#Solicitamos introducir la ciudad
	print("Introduce la ciudad del nuevo contacto:")
	ciudad = input()

	#Solicitamos introducir el email
	print("Introduce el email del nuevo contacto:")
	email = input()

	#Generamos un objeto de la clase contacto y hacemos la llamada para insertarlo en BD
	nuevoC = contacto.Contacto(nombre, apellido1, apellido2, telefono, direccion, cp, ciudad, email)
	print("")
	if(controller.anyadirContacto(nuevoC) == False):
		print("Ha habido un error al insertar el contacto. Por favor, revisa los datos y vuelve a intentarlo")
	else:
		print("Contacto insertado correctamente")

	print("")
	print("Pulsa una tecla para continuar")
	input()

def modificarContacto(controller):
	#Mostramos la cabecera de la aplicación y la cabecera de la opción
	cabecera()
	print("---> MODIFICAR CONTACTO DE LA AGENDA <---")
	print("")

	#Solicitamos nombre y apellidos del contacto a modificar
	print("Nombre del contacto que deseas modificar")
	nombre = input()

	#Comprobamos que se ha introducido una cadena para el nombre
	while(nombre == ""):
		print("Nombre del contacto que deseas modificar")
		nombre = input()

	print("Apellido 1 del contacto que deseas modificar")
	apellido1 = input()

	#Comprobamos que se ha introducido una cadena para el primer apellido
	while(apellido1 == ""):
		print("Apellido 1 del contacto que deseas modificar")
		apellido1 = input()

	print("Apellido 2 del contacto que deseas modificar")
	apellido2 = input()

	#Comprobamos que se ha introducido una cadena para el segundo apellido
	while(apellido2 == ""):
		print("Apellido 2 del contacto que deseas modificar")
		apellido2 = input()

	#Ejecutamos el SELECT por nombre y apellidos sobre la tabla Contacto
	result = controller.selectContactoPorNomCompleto(nombre, apellido1, apellido2)

	#Mostramos los resultados por pantalla
	if(len(result) == 0):
		print("")
		print("No se han encontrado coincidencias. Pulse una tecla para continuar")
		input()
		return
	else:
		#Si hay más de 1 resultado coincidente, damos opción al usuario a cancelar la modificación
		if(len(result) > 1):
			print("Hay " + str(len(result)) + " registros coincidentes. ¿Desea continuar? (sí/NO)")
			opcion = input()
			if(opcion != "sí"):
				print("")
				print("No se ha modificado ningún registro. Pulse una tecla para continuar")
				input()
				return
			
		newC = contacto.Contacto()

		print("¿Deseas modificar el nombre? (s/NO)")
		modificar = input()
		if(modificar == "s"):
			print("Introduce el nuevo valor para el nombre:")
			valor = input()
			newC.setNombre(valor)

		print("¿Deseas modificar el apellido 1? (s/NO)")
		modificar = input()
		if(modificar == "s"):
			print("Introduce el nuevo valor para el apellido 1:")
			valor = input()
			newC.setApellido1(valor)

		print("¿Deseas modificar el apellido 2? (s/NO)")
		modificar = input()
		if(modificar == "s"):
			print("Introduce el nuevo valor para el apellido 2:")
			valor = input()
			newC.setApellido2(valor)

		print("¿Deseas modificar el teléfono? (s/NO)")
		modificar = input()
		if(modificar == "s"):
			print("Introduce el nuevo valor para el teléfono:")
			valor = input()
			newC.setTelefono(valor)

		print("¿Deseas modificar la dirección? (s/NO)")
		modificar = input()
		if(modificar == "s"):
			print("Introduce el nuevo valor para la dirección:")
			valor = input()
			newC.setDireccion(valor)

		print("¿Deseas modificar el código postal? (s/NO)")
		modificar = input()
		if(modificar == "s"):
			print("Introduce el nuevo valor para el código postal:")
			valor = input()
			newC.setCodigoPostal(valor)

		print("¿Deseas modificar la ciudad? (s/NO)")
		modificar = input()
		if(modificar == "s"):
			print("Introduce el nuevo valor para la ciudad:")
			valor = input()
			newC.setCiudad(valor)

		print("¿Deseas modificar el email? (s/NO)")
		modificar = input()
		if(modificar == "s"):
			print("Introduce el nuevo valor para el email:")
			valor = input()
			newC.setEmail(valor)

		#Ejecutamos las modificaciones indicadas sobre el registro seleccionado
		modificado = controller.modificarContacto(nombre, apellido1, apellido2, newC)
		print("")
		if(modificado == True):
			print("Contacto modificado correctamente. Pulse una tecla para continuar")
		else:
			print("No se ha modificado ningún contacto. Pulse una tecla para continuar")
		
		input()

def eliminarContacto(controller):
	#Mostramos la cabecera de la aplicación y la cabecera de la opción
	cabecera()
	print("---> ELIMINAR CONTACTO DE LA AGENDA <---")
	print("")

	#Solicitamos nombre y apellidos del contacto a eliminar
	print("Nombre del contacto que deseas eliminar")
	nombre = input()

	#Comprobamos que se ha introducido una cadena para el nombre
	while(nombre == ""):
		print("Nombre del contacto que deseas eliminar")
		nombre = input()

	print("Apellido 1 del contacto que deseas eliminar")
	apellido1 = input()

	#Comprobamos que se ha introducido una cadena para el primer apellido
	while(apellido1 == ""):
		print("Apellido 1 del contacto que deseas eliminar")
		apellido1 = input()

	print("Apellido 2 del contacto que deseas eliminar")
	apellido2 = input()

	#Comprobamos que se ha introducido una cadena para el segundo apellido
	while(apellido2 == ""):
		print("Apellido 2 del contacto que deseas eliminar")
		apellido2 = input()

	#Ejecutamos el SELECT por nombre y apellidos sobre la tabla Contacto
	result = controller.selectContactoPorNomCompleto(nombre, apellido1, apellido2)

	#Mostramos los resultados por pantalla
	if(len(result) == 0):
		print("")
		print("No se han encontrado coincidencias. Pulse una tecla para continuar")
		input()
		return
	else:
		#Si hay más de 1 resultado coincidente, damos opción al usuario a cancelar la eliminación
		if(len(result) > 1):
			print("Hay " + str(len(result)) + " registros coincidentes. ¿Desea continuar? (sí/NO)")
			opcion = input()
			if(opcion != "sí"):
				print("")
				print("No se ha borrado ningún registro. Pulse una tecla para continuar")
				input()
				return

		#Ejecutar la eliminación del registro indicado
		controller.borrarContacto(nombre, apellido1, apellido2)
		print("")
		print("Contacto eliminado correctamente. Pulse una tecla para continuar")
		input()

def mostrarResultados(result):
	for row in result:
		id = row[0]
		telf = row[4]
		cp = row[6]

		print("%d" % (id) + " - " + row[1] + " " + row[2] + " " + row[3])
		print("    -> Teléfono: %d" % (telf))
		print("    -> Email: " + row[8])
		print("    -> Dirección: " + row[5] + " - %d" % (cp) + " - " + row[7])
		print("")

def msgSalir():
	print("Gracias por utilizar PyContactAgenda. Saliendo del programa ahora...")
	input()

if __name__ == "__main__":
    main()
