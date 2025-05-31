from backend import BackEnd
from main import Main

class principal:
    def __init__(self):
        self.run = True
        self.get = Main()
        self.set = BackEnd()
        self.asa = None
    def running(self):
        self.get.opções()
        self.get.get_name()
        self.set.data_banks()
        while self.run:
            self.get.giro()
if __name__ == "__main__":
    main = principal()
    main.running()