from src import Controller as kernel

controller = kernel.Controller()
controller.initDB()

result = controller.selectAll()

for row in result:
	print(row)