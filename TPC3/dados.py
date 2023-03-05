import math
import re

class Dados: # Todos os dados obtidos a partir do ficheiro "parsing.txt"
    def _init_(self):
        # exercício a) 
        # frequência do nº de processos por ano
        self.freq_processos_ano = {} # ano (key) -> nº de processos (value)
        self.lim_inf_ano_proc = math.inf
        self.lim_sup_ano_proc = 0

        # exercício b)
        # frequência de nomes próprios / apelidos por séculos
        self.freq_nomes_proprios = {} # seculo (key) -> { nome (key) -> nº (value) } (value)
        self.nomes_proprios = {}
        self.seculo_inf_proprios = math.inf
        self.seculo_sup_proprios = 0
        self.top5_proprios = []
        self.freq_apelidos = {} # seculo (key) -> { nome (key) -> nº (value) } (value)
        self.apelidos = {}
        self.seculo_inf_apelidos = math.inf
        self.seculo_sup_apelidos = 0
        self.top5_apelidos = []

        # exercício c)
        # frequência dos vários tipos de relação: irmão, sobrinho, etc.
        self.nomes_maes = []
        self.nomes_pais = []
        self.nomes_para_analisar = [] # apenas para evitar repetições de estudo de relações
        self.mae_pai = {} # pessoa (key) -> (mae, pai) (value)
        self.filhos = {} # (mae, pai) (key) -> [filhos] (value)
        self.n_maes = 0
        self.n_pais = 0
        self.n_filhos = 0
        self.n_irmaos = 0
        self.n_sobrinhos = 0

        # exercício d) 
        # guardar os 20 primerios registos sob a forma de um dicionário
        # de forma a ser compatível com o formato JSON
        self.registos20 = {} # chave :: número do registo ;; resto :: string
        self.n_registos = 0

    # exercício a)
    # Adicionar um processo por ano
    def adicionarProcessoAno(self, ano):
        if self.processos_ano.keys.contains(ano):
            freq = self.processos_ano[ano]
            freq += 1
            self.processos_ano[ano] = freq
        else:
            self.processos_ano[ano] = 1
        if ano < self.lim_inf_ano_proc: self.lim_inf_ano_proc = ano
        if ano > self.lim_sup_ano_proc: self.lim_sup_ano_proc = ano
    
    # exercício d)
    def adicionarRegisto20(self, linha_registo):
        self.n_registos += 1
        self.registos20[self.n_registos] = linha_registo


