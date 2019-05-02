import configparser
from mysql import connector

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
		#TODO : FIX SELECT STATEMENT
		#SELECT de todos los contactos de la agenda que coincidan con el apellido indicado
		mycursor = self.__database.cursor()
		mycursor.execute("SELECT * FROM contacto WHERE (apellido1 LIKE '%s' OR apellido2 LIKE '%s'" % (apellido, apellido))
		print(mycursor.statement)
		result = mycursor.fetchall()
		mycursor.close()
		return result

	def selectContactoPorNomCompleto(self, nombre, apellido1, apellido2):
		#TODO : FIX SELECT STATEMENT
		#SELECT de todos los contactos de la agenda que coincidan con el nombre y apellidos
		#indicados
		mycursor = self.__database.cursor()
		mycursor.execute("SELECT * FROM contacto WHERE nombre LIKE '%s' AND (apellido1 LIKE '%s' OR apellido2 LIKE '%s')" % (nombre, apellido1, apellido2))
		print(mycursor.statement)
		result = mycursor.fetchall()
		mycursor.close()
		return result
