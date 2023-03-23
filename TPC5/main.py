import re
from Maquina import Maquina


def main():

    maquina = Maquina() # Máquina de Estados

    print("\nTPC5 - Processamento de Linguagens - 2023")
    print("Guilherme Martins - a92847 - LEI\n")

    print("-| CABINE TELEFÓNICA |-\n")
    print("maq: Opções possíveis para escrever (ignorar os ;):")
    print("-> LEVANTAR; POUSAR; MOEDA $c, $e. (tem de ter um ponto no final);")
    print("-> T=<o número deve ter 9 dígitos excepto se for iniciado por '0'>; ABORTAR")

    perguntar = 1
    while perguntar:
        opcao = input()
        # A vanatgem destes matches é que o início da expressão é que tem de estar correto
        # pode ter erros a seguir, mas são ignorados!
        m1 = re.match(r'^LEVANTAR$', opcao)
        m2 = re.match(r'^POUSAR$', opcao)
        m3 = re.match(r'^MOEDA(\s+\d+[e|c],)*\s+\d+[e|c]\.$', opcao) # ver estrutura: MOEDA 10c, 30c, 50c, 2e.
        m4_1 = re.match(r'^T=(00\d+)$', opcao) # o número deve ter 9 dígitos excepto se for iniciado por "00"
        m4_2 = re.match(r'T=(\d{9})$', opcao)
        m5 = re.match(r'^ABORTAR$', opcao) 

        if m1: maquina.levantar()
        elif m2: 
            maquina.pousar()
            perguntar = 0
        elif m3: 
            maquina.adicionarMoedas(opcao)
        elif m4_1:
            maquina.t(m4_1[1])
        elif m4_2:
            maquina.t(m4_2[1])
        elif m5:
            maquina.abortar()
            perguntar = 0
        else:
            print('!!! Opção errada !!!')
            print('maq: "!!! Opção errada !!! (Por favor escreva uma das seguintes opções: )')
            print("-> LEVANTAR; POUSAR; MOEDA $c, $e. (tem de ter um ponto no final);")
            print('-> T=<o número deve ter 9 dígitos excepto se for iniciado por \'00\'>; ABORTAR"')
    print("\nFIM do programa\n")

if __name__ == '__main__':
    main()