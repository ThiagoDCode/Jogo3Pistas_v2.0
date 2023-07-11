from palavras import dict_palavras
from control_filters import *
from random import choice
from time import sleep
import os


cont_palavra = 0
acertos = []
pontuacao = 0
copia_palavras = dict_palavras.copy()


def palavra_dica():
    os.system('cls')
    global cont_palavra

    if not copia_palavras:
        print('\nParabéns! Você ZEROU todas as palavras.\n'), os.system('pause')
        return False

    palavra_selecionada, dicas_palavra = choice(list(copia_palavras.items()))
    cont_palavra += 1
    copia_palavras.pop(palavra_selecionada)

    return verificar_resp(palavra_selecionada, dicas_palavra)


def verificar_resp(palavra, dicas):
    global acertos, pontuacao
    dica_iter = iter(dicas)

    for cont, pontos in enumerate([10, 8, 6]):
        os.system('cls')

        print(f'<< PALAVRA  {cont_palavra}/{len(dict_palavras)} >>'.center(60, '='))
        print(f'| {f"Palavra com {len(palavra)} letras":^56} |\n'
              f'{"=" * 60}')
        for dica in dicas[:cont+1]:
            print(cor(5, f'[ {dica.upper()} ]'), end=' ')
        print()

        print(f'\nA {cont+1}ª dica é [{cor(2, next(dica_iter))}], Qual a palavra? ')
        resposta = verify_entry('|> ')

        if resposta.lower() == palavra:
            print(f'\nAcertou! {cor(1, palavra.upper())} => ganhou {cor(1, str(pontos) + " pontos")}\n')

            acertos.append(f'{cor(1, palavra.upper())} (acertou na {cont + 1}ª dica: {pontos}pnt)')
            pontuacao += pontos
            os.system('pause')
            return True
        else:
            print(f'\n{cor(3, "ERROOOUU!")}', end=' ')
            print('Próxima dica...\n' if cont < 2 else 'Que pena, mas sorte na próxima!\n')
            sleep(3)

    os.system('pause')
    return True


def pontos_acertos(final=False):
    os.system('cls')

    if final:
        print(f'Palavras acertadas:')
        for acerto in acertos:
            print(f' => {acerto}')
        print(f'Acertos totais: {cor(1, str(len(acertos)))}\n'
              f'Pontuação final: {cor(1, str(pontuacao) + " pontos")}\n')
    else:
        print(f'\nVocê teve {len(acertos)} acerto(s): ')
        for acerto in acertos:
            print(f' => {acerto}')
        print(f'Pontuação: {cor(1, str(pontuacao) + " pontos")}\n')
        os.system('pause')


def reiniciar_jogo():
    global copia_palavras, acertos, pontuacao, cont_palavra

    print()
    for i in progressbar(range(100), 'Reiniciando Jogo: ', 50):
        sleep(0.03)

    copia_palavras = dict_palavras.copy()
    acertos.clear()
    pontuacao = 0
    cont_palavra = 0

    print(f'{cor(3, "JOGO REINICIADO COM SUCESSO!")}\n')
    os.system('pause')
