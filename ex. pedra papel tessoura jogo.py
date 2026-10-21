import random
import time

nome_do_jogador = str(input("Digite seu nome de jogador: "))
options = ("pedra", "papel", "tessoura")
jogar_novamente = "sim"

while jogar_novamente == "sim":

    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:

        player = None #significa que o jogador ainda não escolheu nada
        computador = random.choice(options)

        while player not in options:
            player = input("Digite uma escolha (pedra, papel, tessoura): ")

        print(f"{nome_do_jogador}: {player}")
        time.sleep(1)
        print(f"Computador: {computador}")

        if player == computador:
            print("Empate")

        elif (
            (player == "papel" and computador == "pedra") or
            (player == "pedra" and computador == "tessoura") or
            (player == "tessoura" and computador == "papel")
        ):
            print("Você venceu!")
            player_score += 1

        else:
            print("Você perdeu")
            computer_score += 1

        print("----------------")
        print(f"Placar: {nome_do_jogador}: {player_score} X IA: {computer_score}")
        print("----------------")

    if player_score == 3:
        print(f"Parabens, {nome_do_jogador}! Você é o grande vencedor pelo placar de {player_score} a {computer_score}")

    else:
        print(f"Que pena, a IA venceu o desafio pelo placar de {computer_score} a {player_score}")

    print("---------------------")

    jogar_novamente = input("Deseja jogar novamente? (sim/nao): ").lower().strip()

    print("                     ")

print("Obrigado por jogar")

