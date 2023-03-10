import math
import numpy as np
import matplotlib.pyplot as plt


# TPC1: Análise de dados: doença cardíaca
# Descarregue o ficheiro de dados: myheart.csv 
# Crie um programa em Python, conjunto de funções, que responda às seguintes questões:

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# 1)
# Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória;
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

class Dados:

    def __init__(self, pessoas, max_idade, min_colesterol, max_colesterol, total_doenca, total_n_doenca, total):
        self.pessoas = pessoas # lista das pessoas, com os seus respetivos dados
        self.max_idade = max_idade
        self.min_colesterol = min_colesterol
        self.max_colesterol = max_colesterol
        self.total_doenca = total_doenca
        self.total_n_doenca = total_n_doenca
        self.total = total

class Pessoa:

    def __init__(self, idade, sexo, colesterol, temDoenca):
        self.idade = idade
        self.sexo = sexo
        self.colesterol = colesterol
        self.temDoenca = temDoenca

def read_myheart(): # Devolve lista dos dados das pessoas
    listaPessoas = [] # lista dos dados das pessoas

    min_idade = math.inf
    max_idade = 0 # var auxiliar para calcular o limite superior das idades
    min_colesterol = math.inf
    max_colesterol = 0 # calcular lims inf e sup das tensões
    total_doenca = 0
    total_n_doenca = 0
    total = 0

    f = open("myheart.csv",'r')
    
    # Ignorar 1ª linha
    linha1 = f.readline()

    # Parsing do conteúdo
    linhas = f.readlines()
    for linha in linhas:
        valores =  linha.split('\n')[0].split(',')

        colesterol = int(valores[3])
        # eliminar valores que não fazem sentido (colesterol = 0)
        if colesterol > 0: 
            idade = int(valores[0])
            temDoenca = int(valores[5])
            pessoa = Pessoa(idade, valores[1], colesterol, temDoenca)
            listaPessoas.append(pessoa)
            total += 1

            # Conjunto de verificações
            #idade
            if idade > max_idade: max_idade = idade
            #colesterol
            if colesterol < min_colesterol: min_colesterol = colesterol
            elif colesterol > max_colesterol: max_colesterol = colesterol
            # doenca
            if temDoenca == 1: total_doenca += 1
            else: total_n_doenca += 1

    # Fechar ficheiro
    f.close()

    dados = Dados(listaPessoas, max_idade, min_colesterol, max_colesterol, total_doenca, total_n_doenca, total)
    return dados

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# 2)
# Pense num modelo para guardar uma distribuição;
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# exemplo: <Nome Variavel> | Tem Doenca | Sem Doenca | Total
        #  (...)
        #  Total | <Total Doença> | <Total Sem Doença> | <Total>

class DistribuicaoClasses: # semelhante a um histograma (valores contínuos)

    def __init__(self, titulo, var):
        self.titulo = titulo
        self.var = var # variável que se quer relacionar com a doença
        self.classes = {} # imitar hash-table (com as várias classes contínuas criadas)
        self.total = 0
        self.total_doenca = 0
        self.total_n_doenca = 0

    def adicionar_classe(self, l_inf, l_sup):
        self.classes[(l_inf,l_sup)] = Classe(l_inf, l_sup)

    def aumenta_doenca(self, l_inf, l_sup):
        self.classes[(l_inf,l_sup)].aumenta_doenca()
        self.total_doenca += 1
        self.total += 1
    
    def aumenta_n_doenca(self, l_inf, l_sup):
        self.classes[(l_inf,l_sup)].aumenta_n_doenca()
        self.total_n_doenca += 1
        self.total += 1

    def dividir_valores(self):
        keys = self.classes.keys()
        for key in keys:
            classe = self.classes[key]
            classe.dividir_valores(self.total)
            self.classes[key] = classe

class Classe: # para classes contínuas (idade - escalões etários)

    def __init__(self, l_inf, l_sup):
        self.l_inf = l_inf   # limite INFERIOR
        self.l_sup = l_sup   # limite SUPERIOR
        # por agora, o valor que vai estar na tabela
        self.valor = [0,0,0]

    def aumenta_doenca(self):
        self.valor[0] += 1 # doença
        self.valor[2] += 1 # total
    
    def aumenta_n_doenca(self):
        self.valor[1] += 1 # sem doença
        self.valor[2] += 1 # total - linhas

    def dividir_valores(self, total):
        for i in range(0,3):
            self.valor[i] = self.valor[i] * 100 / total

