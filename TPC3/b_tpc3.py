from dados import Dados

# > b) Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos 
# e apresenta os 5 mais usados;

def b(dados):
    
    # frequência de nomes próprios
    print("\n-| Frequência de nomes próprios |-")
    for seculo_proprios in range(dados.seculo_inf_proprios, dados.seculo_sup_proprios + 1):
        if seculo_proprios in dados.freq_nomes_proprios:
            print("|| Século " + str(seculo_proprios) + " ||")
            dict = dados.freq_nomes_proprios[seculo_proprios]
            print(dict)

    print("\n-| Frequência de apelidos |-")
    for seculo_apelidos in range(dados.seculo_inf_apelidos, dados.seculo_sup_apelidos + 1):
        if seculo_apelidos in dados.freq_apelidos:
            print("|| Século " + str(seculo_apelidos) + " ||")
            dict = dados.freq_apelidos[seculo_apelidos]
            print(dict)

    print("\n-| Top 5 de Nomes PRÓPRIOS |-\n")
    for i in range(0,5):
        print(str(i+1) + "º : " + dados.top5_proprios[i])

    print("\n-| Top 5 de APELIDOS |-\n")
    for j in range(0,5):
        print(str(j+1) + "º : " + dados.top5_apelidos[j])