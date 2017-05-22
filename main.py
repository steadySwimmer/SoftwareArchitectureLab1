from Controller import Controller
from Model import Model

if __name__ == "__main__":
    model = Model('storage.txt')
    model.load()
    controller = Controller(model)
    controller.start()
    model.save()
