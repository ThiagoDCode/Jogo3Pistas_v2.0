import game
import control_filters as op
from time import sleep
import os

os.system('cls')
# PRINT ------------------------------------------------------------------------------------------------
print(f'{"="*70}'
      f'\n|{"JOGO DAS 3 PISTAS".center(68)}|\n'
      f'{"[ Regras ]".center(70, "=")}')
print(f'\n1. Você deve descobrir a palavra secreta através das pistas dadas'
      f'\n2. Você tem até 3 tentativas, cada tentativa te dá uma dica extra'
      f'\n3. Cada dica vale uma pontuação, menor a dica, maior a pontuação\n'
      f'\n{op.cor(2, "[ Dica 1: 10 pontos | Dica 2: 8 pontos | Dica 3: 6 pontos ]").center(78, "=")}\n')
# ------------------------------------------------------------------------------------------------ PRINT
os.system('pause')
game.exibir_placar('placar_geral.txt')
for i in op.progressbar(range(100), 'DCode', 20):
    sleep(0.04)

while True:
    match op.menu('1:INICIAR JOGO', '2:PLACAR GERAL', '3:SAIR DO JOGO'):

        case 'SAIR DO JOGO':
            print(op.cor(2, '\nObrigado por brincar 0/\n'))
            sleep(2), exit()

        case 'INICIAR JOGO':
            if not os.path.exists('placar_geral.txt'):
                with open('placar_geral.txt', 'w', encoding='UTF-8') as file:
                    file.write(f'{"Bot"}:{6}\n')
                    file.close()

            nick_name = game.nick_name('placar_geral.txt')
            if not nick_name:
                continue
            print(f'\nVamos aos jogos 🎲, {op.cor(3, nick_name)}')
            sleep(2)

            while True:
                match op.menu('1:JOGAR PALAVRA', '2:PONTUAÇÃO', '3:REINICIAR PARTIDA', '4:FINALIZAR PARTIDA'):
                    case 'FINALIZAR PARTIDA':
                        game.save_placar('placar_geral.txt', nick_name, game.pontuacao)
                        game.reiniciar_jogo(nova_partida=True)
                        break

                    case 'JOGAR PALAVRA':
                        game.palavra_dica()

                    case 'PONTUAÇÃO':
                        game.pontos_acertos()

                    case 'REINICIAR PARTIDA':
                        game.reiniciar_jogo()

        case 'PLACAR GERAL':
            game.exibir_placar('placar_geral.txt')
            os.system('pause')
