from palavras import dict_palavras
import menu_filters as op
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

    palavra, dica = choice(list(copia_palavras.items()))
    dica_iter = iter(dica)
    cont_palavra += 1
    copia_palavras.pop(palavra)

    return verificar_resp(palavra, dica_iter)


def verificar_resp(palavra_selecionada, dicas):
    global acertos, pontuacao

    print(f'\n========<< PALAVRA  {cont_palavra}/{len(dict_palavras)} >>========')
    print(f'| {f"Palavra com {len(palavra_selecionada)} letras":^31} |\n'
          f'{"=" * 35}')

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


def pontos_acertos(final=False):
    os.system('cls')

    if final:
        print(f'Palavras acertadas:')
        for acerto in acertos:
            print(f' => {acerto}')
        print(f'Acertos totais: {op.cor(1, str(len(acertos)))}\n'
              f'Pontuação final: {op.cor(1, str(pontuacao) + " pontos")}')
    else:
        print(f'\nVocê teve {len(acertos)} acerto(s): ')
        for acerto in acertos:
            print(f' => {acerto}')
        print(f'Pontuação: {op.cor(1, str(pontuacao) + " pontos")}\n')
        os.system('pause')


def reiniciar_jogo():
    global copia_palavras, acertos, pontuacao, cont_palavra

    print()
    for i in op.progressbar(range(100), 'Reiniciando Jogo: ', 50):
        sleep(0.03)

    copia_palavras = dict_palavras.copy()
    acertos.clear()
    pontuacao = 0
    cont_palavra = 0

    print(f'{op.cor(3, "JOGO REINICIADO COM SUCESSO!")}\n')
    os.system('pause')
