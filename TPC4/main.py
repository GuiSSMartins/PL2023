from genericpath import exists
from parse_csv import csv_json

# TPC4

# Cria um programa em Python que implementa um conversor de um ficheiro CSV (Comma separated values) para o formato JSON.

def main():

    perguntar = 1
    while perguntar:
        print("\n\nTPC4 - Processamento de Linguagens - 2023")
        print("Guilherme Martins - a92847 - LEI\n")

        print("-| Conversor de CSV para JSON |-")
        print("1) CSV 'normal' (sem extensões) - alunos.csv")
        print("2) Listas - alunos2.csv")
        print("3) Listas com um intervalo de tamanhos - alunos3.csv")
        print("4) Funções de agregação - alunos4.csv")
        print("5) Funções de agregação - alunos5.csv")
        print("6) CSV feito por mim (contém todas as extensões) - alunosMe.csv")
        print("7) Qualquer CSV (tem de escrever o nome do ficheiro CSV)")
        print("0) - SAIR\n")

        opcao = int(input("Escreva aqui o número da opção desejada: "))

        if opcao == 1: csv_json("alunos.csv")
        elif opcao == 2: csv_json("alunos2.csv")
        elif opcao == 3: csv_json("alunos3.csv")
        elif opcao == 4: csv_json("alunos4.csv")
        elif opcao == 5: csv_json("alunos5.csv")
        elif opcao == 6: csv_json("alunosMe.csv")
        elif opcao == 7:
            invalido = 1
            while invalido:
                print("\n(É necessário escrever .csv no final & tem de garantir que está dentro da pasta 'csv_testes')")
                filename = input("Escreva o nome do ficheiro (incluindo .csv no final): ")
                directory = "csv_testes/" + filename
                if exists(directory):
                    invalido = 0
                    csv_json(filename)
                else:
                    print("\nO fichceiro não existe! Por favor insira um nome de um ficheiro VÁLIDO!\n")
        elif opcao == 0: perguntar = 0
        else:
            print("\n !!! Opção errada !!!\n")
    print("\nFIM do programa\n")

if __name__ == '__main__':
    main()