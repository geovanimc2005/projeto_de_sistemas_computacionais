#programado por Geovani Moura Coratti
from backend import BackEnd
'''
esta é a parte principal do programa, pois ela é quem vai identificar os elementos que devem ser escolhidos e quais devem ser organizados a fim de achar o resultado adequado
ela é basicamente o front-end, para fins de simplicidade e de funcionalidade ele apenas será uma arquivo que chama o file backend
ele é o que organiza o que deverá ser feitos. por assim dizer.
'''
class Main:
    def __init__(self):
        self.tarefas = []
        self.running = True
        self.correto = False
        self.manos = BackEnd()
        #todas as opções possiveis, se digitar algo que não está aqui, não poderá ir para a frente.
        self.op1 = ["add", "mos","cont", "rem","ler" ,"quit", "ren", "grav"]
    #esta função é apenas aonde a barra de carregamento e o menu mpinripal devem ser mostrados a fim de fazer funcionar a identificação dos elementos
    def opções(self):
        print("*" * 16)
        self.manos.carregamento()
        for i, e in enumerate(self.op1):
            print(f"|{i}  - {e}    |")
        print("*" * 16)
    def tabelas(self):
        return ["Digite exit: \n", "Meu amigo\n"]
    #função simplificada, apenas para poder pegar o nome dos usuarios e depois poder funcionar como um meio de identificar o input primordial
    def get_name(self):
        i = input("Digite o seu nome: ")
        return i
    #subrotina feita apenas para poder fazer rodar e caso seja necessario ler todos os elementos, em antigas iterações ela apresentava um papel mais importante.
    def tars(self):
        for i in self.tarefas:
            return i
    def mostrar_tarefas(self):
        for i in range(len(self.op1)):
            print(f"Tarefas a serem escolhidas: {self.op1[i]}")
        for i in self.tarefas:
            print(i)
    def giro(self):
        #escolha do proximo elemento
        i = input("O que vai ser? ")
        k = None
        try:
            for j in range(len(self.op1)):
                if self.op1[j] == i:
                    print("Acerto")
                    self.correto = True
                    #caso exista na lista
            #se existir pode continuar
            if self.correto:
                match i:
                    case "mos":
                        #mostrar apenas os nomes da lista, substituindo o tars.
                        for i in range(len(self.tarefas)):
                            print(self.tarefas[i])
                    case "add":
                        #apenas adiciona algun comando para ele
                        k = input("quais: ")
                        self.tarefas.append(f"elas são: {i}: {[k]}")
                    case "rem":
                        #apenas retira o ultimo nome da lista, caso mencionado.
                        self.tarefas.pop()
                    case "ren":
                        #caso digitado, o usuario terá de escolher se um destes elementos deverá ser eliminado
                        k = input("Quais: ")
                        for i in self.tarefas:
                            if k in i:
                                print("removendo: ")
                                self.tarefas.remove(i)
                    case "quit":
                        #fechar o programa de sua execução
                        self.correto = False
                        quit()
                    case "cont":
                        #reiniciar
                        self.giro()
                    case "grav":
                        #neste caso ele irá sobre escrever os dados do arquivo, apagando a necessidade de um comando, reescrever.
                        with open("asa.txt", "w") as txt:
                            for i in range(len(self.tarefas)):
                                txt.write(f"tarefas: {self.tarefas[i]}")
                    case "ler":
                        self.manos.ler()
        except Exception as exc:
        #feito com o unico motivo de impedir os crashs em caso de erro nos inputs.
            print(f"Erros encontrados: {exc}")
        return i
