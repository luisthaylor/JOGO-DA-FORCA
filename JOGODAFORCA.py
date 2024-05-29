import random, time, os
##NOMES: LUIS THAYLOR (RA:11367260) e EMANOEL ROSA (RA:1136489)
##jOGO DA FORCA
##NECESSÁRIO TER DESAFIADOR E QUEM ESTÁ SENDO DESAFIADO, PODENDO ESCOLHER PALAVRAS E DICA 

def limpaTela():
    os.system ('cls')

def tempo5s():
    time.sleep (5)
def tempo10s():
    time.sleep (10)

print ('''

 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀█░█▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
      ▐░▌    ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
      ▐░▌    ▐░▌       ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌
      ▐░▌    ▐░▌       ▐░▌▐░▌▐░░░░░░░░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌
      ▐░▌    ▐░▌       ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌
      ▐░▌    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌          ▐░▌       ▐░▌
 ▄▄▄▄▄█░▌    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌
▐░░░░░░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░▌ ▐░▌       ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀   ▀         ▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                                                                         

''')
tempo5s()

limpaTela()

print('Primeramente precisamos saber o nome de quem irá participar deste desafio: ')
nomedesafiante = input('\nDigite o nome do desafiante, sendo a pessoa que irá escolher a palavra do jogo ! ')
nomedesafiado = input('\nInforme o nome do competidor, sendo a pessoal que será desafiada e irá quebrar a cabeça tentando descobrir a palavra... ')

print ('\nBem vindo ao jogo, {} e {}, vocês irão participar deste jogo amigável, o jogador {} terá como objetivo descobrir a palavra a que o jogador {} escolher !!! '.format(nomedesafiante,nomedesafiado,nomedesafiado,nomedesafiante))

tempo5s()
limpaTela()

print ('......ATENÇÃO DESAFIANTE, ESCONDA A TELA DO JOGADOR DESAFIADO PARA ESCOLHER A PALAVRA....')
print ('''

██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗        ██████╗ ██╗     ███████╗ █████╗ ███████╗███████╗    ██╗    ██╗ █████╗ ██╗████████╗
██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝        ██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝██╔════╝    ██║    ██║██╔══██╗██║╚══██╔══╝
██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗       ██████╔╝██║     █████╗  ███████║███████╗█████╗      ██║ █╗ ██║███████║██║   ██║   
██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║       ██╔═══╝ ██║     ██╔══╝  ██╔══██║╚════██║██╔══╝      ██║███╗██║██╔══██║██║   ██║   
███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝▄█╗    ██║     ███████╗███████╗██║  ██║███████║███████╗    ╚███╔███╔╝██║  ██║██║   ██║   
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝    ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   
                                                                                                                                                

 ''')
tempo10s()
limpaTela()

def escolher_palavra():
    palavras = input('Escolha uma palavra para a forca, mas mantenha silencio :  ')
    limpaTela()
    return (palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6

    while True:
        mostrar_forca(letras_erradas, letras_certas, palavra)
        palpite = input("Digite uma letra: ").lower()

        if len(palpite) != 1:
            print("Por favor, digite apenas uma letra.")
            continue
        elif palpite in letras_certas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        elif not palpite.isalpha():
            print("Por favor, digite apenas letras.")
            continue

        if palpite in palavra:
            letras_certas.append(palpite)
            if len(letras_certas) == len(set(palavra)):
                print("Parabéns! Você ganhou! A palavra era:", palavra)
                break
        else:
            letras_erradas.append(palpite)
            tentativas -= 1
            print("Letra errada. Você ainda tem {} tentativas.".format(tentativas))
            if tentativas ==4:
                dica1 = float(input('Percebi que está tendo dificuldades, que tal uma dica ?(1) para RECEBER dica, (0) para NÃO RECEBER:  '))
                if dica1 == 1:
                    print (input('Digite a primeira dica : '))
                    print (input('Pressione enter para continuar'))
    
                    limpaTela()
                    continue
            if tentativas == 2:
                dica2 = float(input('Parece que está dificil em? que tal mais uma dica ? Para RECEBER MAIS UMA DICA pressione (1) e para continuar sem dica pressione (0):  '))
                if dica2 == 1:
                    print(input('A segunda dica é: '))
                    print (input('Pressione enter para continuar'))
                    limpaTela()
                    continue
            if tentativas == 1:
                dica3 = float(input('Se você errar mais uma vez, está fora ! Essa é sua ultima dica.Para RECEBER MAIS UMA DICA pressione (1) e para continuar sem dica pressione (0):  '))
                print(input('A terceira e ultima  dica é: '))
                print (input('Pressione enter para continuar'))
                limpaTela()
                continue
            
            if tentativas == 0:
                print('''
                      
                      
   ▄████████    ▄████████         ▄████████ ███    █▄  ████████▄     ▄████████ ███    █▄  
  ███    ███   ███    ███        ███    ███ ███    ███ ███   ▀███   ███    ███ ███    ███ 
  ███    █▀    ███    █▀         ███    █▀  ███    ███ ███    ███   ███    █▀  ███    ███ 
  ███         ▄███▄▄▄           ▄███▄▄▄     ███    ███ ███    ███  ▄███▄▄▄     ███    ███ 
▀███████████ ▀▀███▀▀▀          ▀▀███▀▀▀     ███    ███ ███    ███ ▀▀███▀▀▀     ███    ███ 
         ███   ███    █▄         ███        ███    ███ ███    ███   ███    █▄  ███    ███ 
   ▄█    ███   ███    ███        ███        ███    ███ ███   ▄███   ███    ███ ███    ███ 
 ▄████████▀    ██████████        ███        ████████▀  ████████▀    ██████████ ████████▀  
                                                                                          
''', 'A palavra era :', palavra)
                break

def mostrar_forca(letras_erradas, letras_certas, palavra):
    print("Palavra: ", end=" ")
    for letra in palavra:
        if letra in letras_certas:
            limpaTela
            print(letra, end=" ")
    
        else:
            print("_", end=" ")
    print("")

    print("Letras erradas:", ", ".join(letras_erradas))


jogar_forca()
