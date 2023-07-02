##############################################################################################
#                             JOGO DAS TRÊS PISTAS v2.0                                      #
#                               by Thiago DallasDev#                                         #
##############################################################################################

from random import choice
import menu_filters as op
from time import sleep
import os
from palavras import dict_palavras


acertos = []
pontuacao = 0
list_copy = dict_palavras.copy()
cont_palavra = 0


def palavra_dica():
    global cont_palavra, list_copy
    os.system('cls')

    if len(list_copy) == 0:
        print('\nParabéns! Você ZEROU todas as palavras.\n'), os.system('pause')
        return False

    palavra, dica = choice(list(list_copy.items()))
    dica_iter = iter(dica)
    cont_palavra += 1
    list_copy.pop(palavra)

    return verificar_resp(palavra, dica_iter)


def verificar_resp(palavra_selecionada, dicas):
    global acertos, pontuacao

    print(f'\n========== PALAVRA {cont_palavra}/{len(dict_palavras)} ==========')
    print(f' ==== Palavra com "{len(palavra_selecionada)}" letras ====')

    for cont, pontos in enumerate([10, 8, 6]):
        print(f'|> A {cont+1}ª dica é: [ { op.cor(2, next(dicas)) } ]')
        resposta = input('Qual é a palavra? ').strip()

        if resposta.lower() == palavra_selecionada:
            print(f'\nAcertou! {op.cor(1, palavra_selecionada.upper())} => ganhou {op.cor(1, str(pontos) + " pontos")}\n')
            acertos.append(f'{op.cor(1, palavra_selecionada.upper())} (acertou na {cont+1}ª dica: {pontos}pnt)')
            pontuacao += pontos
            os.system('pause')
            return True
        else:
            print('\nERRADA!', end=' ')
            print('Próxima dica...\n' if cont < 2 else 'Que pena, mas sorte na próxima!\n')

    os.system('pause')
    return True


def pontos_acertos():
    os.system('cls')

    print(f'\nVocê teve {len(acertos)} acerto(s): ')
    for acerto in acertos:
        print(f' => {acerto}')
    print(f'Sua pontuação até agora: {op.cor(1, str(pontuacao) + " pontos")}\n')
    os.system('pause')


def reiniciar_jogo():
    global list_copy, acertos, pontuacao, cont_palavra

    print()
    for i in op.progressbar(range(100), 'Reiniciando Jogo: ', 50):
        sleep(0.03)

    list_copy = dict_palavras.copy()
    acertos.clear()
    pontuacao = 0
    cont_palavra = 0

    print(f'{op.cor(3, "JOGO REINICIADO COM SUCESSO!")}\n')
    os.system('pause')


while True:
    match op.menu('1:Iniciar Jogo', '2:Ver Pontuação', '3:Reiniciar Jogo', '4:Sair do Jogo'):

        case 'Sair do Jogo':
            print('Encerrando Jogo... Obrigado por brincar!\n')
            sleep(2)
            break

        case 'Iniciar Jogo':
            while True:
                if not palavra_dica():
                    break
                match op.menu('1:Próxima Palavra', '2:Menu Principal'):
                    case 'Menu Principal':
                        break

        case 'Ver Pontuação':
            pontos_acertos()

        case 'Reiniciar Jogo':
            os.system('cls')
            print(f'\n{op.cor(4, "ATENÇÃO!")}: Isso reiniciará o jogo, zerando sua pontuação!')
            reiniciar = op.continuar_parar('S', 'N', 'Deseja reiniciar? [S/N]: ')

            if reiniciar:
                reiniciar_jogo()


print(op.cor(3, ' FIM DE JOGO! '.center(40, '=')))
print(f'Sua pontuação final foi de {op.cor(1, str(pontuacao) + " pontos")}\n')
