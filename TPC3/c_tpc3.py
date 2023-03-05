from dados import Dados

# > c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;

def c(dados):
    print("-| Frequência dos vários tipos de relação |-\n")
    print("-> Nº de MÃES: " + str(dados.n_maes))
    print("-> Nº de PAIS: " + str(dados.n_pais))
    print("-> Nº de FILHOS: " + str(dados.n_filhos))
    print("-> Nº de IRMÃOS: " + str(dados.n_irmaos))
    print("-> Nº de SOBRINHOS: " + str(dados.n_sobrinhos))