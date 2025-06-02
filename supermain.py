from backend import BackEnd
from main import Main
# este arquivo é mais simplificado de uma forma ou de outra.
class principal:
    def __init__(self):
        self.run = True
        self.get = Main()
        self.set = BackEnd()
        self.asa = None
    def running(self):
        #função do loop principal, que faz funcionar o que deve ser executado, e chamando de forma sistematica o frontend no arquivo main.py
        self.get.opções()
        self.get.get_name()
        self.set.data_banks()
        while self.run:
            self.get.giro()
if __name__ == "__main__":
    main = principal()
    main.running()
