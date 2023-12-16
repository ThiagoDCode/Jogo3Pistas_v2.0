import game
from control_filters import *
from time import sleep
import os


# Cria o arquivo onde serão armazenados as pontuações
if not os.path.exists('placar_geral.txt'):
    with open('placar_geral.txt', 'w', encoding='UTF-8') as file:
        file.write(f'{"Bot"}:{6}\n')
        file.close()


os.system('cls')
# PRINT ------------------------------------------------------------------------------------------------
print(f"""
{'='*76}
|{'JOGO DAS 3 PISTAS'.center(74)}|
{'[ Regras ]'.center(76, '=')}
1. Você deve descobrir a palavra secreta através das pistas dadas!
2. Você tem até 3 tentativas; cada tentativa te dá uma dica extra!
3. Cada dica vale uma pontuação, quanto menos tentativas, maior a pontuação!

{cor('[1ª Dica: 10 pontos] [2ª Dica: 8 pontos] [3ª Dica: 6 pontos]', 2).center(84, '=')}
""")
# ------------------------------------------------------------------------------------------------ PRINT
os.system('pause')


game.exibir_placar('placar_geral.txt'), print()
for i in game.progressbar(range(100), 'DCode', 20):
    sleep(0.04)


while True:
    match menu('INICIAR JOGO', 'PLACAR GERAL', 'SAIR DO JOGO'):

        case 3:  # SAIR DO JOGO
            print(cor('\nObrigado por brincar 0/', 2))
            sleep(2), exit()

        case 1:  # INICIAR JOGO
            nick = nickname('placar_geral.txt')
            if not nick:
                continue
            
            print(f'\nVamos aos jogos 🎲 {cor(nick, 3)}'), sleep(2)

            while True:
                match menu('JOGAR PALAVRA', 'PONTUAÇÃO', 'REINICIAR PARTIDA', 'FINALIZAR PARTIDA'):
                    
                    case 4:  # FINALIZAR PARTIDA
                        if not game.save_placar('placar_geral.txt', nick, game.pontos_jogador):
                            continue
                        game.reiniciar_jogo(nova_partida=True)
                        break

                    case 1:  # JOGAR PALAVRA
                        game.jogar_palavra()

                    case 2:  # PONTUAÇÃO
                        game.pontos_acertos(nick)

                    case 3:  # REINICIAR PARTIDA
                        game.reiniciar_jogo()

        case 2:  # PLACAR GERAL
            game.exibir_placar('placar_geral.txt')
            os.system('pause')
