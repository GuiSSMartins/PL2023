import math
import re

class Dados: # Todos os dados obtidos a partir do ficheiro "parsing.txt"
    def _init_(self):
        self.registos = [] # ordem sequencial dos registos
        self.total = 0

        # exercício a) 
        # frequência do nº de processos por ano
        self.freq_processos_ano = {} # ano (key) -> nº de processos (value)
        self.lim_inf_proc = math.inf
        self.lim_sup_proc = 0

        # exercício b)
        # frequência de nomes próprios
        self.freq_nomes_proprios = {} # seculo (key) -> { nome (key) -> nº (value) } (value)
        self_seculo_inf_proprios = math.inf
        self_seculo_sup_proprios = 0
        self_seculo_inf_apelidos = math.inf
        self_seculo_sup_apelidos = 0

        # exercício c)

        # exercício d) 
        # guardar os 20 primerios registos sob a forma de um dicionário
        # de forma a ser compatível com o formato JSON
        self.registos20 = {} # chave :: número do registo ;; resto :: string
        self.n_registos = 0


    # Adicionar um processo 
    def adicionarProcessoAno(self, ano):
        self.processos_ano.keys.contains(ano)
    
    # exercício d)
    def adicionarRegisto20(self, linha_registo):
        self.n_registos += 1
        self.registos20[self.n_registos]
    


# eliminar processos repetidos
# CUIDADO: podem haves 2 ou mais processos com o mesmo ID


def parsing():
    
    dados = Dados()
    f = open("processos.txt",'r')

    # Parsing do conteúdo
    linhas = f.readlines()

    # Expressão Regular
    er = re.compile(r'(?P<id>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome1>(\w+|\s+)+)::(?P<nome2>(\w+|\s+)*)::(?P<nome3>(\w+|\s+)*)::(?P<nome4>(\w+|\s+)*)::(?P<nome5>(\w+|\s+)*)')

    for linha in linhas:
        if linha != "": # tem de ter conteúdo
            registo = er.match(linha).groupdict()
            dados.registos.append(registo)
            dados.total += 1
            # Verificar se é para adicionar aos primeiros 20 registos d)
            if dados.n_registos < 20:
                dados.adicionarRegisto20(linha)
            if re.search("Doc.danificado.", linha):

    # Fechar ficheiro
    f.close()
    return dados

def calcular_seculo(ano):
    if (ano % 100) == 0: # ano igual ao século
        return ano / 100
    else:


def nome_proprio_apelido(nome):


    return (None,None)