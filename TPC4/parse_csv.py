import re
import json


# NOTA: TODAS as opções podem estar misturadas no mesmo CSV
# Função ÚNICA para todas as extensões possíveis
# ATENÇÃO: 
def csv_json(filename):
    directory = "csv_testes/" + filename
    f = open(directory,'r')

    #  Split dos vários campos da 1ª linha
    linha1 = f.readline()
    nomes_campos = [] # lista
    numero_vezes_campos = {} # dicionário (campo -> lista número [lim_inf, lim_sup]) 
    funcoes_campos = {} # dicionário (campo -> função)
    campos = linha1.split(',')
    for campo in campos:
        if not (len(campo) == 0 or campo == "\n"): # Ignorar campo quando o que está dentro dos () é válido
            # Campo aceite - temos de saber quantas colunas cada campo possui
            # Verificar extensão utilizada
            # Listas
            match1 = re.match(r'^(\w+){(\d)}\n?$', campo) # grupo de captura do número dentro do {}
            if match1:
                nomes_campos.append(match1[1])
                numero_vezes_campos[match1[1]] = [int(match1[2])]
                # não se adiciona função a esse campo
            else:
                # Lista com intervalo de tamanhos
                match2 = re.match(r'^(\w+){(\d),(\d)}\n?$', campo)
                if match2:
                    nomes_campos.append(match1[1])
                    numero_vezes_campos[match1[1]] = [int(match1[2]), int(match1[3])]
                else:
                    # Funções de agregação
                    match3 = re.match(r'^(\w+){(\d),(\d)}::(\w+)\n?$', campo)
                    if match3:
                        nomes_campos.append(match1[1])
                        numero_vezes_campos[match1[1]] = [int(match1[2]), int(match1[3])]
                        funcoes_campos[match1[1]] = [int(match1[4])]
                    # Se não tiver nenhuma extensão, simplesmente adiciona-se ao dicionário
                    else:
                        nomes_campos.append(campo.split('\n')[0])


    list = [] # guardam-se os vários dicionários

    # Ler as outras linhas
    linhas = f.readlines()

    for linha in linhas:
        i = 0
        index_nome = 0
        valores = linha.split(',')
        length = len(linha)
        dict = {} # dicionário onde serão guardados os vários dados da linha para o json
        while i < length : # enquanto os vários valores não forem todos analisados
            nome = nomes_campos[index_nome]
            index_nome += 1
            valores_campo = []
            lim_inf = 0
            lim_sup = 0 # apenas temporário

            #Ver o número de colunas para o campo atual
            if nome in numero_vezes_campos:
                l = numero_vezes_campos[nome]
                if len(l) == 1:
                    lim_inf = l[0]
                    lim_sup = l[0]
                else:
                    lim_inf = l[0]
                    lim_sup = l[1]
            else:
                lim_inf = 1
                lim_sup = 1 # apenas 1 coluna

            # valores obrigatórios da lista
            for n in range(0, lim_inf):
                # valores[i] = valores[i].split('\n')[0]
                if valores[i].isnumeric(): valores_campo.append(int(valores[i]))
                else: valores_campo.append(valores[i])
                i += 1

            # pode acontecer que a linha tenha valores não obrigatórios
            for n in range(lim_inf, lim_sup+1):
                # valores[i] = valores[i].split('\n')[0]
                if len(valores[i]) > 0:
                    if valores[i].isnumeric(): valores_campo.append(int(valores[i]))
                    else: valores_campo.append(valores[i])
                i += 1

            # aplicar função (se existe)
            if nome in funcoes_campos:
                funcao = funcoes_campos[nome]
                if funcao == "sum":
                    sum = 0
                    for num in valores_campo:
                        sum += num
                    dict[nome] = sum

                elif funcao == "media":
                    media = 0
                    n_total = len(valores_campo)
                    for num in valores_campo:
                        media += num
                    media /= n_total
                    dict[nome] = media

                # se não tiver função, adicionamos todos os valores (em forma de lista) ao dicionário
                else: dict[nome] = valores_campo
        
        list.append(dict)


    create_json(dict, filename)


# Converter um dicionário num ficheiro JSON (https://pythonexamples.org/python-write-json-to-file/)
def create_json(list, filecsv):
    filename = filecsv.split('.')[0]
    directory = "resultados_json/" + filename + ".json"
    jsonFile = open(directory, "w")
    for l in list:
        jsonString = json.dump(list)
        jsonFile.write(jsonString)
    jsonFile.close()


# CSV normal

# Número,Nome,Curso
# 3162,Cândido Faísca,Teatro
# 7777,Cristiano Ronaldo,Desporto
# 264,Marcelo Sousa,Ciência Política

# Listas

# Número,Nome,Curso,Notas{5},,,,,
# 3162,Cândido Faísca,Teatro,12,13,14,15,16
# 7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
# 264,Marcelo Sousa,Ciência Política,18,19,19,20,18

# Listas com um intervalo de tamanhos

# Número,Nome,Curso,Notas{3,5},,,,,
# 3162,Cândido Faísca,Teatro,12,13,14,,
# 7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
# 264,Marcelo Sousa,Ciência Política,18,19,19,20,

# Funções de agregação

# Número,Nome,Curso,Notas{3,5}::sum,,,,,
# 3162,Cândido Faísca,Teatro,12,13,14,,
# 7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
# 264,Marcelo Sousa,Ciência Política,18,19,19,20,

# Número,Nome,Curso,Notas{3,5}::media,,,,,
# 3162,Cândido Faísca,Teatro,12,13,14,,
# 7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
# 264,Marcelo Sousa,Ciência Política,18,19,19,20,