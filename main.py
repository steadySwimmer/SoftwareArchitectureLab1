from Controller import Controller
from Model import Model

model = Model('storage')

model.load()

controller = Controller(model)

controller.start()

model.save()