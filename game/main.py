##############################################################################################
#                             JOGO DAS TRÊS PISTAS v2.0                                      #
#                               by Thiago DallasDev#                                         #
##############################################################################################


import game
import control_filters as op
from time import sleep
import os


while True:
    match op.menu('1:INICIAR JOGO', '2:VER PONTUAÇÃO', '3:REINICIAR JOGO', '4:SAIR DO JOGO'):

        case 'SAIR DO JOGO':
            print('Encerrando Jogo... Obrigado por brincar!\n')
            sleep(2)
            break

        case 'INICIAR JOGO':
            while True:
                if not game.palavra_dica():
                    break
                match op.menu('1:PRÓXIMA PALAVRA', '2:MENU PRINCIPAL'):
                    case 'MENU PRINCIPAL':
                        break

        case 'VER PONTUAÇÃO':
            game.pontos_acertos()

        case 'REINICIAR JOGO':
            os.system('cls')
            print(f'\n{op.cor(4, "ATENÇÃO!")}: Isso reiniciará o jogo, zerando sua pontuação!')

            if op.continuar('Deseja reiniciar? [S/N]: ', 'S', 'N'):
                game.reiniciar_jogo()


print(op.cor(3, '<< FIM DE JOGO! >>'.center(31, '=')))
game.pontos_acertos(True)
