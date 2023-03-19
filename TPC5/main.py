import re
import Maquina


def main():

    maquina = Maquina() # Máquina de Estados

    print("\n\nTPC5 - Processamento de Linguagens - 2023")
    print("Guilherme Martins - a92847 - LEI\n")

    print("ATENÇÃO: O programa só funciona para strings fornecidas válidas!\n")

    print("-| CABINE TELEFÓNICA |-\n")
    print("maq: Opções possíveis para escrever (ignorar os ;):")
    print("-> LEVANTAR; POUSAR; MOEDA $c, $e. (tem de ter um ponto no final);")
    print("-> T=<o número deve ter 9 dígitos excepto se for iniciado por '0'>; ABORTAR")

    perguntar = 1
    while perguntar:
        opcao = input()
        # A vanatgem destes matches é que o início da expressão é que tem de estar correto
        # pode ter erros a seguir, mas são ignorados!
        m1 = re.match(r'^LEVANTAR', opcao)
        m2 = re.match(r'^POUSAR', opcao)
        m3 = re.match(r'^MOEDA(\s+[ec][,\.])+', opcao) # ver estrutura 
        m4 = re.match(r'T=((00)?\d{9,})', opcao) # o número deve ter 9 dígitos excepto se for iniciado por "00"
        m5 = re.match(r'^ABORTAR', opcao)

        if m1: maquina.levantar()
        elif m2: 
            maquina.pousar()
            perguntar = 0
        elif m3: 
            maquina.adicionarMoedas(opcao)
        elif m4:
            maquina.t(m4[1])
        elif m5:
            maquina.abortar()
            perguntar = 0
        else:
            print("\n !!! Opção errada !!!")
            print("maq: (Por favor escreva uma das seguintes opções: )")
            print("-> LEVANTAR; POUSAR; MOEDA $c, $e. (tem de ter um ponto no final);")
            print("-> T=<o número deve ter 9 dígitos excepto se for iniciado por '0'>; ABORTAR")
    print("\nFIM do programa\n")

if __name__ == '__main__':
    main()