class DistribuicaoSimples: # sem classes (sexo-doença)

    def __init__(self, titulo, var):
        self.titulo = titulo
        self.var = var # variável que se quer relacionar com a doença
        self.tabela = {}

    def adicionar_chave(self, chave):
        self.tabela[chave] = [0,0,0] # doença, sem doença, total-linha

    def aumenta_doenca(self,chave):
        (valor_d, valor_n_d, total_linha) = self.tabela[chave]
        valor_d += 1
        total_linha += 1
        self.tabela[chave] = (valor_d, valor_n_d, total_linha)
    
    def aumenta_n_doenca(self,chave):
        (valor_d, valor_n_d, total_linha) = self.tabela[chave]
        valor_n_d += 1
        total_linha += 1
        self.tabela[chave] = (valor_d, valor_n_d, total_linha)

    def dividir_valores(self, total):
        keys = self.tabela.keys()
        for key in keys:
            (v1, v2, v3) = self.tabela[key]
            self.tabela[key] = (v1 * 100 / total, v2 * 100 / total, v3 * 100 / total)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# 3)
# Crie uma função que calcula a distribuição da doença por sexo;
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def dist_doenca_sexo(dados):
    dist = DistribuicaoSimples("-| Distribuição da doença por sexo (em percentagem, %) |-","Sexo")
    dist.adicionar_chave("Masculino")
    dist.adicionar_chave("Feminino")

    pessoas = dados.pessoas
    for pessoa in pessoas:
        if pessoa.sexo == "M":
            if pessoa.temDoenca == 1:
                dist.aumenta_doenca("Masculino")
            else:
                dist.aumenta_n_doenca("Masculino")
        else:
            if pessoa.temDoenca == 1:
                dist.aumenta_doenca("Feminino")
            else:
                dist.aumenta_n_doenca("Feminino")
    
    dist.dividir_valores(dados.total)

    return dist

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# 4)
# Crie uma função que calcula a distribuição da doença por escalões etários. Considere os seguintes escalões: [30-34], [35-39], [40-44], ...
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def dist_doenca_etario(dados):
    # Tal como pedido no enunciado, só serão aceites idades a partir dos 30 anos
    lim_inf = 30 # diferença = 5
    max_idade = dados.max_idade

    dist = DistribuicaoClasses("-| Distribuição da doença por escalões etários (em percentagem, %) |-", "Idade")
    
    # Criar as várias classes (mas, sem preencher com os seus valores)
    while lim_inf <= max_idade :
        dist.adicionar_classe(lim_inf, lim_inf+4)
        #print(lim_inf)
        lim_inf += 5
    
    pessoas = dados.pessoas
    for pessoa in pessoas:
        idade = pessoa.idade
        if idade >= 30: # Tal como pedido no enunciado, só serão aceites idades a partir dos 30 anos
            ultimo_digito = idade % 5
            lim_inf = idade - ultimo_digito

            if pessoa.temDoenca == 1:    
                dist.aumenta_doenca(lim_inf, lim_inf + 4)
            else:
                dist.aumenta_n_doenca(lim_inf, lim_inf + 4)
    
    # Calcular percentagem para cada classe
    dist.dividir_valores()

    return dist

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# 5)
# Crie uma função que calcula a distribuição da doença por níveis de colesterol. 
# Considere um nível igual a um intervalo de 10 unidades, comece no limite inferior e crie os níveis necessários até abranger o limite superior;
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def dist_doenca_colesterol(dados):
    lim_inf = dados.min_colesterol - (dados.min_colesterol % 10) # diferença = 10
    max_colesterol = dados.max_colesterol

    dist = DistribuicaoClasses("-| Distribuição da doença por níveis de colesterol (em percentagem, %) |-", "Colesterol")
    
    # Criar as várias classes (mas, sem preencher com os seus valores)
    while lim_inf <= max_colesterol :
        dist.adicionar_classe(lim_inf, lim_inf+9)
        #print(lim_inf)
        lim_inf += 10
    
    pessoas = dados.pessoas
    for pessoa in pessoas:
        colesterol = pessoa.colesterol
        ultimo_digito = colesterol % 10
        lim_inf = colesterol - ultimo_digito
        
        if pessoa.temDoenca == 1:    
            dist.aumenta_doenca(lim_inf, lim_inf+9)
        else:
            dist.aumenta_n_doenca(lim_inf, lim_inf+9)
    
    dist.dividir_valores()

    return dist

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# 6)
# Crie uma função que imprime na forma de uma tabela uma distribuição;
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def imprimir_distribuicao(dist, dados): # sob forma de tabela
    print("")
    print(dist.titulo)
    print("")
    print(dist.var + " | Tem Doenca | Sem Doenca | Total")
    print("----------------------------------------------")

    if isinstance(dist, DistribuicaoClasses):
        keys = dist.classes.keys()
        for key in keys:
            classe = dist.classes[key]
            print("[" + str(classe.l_inf) + ", " + str(classe.l_sup) + "] | " + str(classe.valor[0]) + " % | " + str(classe.valor[1]) + " % | " + str(classe.valor[2]) + " %")
        print("Total | " + str(dist.total_doenca * 100 / dist.total) + " % | " + str(dist.total_n_doenca * 100 / dist.total) + " % | " + str(dist.total * 100 / dist.total) + " %\n")

    elif isinstance(dist, DistribuicaoSimples):
        keys = dist.tabela.keys()
        for key in keys:
            valor = dist.tabela[key]
            print(key + " | " + str(valor[0]) + " % | " + str(valor[1]) + " % | " + str(valor[2]) + " %")
        print("Total | " + str(dados.total_doenca * 100 / dados.total) + " % | " + str(dados.total_n_doenca * 100 / dados.total) + " % | " + str(dados.total * 100 / dados.total) + " %\n")

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# 7)
# Especifique um programa que ao executar apresenta as tabelas correspondentes às distribuições pedidas;
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def main():

    print("\nTPC1 - Processamento de Linguagens - 2023")
    print("Guilherme Martins - a92847 - LEI")

    dados = read_myheart() # dados do csv
    #print("Parsing dos dados concluído\n")
    
    dist_sexo = dist_doenca_sexo(dados)
    dist_etario = dist_doenca_etario(dados)
    dist_colesterol = dist_doenca_colesterol(dados)
    #print("Cálculo das distribuições concluído\n")

    sair = 1

    # Interface do programa
    while sair :

        print("\n--------------------")
        print("| Opcoes possíveis |")
        print("--------------------\n")
        print("1 - Distribuição da doença por sexo")
        print("2 - Distribuição da doença por escalões etários")
        print("3 - Distribuição da doença por níveis de colesterol")
        print("4 - (matplotlib) Distribuição da doença por sexo")
        print("5 - (matplotlib) Distribuição da doença por escalões etários")
        print("6 - (matplotlib) Distribuição da doença por níveis de colesterol")
        print("0 - Sair")
        opcao = int(input("\nEscreva a opção desejada: "))
        
        # 1 - Distribuição da doença por sexo
        if opcao == 1:
            imprimir_distribuicao(dist_sexo, dados)
        # 2 - Distribuição da doença por escalões etários
        elif opcao == 2:
            imprimir_distribuicao(dist_etario, dados)
        # 3 - Distribuição da doença por níveis de colesterol
        elif opcao == 3:
            imprimir_distribuicao(dist_colesterol, dados)
        # 4 - (matplotlib) Distribuição da doença por sexo
        elif opcao == 4:
            graficos_dists(dist_sexo, dados)
        # 5 - (matplotlib) Distribuição da doença por escalões etários
        elif opcao == 5:
            graficos_dists(dist_etario, dados)
        # 6 - (matplotlib) Distribuição da doença por níveis de colesterol
        elif opcao == 6:
            graficos_dists(dist_colesterol, dados)
        # 0 - Sair
        elif opcao == 0: 
            sair = 0

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# 8)
# Extra: explore o módulo matplotlib e crie gráficos para as suas distribuições.
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def graficos_dists(dist, dados):

    # https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    classes = []
    colunas = {"Tem Doença": (), "Sem Doença": (), "Total": ()}

    if isinstance(dist, DistribuicaoClasses):
        keys = dist.classes.keys()
        # temos de criar a string das chaves
        for (v1,v2) in keys:
            classe = dist.classes[(v1,v2)]
            classes.append("[" + str(v1) + ", " + str(v2) +"]")
            valor = classe.valor
            colunas["Tem Doença"] = colunas["Tem Doença"] +(valor[0],)
            colunas["Sem Doença"] = colunas["Sem Doença"] +(valor[1],)
            colunas["Total"] = colunas["Total"] +(valor[2],)
    elif isinstance(dist, DistribuicaoSimples):
        classes = list(dist.tabela.keys())
        for key in classes:
            # dist.tabela[key]
            colunas["Tem Doença"] = colunas["Tem Doença"] +(dist.tabela[key][0],)
            colunas["Sem Doença"] = colunas["Sem Doença"] +(dist.tabela[key][1],)
            colunas["Total"] = colunas["Total"] +(dist.tabela[key][2],)

    x = np.arange(len(classes))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(constrained_layout=True)

    for attribute, measurement in colunas.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Percentagem (%)')
    ax.set_title(dist.titulo)
    ax.set_xticks(x + width, classes)
    ax.legend(loc='upper left', ncols=3)
    if isinstance(dist, DistribuicaoClasses): 
        if dist.var == "Idade":  ax.set_ylim(0, 25)
        elif dist.var == "Colesterol":  ax.set_ylim(0, 10)
    elif isinstance(dist, DistribuicaoSimples): ax.set_ylim(0, 85)

    plt.show()

if __name__ == '__main__':
    main()