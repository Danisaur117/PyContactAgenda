Agenda de Contactos implementada en Python con almacenamiento de datos en una base de datos MySQL

Observaciones:
- PyContactAgenda requiere tener instalado Python y mysql-connector para Python instalado:
	python -m pip install mysql-connector
- El script para crear la base de datos MySQL, las tablas y volcar algunos datos de ejemplo se encuentra en el directorio resources
- Para configurar los datos de conexión a la BD MySQL es necesario modificar el archivo config/bd.cfg.example con los datos adecuados y quitarle la extensión .example al nombre del archivo
- Para lanzar el programa se debe ejecutar el script PyContactoAgenda.py