#TPC3: Processador de Pessoas listadas nos Róis de Confessados

# Construa agora um ou vários programas Python para  processar o texto 'processos.txt' (procurar o ficheiro no Bb) com o intuito de
# calcular frequências de alguns elementos (a ideia é utilizar arrays associativos, dicionários em Python, para o efeito):

# > a) Calcula a frequência de processos por ano (primeiro elemento da data);

# > b) Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos 
# e apresenta os 5 mais usados;

# > c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;

# > d) Converta os 20 primeiros registos num novo ficheiro de output mas em formato **Json**.




from a_tpc3 import a
from b_tpc3 import b
from c_tpc3 import c
from d_tpc3 import d
from dados import parsing

def main():

    
    print("\nTPC3 - Processamento de Linguagens - 2023")
    print("Guilherme Martins - a92847 - LEI")

    # Parsing dos dados
    dados = parsing()


    perguntar = 1
    while perguntar:
        print("\n-| Exercícios |-\n")
        print("1) - Exercício a): Calcula a frequência de processos por ano (primeiro elemento da data)")
        print("2) - Exercício b): Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados")
        print("3) - Exercício c): Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.")
        print("4) - Exercício d): onverta os 20 primeiros registos num novo ficheiro de output mas em formato **Json**")
        print("0) - SAIR\n")

        opcao = int(input("Escreva aqui apenas o número da opção desejada: "))
        if opcao == 1: a(dados)
        elif opcao == 2: b(dados)
        elif opcao == 3: c(dados)
        elif opcao == 4: d(dados)
        elif opcao == 0: perguntar = 0
        else:
            print("\n !!! Opção errada !!!\n")


if __name__ == '__main__':
    main()