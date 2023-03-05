from dados import Dados

# > a) Calcula a frequência de processos por ano (primeiro elemento da data);

def a(dados):
    print("\n-| Frequência de processos por ano |-\n")
    print("Ano | Frequência Absoluta")
    for ano in range(dados.lim_inf_ano_proc, dados.lim_sup_ano_proc + 1):
        if str(ano) in dados.freq_processos_ano:
            print(str(ano) + " : " + str(dados.freq_processos_ano[str(ano)]))