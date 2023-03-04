from dados import Dados, parsing

import json

# > d) Converta os 20 primeiros registos num novo ficheiro de output mas em formato **Json**.
# guardar os registos sob a forma de um dicionário
def d(dados):
    # https://pythonexamples.org/python-write-json-to-file/
    registos20 = dados.registos20 # dicionário
    jsonString = json.dumps(registos20)
    jsonFile = open("processos20.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    print("\nCriação do ficheiro 'processos20.json' concluído!\n")