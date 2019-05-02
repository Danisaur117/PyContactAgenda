#!C:\Program Files\Python37\python.exe

from src import Controller as kernel

controller = kernel.Controller()
controller.initDB()

result = controller.selectAll()

print("Registros: " + str(len(result)))

for row in result:
	print(row)