# CUIDADO: podem haves 2 ou mais processos com a mesma pasta
def parsing():
    dados = Dados()
    f = open("processos.txt",'r')

    # Parsing do conteúdo
    linhas = f.readlines()

    # Expressão Regular - Pasta | Data | Nome | Pai | Mãe | Observações
    er = re.compile(r'(?P<pasta>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>(\w+|\s+)+)::(?P<pai>(\w+|\s+)*)::(?P<mae>(\w+|\s+)*)::(?P<observacoes>(\w+|\s+)*)::')

    for linha in linhas:
        if linha != "": # tem de ter conteúdo
            registo = er.match(linha).groupdict()

            # (exercicio d) ) Verificar se é para adicionar aos primeiros 20 registos
            if dados.n_registos < 20:
                dados.adicionarRegisto20(linha)

            # (exercicio a) ) Frequência dos processos por ano
            ano = registo['ano']
            dados.adicionarProcessoAno(ano)
            seculo = calcular_seculo(ano)
            nome = registo['nome']
            mae = registo['mae']
            pai = registo['pai']

            if not any(nome for n in dados.nomes_para_analisar):
                dados.nomes_para_analisar.append(nome)
                dados.mae_pai[nome] = (mae, pai) 
                if dados.filhos.keys.contains((mae, pai)):
                    filhos = dados.filhos[(mae, pai)]
                    filhos.append(nome)
                else: dados.filhos[(mae, pai)] = [nome]
                
                if dados.filhos.keys.contains(mae):
                    filhos = dados.filhos[mae]
                    filhos.append(nome)
                else: dados.filhos[mae] = [nome]
                if dados.filhos.keys.contains(pai):
                    filhos = dados.filhos[pai]
                    filhos.append(nome)
                else: dados.filhos[pai] = [nome]

                # (exercicio b) organizar nomes próprios / apelidos por séculos
                # ---> Nome Próprio / Apelido (Nome)
                (proprio, apelido) = nome_proprio_apelido(nome)
                if proprio != "":
                    if dados.freq_nomes_proprios.keys.contains(seculo):
                        dict = dados.freq_nomes_proprios[seculo]
                        if dict.keys.contains(proprio):
                            dict[proprio] += 1
                            dados.freq_nomes_proprios[seculo] = dict
                    else: 
                        if seculo < dados.seculo_inf_proprios: dados.seculo_inf_proprios = seculo
                        if seculo > dados.seculo_sup_proprios: dados.seculo_sup_proprios = seculo 
                        dados.freq_nomes_proprios[seculo] = {proprio : 1}
                if apelido != "":
                    if dados.freq_apelidos.keys.contains(seculo):
                        dict = dados.freq_apelidos[seculo]
                        if dict.keys.contains(apelido):
                            dict[apelido] += 1
                            dados.freq_apelidos[seculo] = dict
                    else: 
                        if seculo < dados.seculo_inf_apelidos: dados.seculo_inf_apelidos = seculo
                        if seculo > dados.seculo_sup_apelidos: dados.seculo_sup_apelidos = seculo 
                        dados.freq_apelidos[seculo] = {proprio : 1}

                if dados.nomes_proprios.keys.contains(proprio):
                    dados.nomes_proprios[proprio] += 1
                else:
                    dados.top5_proprios.append(proprio)
                    dados.nomes_proprios[proprio] = 1
                if dados.apelidos.keys.contains(apelido):
                    dados.apelidos[apelido] += 1
                else:
                    dados.top5_apelidos.append(apelido)
                    dados.apelidos[apelido] = 1

            # (exercicio b) organizar nomes próprios / apelidos por séculos
            # ---> Nome Próprio / Apelido(Mãe)
            if mae != "" and mae not in dados.nomes_maes:
                dados.n_maes += 1
                dados.nomes_maes.append(mae)
                (proprio, apelido) = nome_proprio_apelido(mae)
                if proprio != "":
                    if dados.freq_nomes_proprios.keys.contains(seculo):
                        dict = dados.freq_nomes_proprios[seculo]
                        if dict.keys.contains(proprio):
                            dict[proprio] += 1
                            dados.freq_nomes_proprios[seculo] = dict
                    else: 
                        if seculo < dados.seculo_inf_proprios: dados.seculo_inf_proprios = seculo
                        if seculo > dados.seculo_sup_proprios: dados.seculo_sup_proprios = seculo 
                        dados.freq_nomes_proprios[seculo] = {proprio : 1}
                if apelido != "":
                    if dados.freq_apelidos.keys.contains(seculo):
                        dict = dados.freq_apelidos[seculo]
                        if dict.keys.contains(apelido):
                            dict[apelido] += 1
                            dados.freq_apelidos[seculo] = dict
                    else: 
                        if seculo < dados.seculo_inf_apelidos: dados.seculo_inf_apelidos = seculo
                        if seculo > dados.seculo_sup_apelidos: dados.seculo_sup_apelidos = seculo 
                        dados.freq_apelidos[seculo] = {proprio : 1}

                if dados.nomes_proprios.keys.contains(proprio):
                    dados.nomes_proprios[proprio] += 1
                else:
                    dados.top5_proprios.append(proprio)
                    dados.nomes_proprios[proprio] = 1
                if dados.apelidos.keys.contains(apelido):
                    dados.apelidos[apelido] += 1
                else:
                    dados.top5_apelidos.append(apelido)
                    dados.apelidos[apelido] = 1

            
            # ---> Nome Próprio / Apelido (Pai)
            if pai != "" and pai not in dados.nomes_pais:
                dados.n_pais += 1
                dados.nomes_pais.append(pai)
                (proprio, apelido) = nome_proprio_apelido(pai)
                if proprio != "":
                    if dados.freq_nomes_proprios.keys.contains(seculo):
                        dict = dados.freq_nomes_proprios[seculo]
                        if dict.keys.contains(proprio):
                            dict[proprio] += 1
                            dados.freq_nomes_proprios[seculo] = dict
                    else: 
                        if seculo < dados.seculo_inf_proprios: dados.seculo_inf_proprios = seculo
                        if seculo > dados.seculo_sup_proprios: dados.seculo_sup_proprios = seculo 
                        dados.freq_nomes_proprios[seculo] = {proprio : 1}
                if apelido != "":
                    if dados.freq_apelidos.keys.contains(seculo):
                        dict = dados.freq_apelidos[seculo]
                        if dict.keys.contains(apelido):
                            dict[apelido] += 1
                            dados.freq_apelidos[seculo] = dict
                    else:
                        if seculo < dados.seculo_inf_apelidos: dados.seculo_inf_apelidos = seculo
                        if seculo > dados.seculo_sup_apelidos: dados.seculo_sup_apelidos = seculo  
                        dados.freq_apelidos[seculo] = {proprio : 1}

                if dados.nomes_proprios.keys.contains(proprio):
                    dados.nomes_proprios[proprio] += 1
                else:
                    dados.top5_proprios.append(proprio)
                    dados.nomes_proprios[proprio] = 1
                if dados.apelidos.keys.contains(apelido):
                    dados.apelidos[apelido] += 1
                else:
                    dados.top5_apelidos.append(apelido)
                    dados.apelidos[apelido] = 1


    # Ordenar os top5 dos nomes e apelidos
    dados.top5_apelidos = sorted(dados, key = lambda x : dados.nomes_proprios[x], reverse=True)
    dados.top5_proprios = sorted(dados, key = lambda x : dados.apelidos[x], reverse=True)

    # (exercício c) ) -> Calcular nº de filhos, irmãos e de sobrinhos
    relacoes(dados)

    f.close() # Fechar ficheiro
    return dados

def calcular_seculo(ano):
    if (ano % 100) == 0: # ano igual ao século
        return ano / 100
    else: # tirar
        return ((ano - (ano % 100)) / 100) + 1

def nome_proprio_apelido(nome):
    proprio = ""
    apelido = ""
    while nome != "":
        n = nome.split(' ')
        proprio = n[0]
        apelido = n[-1]
    return (proprio, apelido)

# exercício c) (filhos, irmãos, sobrinhos)
def relacoes(dados):
    # nº de irmaos e de pais
    for (mae, pai) in dados.filhos.keys:
        n_filhos = len(dados.filhos[(mae, pai)])
        dados.n_filhos += n_filhos
        if n_filhos > 1: 
            dados.n_irmaos += n_filhos
            # procurar pelo nº de filhos dos irmãos (Sobrinhos)
            
            if dados.filhos.keys.contains(mae):
                dados.n_sobrinhos += dados.filhos[mae]
            if dados.filhos.keys.contains(pai):
                dados.n_sobrinhos += dados.filhos[pai]