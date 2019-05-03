class Contacto:
	def __init__(self, nombre = "", apellido1 = "", apellido2 = "", telefono = 0, direccion  = "",
	codigoPostal = 0, ciudad = "", email = ""):
		self.__nombre = nombre
		self.__apellido1 = apellido1
		self.__apellido2 = apellido2
		self.__telefono = telefono
		self.__direccion = direccion
		self.__codigoPostal = codigoPostal
		self.__ciudad = ciudad
		self.__email = email

	def getNombre(self):
		return self.__nombre
	
	def setNombre(self, nombre):
		self.__nombre = nombre

	def getApellido1(self):
		return self.__apellido1
	
	def setApellido1(self, apellido):
		self.__apellido1 = apellido

	def getApellido2(self):
		return self.__apellido2
	
	def setApellido2(self, apellido):
		self.__apellido2 = apellido

	def getTelefono(self):
		return self.__telefono
	
	def setTelefono(self, telefono):
		self.__telefono = telefono

	def getDireccion(self):
		return self.__direccion
	
	def setDireccion(self, direccion):
		self.__direccion = direccion
	
	def getCodigoPostal(self):
		return self.__codigoPostal
	
	def setCodigoPostal(self, cp):
		self.__codigoPostal = cp

	def getCiudad(self):
		return self.__ciudad
	
	def setCiudad(self, ciudad):
		self.__ciudad = ciudad

	def getEmail(self):
		return self.__email
	
	def setEmail(self, email):
		self.__email = email

	def esPorDefecto(self):
		if(self.__nombre == ""):
			return False

		if(self.__apellido1 == ""):
			return False
		
		if(self.__apellido2 == ""):
			return False

		if(self.__telefono == 0):
			return False

		if(self.__direccion == ""):
			return False

		if(self.__codigoPostal == 0):
			return False

		if(self.__ciudad == ""):
			return False

		if(self.__email == ""):
			return False

		return True

	def toString(self):
		self.__nombre + " " + self.__apellido1 + " " + self.__apellido2 + " " + str(self.__telefono) + " " + self.__direccion + " " + str(self.__codigoPostal) + " " + self.__ciudad + " " + self.__email