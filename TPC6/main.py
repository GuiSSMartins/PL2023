# TPC6: Analisador Léxico para uma Linguagem de Programação

# Usando o `Ply` constrói um analisador léxico que 
# devolve a lista de tokens para a linguagem de programação que se exemplifica a seguir.
# (NOTA: exemplos inspirados na linguagem de programação C)
"""

"""

import ply.lex as lex

states = (
    ('comment_multi_a', 'exclusive'), # a ler conteúdos de um comentário multi-linha
    ('comment_multi_f', 'exclusive'), # terminou-se a leitura do  comentário multi-linha
    ('function_a', 'exclusive'), # 
    ('function_f', 'exclusive'), 
    ('list_a', 'exclusive'), # estamos a definir uma nova lista
    ('list_f', 'exclusive'),

    ('while_cond', 'exclusive'), # estamos a ver as condições do WHILE

    # num estado exclusivo, apenas aplicamos os tokens e regras para esse estado
                           # por outro lado, num estado inclusivo, as regras e tokens desse estado juntam-se às outras regras e tokens
                           # o estado inicial chama-se 'INITIAL' e não é preciso defini-lo
)

tokens = (
    'MULTI_COMENT' # /* (...)  */
    'A_COMENT', # // (...)
    'A_LIST', # \d+[
    'LIST_CONTENT', # 
    'F_LIST', # ]
    'LIST_CONTENT', # \=\s{
    'F_LIST_CONTENT', # }
    'INTERVAL', # ..
    'INT', # int
    'PROGRAM_NAME', # program \d+{
    ''
    'FUNCTION', # function
    'EQUALS', # =
    'MULT', # *
    'MENOS', # -
    'MENOR', # <
    'VAR_IGUALDADE', # ()


)

def t_MULTI_COMMENT(t):
    r'\/\*\w*\*\/'
    return t

def t_ATAGF(t):
    r'</'
    return t


t_ANY_ignore = ' \t\n'

def t_ANY_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)



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
    print("Guilherme Martins - a92847 - LEI\n")

    print("-| CABINE TELEFÓNICA |-\n")
    print("maq: Opções possíveis para escrever (ignorar os ;):")
    print("-> LEVANTAR; POUSAR; MOEDA $c, $e. (tem de ter um ponto no final);")
    print("-> T=<o número deve ter 9 dígitos excepto se for iniciado por '0'>; ABORTAR")

    perguntar = 1
    while perguntar:
        opcao = input()

    # Resultados dos tokens para o Exemplo 1

    lexer.input(exemplo1)

    while tok := lexer.token():
        # pass
        print(tok)

    # Resultados dos tokens para o Exemplo 2

    lexer.input(exemplo2)

    while tok := lexer.token():
        # pass
        print(tok)


if __name__ == '__main__':
    main()