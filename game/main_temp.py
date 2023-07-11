import game
import control_filters as op
from time import sleep
import os


while True:
    match op.menu('1:INICIAR JOGO', '2:PLACAR GERAL', '3:SAIR DO JOGO'):

        case 'SAIR DO JOGO':
            game.pontos_acertos(True)
            print('Obrigado por brincar 0/\n')
            sleep(2), exit()

        case 'INICIAR JOGO':
            nick_name = game.nick_name()
            print(f'\nVamos aos jogos, {nick_name}')
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
