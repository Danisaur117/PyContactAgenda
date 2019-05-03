import configparser
import datetime
from mysql import connector
# import Contacto

class Controller:
	def __init__(self, database = None):
		self.__database = database

	# def getMyDB(self):
	# 	return self.__database

	# def setMyDB(self, db):
	# 	self.__database = db

	def initDB(self):
		#Leemos las opciones de configuración de BD del archivo
		config = configparser.ConfigParser()
		config.read('./config/bd.cfg')
		bdconfig = config['MYSQL_CONFIG']

		#Inicializamos la conexión a MySQL
		self.__database = connector.connect(
			host=bdconfig['host'],
			user=bdconfig['user'],
			passwd=bdconfig['passwd'],
			database=bdconfig['database'],
			auth_plugin=bdconfig['auth_plugin']
		)
	
	def selectAll(self):
		#SELECT de todos los contactos de la agenda
		mycursor = self.__database.cursor()
		mycursor.execute("SELECT * FROM contacto")
		result = mycursor.fetchall()
		mycursor.close()
		return result

	def selectContactoPorNombre(self, nombre):
		#SELECT de todos los contactos de la agenda que coincidan con el nombre indicado
		mycursor = self.__database.cursor()
		mycursor.execute("SELECT * FROM contacto WHERE nombre LIKE '%" + "%s" % (nombre) + "%'")
		result = mycursor.fetchall()
		mycursor.close()
		return result

	def selectContactoPorApellido(self, apellido):
		#SELECT de todos los contactos de la agenda que coincidan con el apellido indicado
		mycursor = self.__database.cursor()
		mycursor.execute("SELECT * FROM contacto WHERE (apellido1 LIKE '%" + "%s" % (apellido) + "%' OR apellido2 LIKE '%" + "%s" % (apellido) + "%')")
		result = mycursor.fetchall()
		mycursor.close()
		return result

	def selectContactoPorNomCompleto(self, nombre, apellido1, apellido2):
		#SELECT de todos los contactos de la agenda que coincidan con el nombre y apellidos
		#indicados
		mycursor = self.__database.cursor()
		mycursor.execute("SELECT * FROM contacto WHERE nombre LIKE '%" + "%s" % (nombre) + "%' AND (apellido1 LIKE '%" + "%s" % (apellido1) + "%' OR apellido2 LIKE '%" + "%s" % (apellido2) + "%')")
		result = mycursor.fetchall()
		mycursor.close()
		return result

	def anyadirContacto(self, contacto):
		#Añadir a la BD los datos del nuevo contacto pasados en el objeto "contacto". Devolvemos
		#true en caso de éxito y false en caso contrario
		mycursor = self.__database.cursor()
		select = "INSERT INTO contacto (nombre, apellido1, apellido2, telefono, direccion, codigoPostal, ciudad, email, lastUpdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		values = (contacto.getNombre(), contacto.getApellido1(), contacto.getApellido2(), contacto.getTelefono(), contacto.getDireccion(), contacto.getCodigoPostal(), contacto.getCiudad(), contacto.getEmail(), datetime.datetime.now())
		mycursor.execute(select, values)
		self.__database.commit()

		if(mycursor.rowcount == 0):
			return False
		else:
			return True