
from backend import BackEnd
class Main:
    def __init__(self):
        self.tarefas = []
        self.running = True
        self.correto = False
        self.manos = BackEnd()
        self.op1 = ["add", "mos","cont", "rem","ler" ,"quit", "ren", "grav"]
    def opções(self):
        print("*" * 16)
        self.manos.carregamento()
        for i, e in enumerate(self.op1):
            print(f"|{i}  - {e}    |")
        print("*" * 16)
    def tabelas(self):
        return ["Digite exit: \n", "Meu amigo\n"]
    def get_name(self):
        i = input("Digite o seu nome: ")
        return i
    def tars(self):
        for i in self.tarefas:
            return i
    def mostrar_tarefas(self):
        for i in range(len(self.op1)):
            print(f"Tarefas a serem escolhidas: {self.op1[i]}")
        for i in self.tarefas:
            print(i)
    def giro(self):
        i = input("O que vai ser? ")
        k = None
        try:
            for j in range(len(self.op1)):
                if self.op1[j] == i:
                    print("Acerto")
                    self.correto = True
            
            if self.correto:
                match i:
                    case "mos":
                        for i in range(len(self.tarefas)):
                            print(self.tarefas[i])
                    case "add":
                        k = input("quais: ")
                        self.tarefas.append(f"elas são: {i}: {[k]}")
                    case "rem":
                        self.tarefas.pop()
                    case "ren":
                        k = input("Quais: ")
                        for i in self.tarefas:
                            if k in i:
                                print("removendo: ")
                                self.tarefas.remove(i)
                    case "quit":
                        self.correto = False
                        quit()
                    case "cont":
                        self.giro()
                    case "grav":
                        with open("asa.txt", "w") as txt:
                            for i in range(len(self.tarefas)):
                                txt.write(f"tarefas: {self.tarefas[i]}")
                    case "ler":
                        self.manos.ler()
        except Exception as exc:
            print(f"Erros encontrados: {exc}")
        return i