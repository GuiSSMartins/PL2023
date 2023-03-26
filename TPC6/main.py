# TPC6: Analisador Léxico para uma Linguagem de Programação

# Usando o `Ply` constrói um analisador léxico que  devolve a lista de tokens para a linguagem de programação.


import ply.lex as lex

states = (
    # COMENTÁRIOS
    ('comentario', 'exclusive'),
    ('multicomentario', 'exclusive'), # apenas para lermos o conteúdo das linhas do comentário de maneira diferente

    # Para os nomes dos PROGRAM e FUNCTION
    ('function', 'exclusive'),
    ('program', 'exclusive')
    # num estado exclusivo, apenas aplicamos os tokens e regras para esse estado
    # por outro lado, num estado inclusivo, as regras e tokens desse estado juntam-se às outras regras e tokens
    # o estado inicial chama-se 'INITIAL' e não é preciso defini-lo
)

tokens = (
    'A_MULTI_COMENTARIO', 'F_MULTI_COMENTARIO', # /* */
    'COMENTARIO', # //

    # excluivos quando estamos dentro dos comentários
    'TEXT_COMENTARIO', 'TEXT_MULTI_COMENTARIO',

    # declaração de variáveis (normais OU globais)
    'INT', # int

    # Listas
    'A_DEF_LIST', 'F_DEF_LIST', # [ ],
    'A_LIST', 'F_LIST', # { }
    'INTERVAL_LIST', # ..

    'PRINT', 'A_PARENTESES', 'F_PARENTESES', # ( )
    'PROGRAM', # program
    'PROGRAM_NAME', 'FUNCTION_NAME',
    'FUNCTION', # function
    'CALL_FUNCTION', # chama-se uma função já definida
    'MULT', # *
    'MENOS', # -
    'MENOR', # <
    'MAIOR', # >
    'IGUAL', # =
    'NUM',
    'VIRGULA', # ,
    'PONTO_VIRGULA', # ;

    'WHILE', 'FOR', 'IF', 'IN',

    'VAR_ARRAY', # variável de um array
    'VAR' # String de uma variável
)


# TUDO sobre os comentários

def t_A_MULTI_COMENTARIO(t):
    r'\/\*'
    t.lexer.begin('multicomentario')
    return t

t_multicomentario_TEXT_MULTI_COMENTARIO = r'[\w\.\-\:\,\s\n]*(?=\*\/)'

def t_multicomentario_F_MULTI_COMENTARIO(t):
    r'\*/'
    t.lexer.begin('INITIAL')
    return t

def t_COMENTARIO(t):
    r'\/\/'
    t.lexer.begin('comentario')
    return t

def t_comentario_TEXT_COMENTARIO(t):
    r'[\w\.\-\:\,\s\n]+(?=\n)'
    t.lexer.begin('INITIAL')
    return t

# ---------------------------------------------------------------------

t_INT = r'int(?=\s)'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return 

t_VIRGULA = r','
t_PONTO_VIRGULA = r';'

# Definiçaõ de uma lista {} : quando estamos a definir uma variável

t_A_DEF_LIST = r'\['
t_F_DEF_LIST = r'\]'
t_A_LIST = r'\{'
t_F_LIST = r'\}'
t_INTERVAL_LIST = r'\.{2}'

t_PRINT = r'print(?=\()'
t_A_PARENTESES = r'\('
t_F_PARENTESES = r'\)'

# Dentro das funções e dos programas

def t_FUNCTION(t):
    r'function(?=\s)'
    t.lexer.begin('function')
    return t

def t_PROGRAM(t):
    r'program(?=\s)'
    t.lexer.begin('program')
    return t

def t_function_FUNCTION_NAME(t):
    r'\w+'
    t.lexer.begin('INITIAL')
    return t

def t_program_PROGRAM_NAME(t):
    r'\w+'
    t.lexer.begin('INITIAL')
    return t

t_WHILE = r'while'
t_FOR = r'for'
t_IN = r'in'

t_CALL_FUNCTION = r'\w+(?=\()'

# Operadores comuns

t_IGUAL = r'\='
t_MULT = r'\*(?=[\s\w])'
t_MENOR = r'\<'
t_MAIOR = r'\>'
t_MENOS = r'\-'

t_VAR_ARRAY = r'\w+(?=\[)'
t_VAR = r'\w+' # definição de variável

t_ANY_ignore = ' \t\n'

def t_ANY_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)

#-------------------------------------------------
def main():

    lexer = lex.lex()

    exemplo1 = '''
    /* factorial.p
    -- 2023-03-20 
    -- by jcr
    */

    int i;

    // Função que calcula o factorial dum número n
    function fact(n){
    int res = 1;
    while res > 1 {
        res = res * n;
        res = res - 1;
    }
    }

    // Programa principal
    program myFact{
    for i in [1..10]{
        print(i, fact(i));
    }
    }
    '''

    exemplo2 = '''
    /* max.p: calcula o maior inteiro duma lista desordenada
    -- 2023-03-20 
    -- by jcr
    */

    int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

    // Programa principal
    program myMax{
    int max = a[0];
    for i in [1..9]{
        if max < a[i] {
        max = a[i];
        }
    }
    print(max);
    }
    '''

    print("\nTPC6 - Processamento de Linguagens - 2023")
    print("Guilherme Martins - a92847 - LEI")

    perguntar = 1
    while perguntar:

        print("\n-| Analisador Léxico para uma Linguagem de Programação |-\n")

        print("Escolha o exemplo em que deseja aplicar o Analisador Léxico:")
        print("1) Exemplo 1")
        print("2) Exemplo 2")
        print("0) SAIR")

        opcao = int(input("\nEscreva a opção desejada: "))

        if opcao == 1: # Resultados dos tokens para o Exemplo 1
            print()
            lexer.input(exemplo1)
            #lexer.variables = list() # lisat de variáveis + estado main atual
            while tok := lexer.token():
                # pass
                print(tok)
        elif opcao == 2: # Resultados dos tokens para o Exemplo 2
            print()
            lexer.input(exemplo2)
            #lexer.variables = list() # lisat de variáveis + estado main atual
            while tok := lexer.token():
                # pass
                print(tok)
        elif opcao == 0: perguntar = 0
        else: print("\nOpção Errada\n")
    print("\nFIM do programa!\n")


if __name__ == '__main__':
    main()