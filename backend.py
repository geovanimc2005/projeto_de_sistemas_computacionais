import os
import sys
from tqdm import tqdm
import time
import json
class BackEnd:
    def data_banks(self):
        i = input("nombre: ")
        with open("asaa.txt", "w") as txt:
            txt.write(f"Nomes: {i} ")
    def ler(self):
        try:
            with open("asa.txt", "r") as txt:
                asa = txt.read()
                aaa = json.dumps(asa)
                print(asa)
                return aaa
        except Exception as exc:
            print(exc)
    def carregamento(self):
        with tqdm(total=100) as pt:
            for i in range(100):
                time.sleep(0.01)
                pt.update(1)
                if i == 25:
                    pt.set_postfix({"Concluido" : "no meio do caminho"})
            pt.set_description("Acabado")