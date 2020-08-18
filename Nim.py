# -*- coding: utf-8 -*-

def computador_escolhe_jogada(n, m):

    #Vez do computador
    print("Vez do computador!")

    #Pode retirar todas as peças?
    if n <= m:

        #Retira todas as peças do jogo e o ganha
        return n
    else:

        #Verifica se é possivel deixar uma quantia multipla de m+1:
        quantia = n % (m+1)

        if quantia > 0:
            return quantia
        #Não é, então tire m peças::
        return m


def usuario_escolhe_jogada(n, m):

    #Vez do Usuario
    print("Sua vez!!")

    #Define o número de peças do úsuario
    jogada = 0

    #Enquanto o número não for valido
    while jogada == 0:

        #Solicita ao usuario quantas peças ele irá tirar
        jogada = int(input("Quantas peças deseja tirar? "))

        #Condições de jogada < n, jogada < m, jogada > 0
        if jogada > n or jogada < 1 or jogada > m:

            #Valor invalido. O programa continuará solicitando um valor valido
            jogada = 0
    #Número de peças valido
    return jogada



def partida():


    #Solicita os padrões de n e m para a partida
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    #Variavel que controla o turno do computador
    pc_turn = True

    #Decide quem inicia o jogo
    if n % (m+1) == 0: pc_turn = True

    #Executa enquanto restar peças no jogo
    while n > 0:

        if pc_turn:
            jogada = computador_escolhe_jogada(n, m)
            pc_turn = False
            print("Computador retirou {} peças".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            pc_turn = True
            print("Você retirou {} peças".format(jogada))

        # Retira as peças do jogo
        n = n - jogada

        # Mostra o Atual estado do Jogo
        print("Restam {} peças no jogo\n".format(n))

    # Verifica quem ganhou e da fim ao jogo
    if pc_turn:
        print("VOCÊ GANHOU!!!! PARABÉNS")
        return 1
    else:
        print("O computador ganhou!!! ( ´ - ` )")
        return 0

def campeonato():

    #Pontuações:
    usuario = 0
    computador = 0

    #Executa 3 vezes
    for _ in range(3):

        #Executa a partida
        vencedor = partida()

        #Verifica o resultado e soma a pontuação
        if vencedor == 1:

            #Usuario venceu
            usuario = usuario + 1
        else:
            #Computador venceu
            computador = computador + 1
    #Exibe o placar final
    print("Placar final: Você {} x {} Computador".format(usuario, computador))


tipo_jogo = 0

#Enquanto não for uma opção valida
while tipo_jogo == 0:

    #Menu
    print('{}'.format('Bem-vindo ao Jogo NIM! Escolha uma das opções: '))
    print('='*30)
    print("1 - para escolher PARTIDA")
    print("2 - para escolher CAMPEONATO")

    tipo_jogo =int(input("Sua escolha: "))
    print("="*30)

    #Escolhendo o tipo de partida
    if tipo_jogo == 1:
        print("Você escolheu partida isolada! Boa sorte")
        partida()
        break
    elif tipo_jogo == 2:
        print("Você escolheu campeonato! Boa sorte")
        campeonato()
        break
    else:
        print("Opção invalida")
        tipo_jogo = 0







