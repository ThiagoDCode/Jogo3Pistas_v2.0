##############################################################################################
#                             JOGO DAS TRÊS PISTAS v2.0                                      #
#                               by Thiago DallasDev#                                         #
##############################################################################################


from def_control import *
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
                if not palavra_dica():
                    break
                match op.menu('1:PRÓXIMA PALAVRA', '2:MENU PRINCIPAL'):
                    case 'MENU PRINCIPAL':
                        break

        case 'VER PONTUAÇÃO':
            pontos_acertos()

        case 'REINICIAR JOGO':
            os.system('cls')
            print(f'\n{op.cor(4, "ATENÇÃO!")}: Isso reiniciará o jogo, zerando sua pontuação!')

            if op.continuar('Deseja reiniciar? [S/N]: ', 'S', 'N'):
                reiniciar_jogo()


print(op.cor(3, '<< FIM DE JOGO! >>'.center(31, '=')))
pontos_acertos(True)
