# THE HANGMAN GAME

import random

palavras = ("abacaxi", "amor", "amizade", "alegria", "avião", "abelha", "arroz", "árvore", "azul", "areia", "bola", "brasil",
            "banana", "borboleta", "bicicleta", "beleza", "cachorro", "casa", "carro", "coração", "cavalo", "chuva", "caderno",
            "cadeira", "caminho", "computador", "café", "camisa", "doce", "dinheiro", "dado", "dragão", "dedo", "dia", "dança",
            "elefante", "estrela", "escola", "espelho", "esperança", "envelope", "escada", "futebol", "flor", "fogo", "festa",
            "família", "foguete", "fazenda", "felicidade", "formiga", "gato", "garrafa", "girafa", "geladeira", "guitarra", "guerra", 
            "geleia", "golfinho", "helicóptero", "história", "homem", "hotel", "igreja", "ilha", "inverno", "internet", "jardim", 
            "janela", "jacaré", "jornal", "joelho", "jogo", "kiwi", "lápis", "livro", "leão", "lua", "laranja", "limão", "luz", 
            "montanha", "macaco", "mesa", "música", "mochila", "médico", "melancia", "milho", "navio", "nuvem", "natureza", "nariz", 
            "noite", "número", "oceano", "olho", "ovo", "onça", "orelha", "outono", "pássaro", "praia", "porta", "panela", "pintura", 
            "pipoca", "professor", "planeta", "queijo", "quadro", "quarto", "quintal", "raposa", "relógio", "rio", "roupa", "rosa", 
            "sapato", "sol", "sorriso", "sorvete", "sapo", "saúde", "telefone", "tesouro", "tomate", "tigre", "trabalho", "universo", 
            "uva", "urso", "unha", "vaca", "vento", "verão", "viagem", "violão", "vitória", "xadrez", "xícara", "zebra", "zoológico", "rainha", 
            "logan")

hangman_art = {0: ("   ",
                   "   ",
                   "   ",),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " | ",
                   "   "),
               3: (" O ",
                   " |\\",
                   "   "),
               4: (" O ",
                   " |\\",
                   "  \\"),
               5: (" O ",
                   "/|\\",
                   "  \\"),
               6: (" O ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(palavras)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Digite uma letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Digito invalido")
            continue

        if guess in guessed_letters:
            print(f"{guess} ja foi digitado")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("VOCE VENCEU!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("VOCE PERDEU!")
            is_running = False
   
    
if __name__ == "__main__":
    main()
