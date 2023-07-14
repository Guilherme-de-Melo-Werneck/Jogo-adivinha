import random #gerar um número aleatório

def adivinha():   #funcao do jogo
    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    numero_secreto = random.randint(1, 100) #gera um número aleatório entre 1 e 100 
    tentativas = 0  #conta o número de tentativas, começando por 0

    while True:   #O jogo continua até que o jogador acerte o número
        tentativa = int(input("Digite um número: "))
        tentativas = tentativas + 1    # o jogador fez uma tentativa.

        if tentativa < numero_secreto:  #se o número escolhido for menor, printa oque está escrito em baixo
            print("Número baixo! Tente um número maior.")
        elif tentativa > numero_secreto:    #se o número escolhido for maior, printa oque está escrito em baixo
            print("Número alto! Tente um número menor.")
        else:     #se o número escolhido for escolhido, print oque está em baixo 
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas,") 
            break

adivinha()