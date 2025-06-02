import os
import sys
from tqdm import tqdm
import time
import json
#detalhe que o use de json que era mais presente em iterações anteriores do codigo foi simplificado, pois foi visto que um arquivo txt faz a mesma coisa e de forma mais simples e que se adequa aos iniciantes da faculdade de computação.
#este é o backend aonde o codigo vai fazer uma intermediação, para que se possa ler os arquivos, e mandar eles para o banco de dados ou neste caso uma folha do tipo txt.
class BackEnd:
    def data_banks(self):
        i = input("nombre: ")
        with open("asaa.txt", "w") as txt:
            txt.write(f"Nomes: {i} ")
    #esta função, apenas ler o codigo que estava marcado no outro arquivo no file asa.txt e ainda assim o imprime, para que se possa ver o que está acontecendo
    def ler(self):
        try:
            with open("asa.txt", "r") as txt:
                asa = txt.read()
                aaa = json.dumps(asa)
                print(asa)
                return aaa
        except Exception as exc:
            print(exc)
    #barra de carregamento feito apenas para fins esteticos, e não apresenta nenhuma função de fato que interfere na qualidade do programa.
    def carregamento(self):
        with tqdm(total=100) as pt:
            for i in range(100):
                time.sleep(0.01)
                pt.update(1)
                if i == 25:
                    pt.set_postfix({"Concluido" : "no meio do caminho"})
            #mosta o que acabou
            pt.set_description("Acabado")
