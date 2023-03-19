# Deterministic Finite Automata (DFA)
# Webgrafia: https://www.askpython.com/python-modules/state-machines-python#:~:text=A%20state%20machine%20is%20a,logic%20circuits%20and%20computer%20programs.

class Maquina:
    # Automata = (Q, F, δ, q0, Σ)

    # Q = A set of all states.
    # F = Set of all final states.
    # δ = The transition function or mapping function that maps the movement of states with each input.
    # q0 = The initial state.
    # Σ = A finite set of input symbols.

    def __init__(self):
        self.saldo = 0.0 # saldo que o utilizador já inseriu
        self.lista_moedas = [] # contém APENAS as moedas inseridas pelo utilizador
        # self.lista_custos_telefonema = [] # contém APENAS os valores dos Telefonemas
        self.q = ['INICIOU', 'LEVANTOU', 'POUSOU', 'ABORTOU']
        self.f = ['POUSOU', 'ABORTOU']
        self.q0 = 'INICIOU'
        # As transições são definidas pelas várias funções definidas abaixo

    def levantar(self):
        if self.q0 == 'INICIOU':
            self.q0 = 'LEVANTOU'
            print('maq: "Introduza moedas."')
        else: print("\n!!! Não pode levantar  !!!\n")

    def pousar(self): # pousar o auscultador, fim da interacção, deverá ser indicado o montante a ser devolvido;
        if self.q0 == 'LEVANTOU':
            self.q0 = 'POUSOU'
            # Indicar montante a devolver
            print()
        else: print('maq: "!!! Não pode levantar !!!"')

    # MOEDA $c, $e  ||   MOEDA <lista de valores>
    def adicionarMoedas(self, string_moeda):
        if self.q0 == 'LEVANTOU':

            # EXEMPLO: MOEDA 10c, 30c, 50c, 2e. (CUIDADO com o ponto final)
            pos_moeda = string_moeda[6:]
            moedas = pos_moeda.split('.')[0].split(',')

            # Moedas válidas: 1 cêntimo (1c), 2 cêntimos (2c), 5 cêntimos (5c), 10 cêntimos (10c), 20 cêntimos (20c)
            # 50 cêntimos (50c), 1 euro (1e), 2 euros (2e)
            # ATENÇÃO: se encontrar uma moeda inválida, deve escrever uma mensagem de erro

            for md in moedas:
                if 'c' in md:

                elif 'e' in md: 

            m = re.match(r'', string_moeda)

            self.custo_total += valor
            self.lista_moedas.append(valor)

        else: print('maq: "Não pode adicionar moedas se ainda não LEVANTOU os auscultadores!"')





    # (o número deve ter 9 dígitos excepto se for iniciado por "00")

    # * para números iniciados por "601" ou "641" a chamada é "_bloqueada_";
    # * para chamadas internacionais (iniciadas por "00") o utilizador tem que ter um saldo igual ou superior a 1,5 euros, caso contrário deverá ser avisado que o saldo é insuficiente e a máquina volta ao estado anterior; a chamada se for realizada tem um custo de 1,5 euros;
    # * para chamadas nacionais (iniciadas por "2") o saldo mínimo e custo de chamada é de 25 cêntimos;
    # * para chamadas verdes (iniciadas por "800") o custo é 0;
    # * para chamadas azuis (iniciadas por "808") o custo é de 10 cêntimos.
    def t(self, string_numero): # discar um número
        if self.q0 == 'LEVANTOU':
            # Processar número de telefone
            if string_numero[0:3] == "601" or string_numero[0:3] == "641":
                print('maq: "Chamada _bloqueada_"')
            elif string_numero[0:2] == "00":
                if self.saldo >= 1.5: 
                    self.saldo -= 1.5
                    print('maq. "Chamada internacional efetuada com sucesso."')
                else: 
                    print('maq: "Saldo INSUFICIENTE! Por favor, adicione mais moedas"')
                    print('maq: "Para chamadas internacionais, tem de ter um saldo igual ou superior a 1,5 euros!"')
            elif string_numero[0] == '2':

            
            elif string_numero[0:3] == "800":
                print('maq. "Chamada verde efetuada com sucesso."')
            elif string_numero[0:3] == "808":
                if self.saldo >= 0.10:
                    self.saldo -= 0.10
                    print('maq. "Chamada azul efetuada com sucesso."')
                else:
                    print('maq: "Saldo INSUFICIENTE! Por favor, adicione mais moedas"')
                    print('maq: "Para chamadas azuis, tem de ter um saldo igual ou superior a 10 cêntimos!"')
            else:
                print('maq: "Esse número não é permitido neste telefone. Queira discar novo número!"')
            # Adicionar custo da chamada
            # self.saldo -= valor
        else:
            print('maq: "Por favor, LEVANTE o auscultador antes de telefonar! "')
        centimos = (self.saldo % 1) * 100
        euros = self.saldo - centimos
        print('maq: "SALDO atual: ' + + str(euros) + 'e' + '{:.2f}'.format(centimos) + 'c"')
        print('maq: "Não se esqueça de POUSAR o auscultador, caso não deseje fazer mais chamadas!"')
        

    # devolver as moedas
    def abortar(self):
        if self.q0 != 'POUSOU' and self.q0 != 'ABORTOU': # Basta que o programa não esteja num estado final para 
            self.q0 = 'ABORTOU'
            centimos = (self.saldo % 1) * 100
            euros = self.saldo - centimos
            print('maq: "Operação abortada! troco: "' + str(euros) + 'e' + '{:.2f}'.format(centimos) + 'c; Volte sempre!"')
        else: 
            print('maq: "Não pode abortar!"')
