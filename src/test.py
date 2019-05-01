from Controller import Controller

controller = Controller()
controller.initDB()

result = controller.selectAll()

for row in result:
	print(row)