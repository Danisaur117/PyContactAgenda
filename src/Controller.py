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
