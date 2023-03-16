import re


# variáveis globais
levantou = 0 # inicialmente, nada foi levantado

    

# LEVANTAR
def levantar(): # marca início de interação
    global levantou 
    levantou = 1

# POUSAR
def pousar():

# MOEDA $c, $e  ||   MOEDA <lista de valores>
def moeda(string_moeda):
    preco_total = 0.0

    # EXEMPLO: MOEDA 10c, 30c, 50c, 2e. (CUIDADO com o ponto final)
    pos_moeda = string_moeda[6:]
    moedas = pos_moeda.split('.')[0].split(',')

    # Moedas válidas: 1 cêntimo (1c), 2 cêntimos (2c), 5 cêntimos (5c), 10 cêntimos (10c), 20 cêntimos (20c)
    # 50 cêntimos (50c), 1 euro (1e), 2 euros (2e)

    for md in moedas:
        if 'c' in md:

        elif 'e' in md: 

    m = re.match(r'', string_moeda)


def t():


def main():

    print("\n\nTPC5 - Processamento de Linguagens - 2023")
    print("Guilherme Martins - a92847 - LEI\n")

    print("ATENÇÃO: O programa só funciona para strings fornecidas válidas!\n")

    print("-| CABINE TELEFÓNICA |-\n")
    print("Opções possíveis para escrever (ignorar os ;):")
    print("LEVANTAR; POUSAR; MOEDA $c, $e. (tem de ter um ponto no final);")

    perguntar = 1
    while perguntar:
        opcao = input()

        m1 = re.match(r'^LEVANTAR', opcao)
        m2 = 
        m3 = re.match(r'^MOEDA', opcao)

        if m1: # LEVANTAR
            if levantou: print("\n!!! Não pode levantar  !!!\n")
            else: levantar()
        else:
            print("\n !!! Opção errada !!!")
            print("(Por favor escreva uma das seguintes opções: )")
    print("\nFIM do programa\n")

if __name__ == '__main__':
    main()