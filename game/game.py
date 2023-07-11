import string

from palavras import dict_palavras
from control_filters import *
from random import choice
from time import sleep
from operator import itemgetter
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
        return pontos_acertos()

    palavra_selecionada, dicas_palavra = choice(list(copia_palavras.items()))
    cont_palavra += 1
    copia_palavras.pop(palavra_selecionada)

    return verificar_resp(palavra_selecionada, dicas_palavra)


def verificar_resp(palavra, dicas):
    global acertos, pontuacao
    dica_iter = iter(dicas)

    for cont, pontos in enumerate([10, 8, 6]):
        os.system('cls')

        print(f'<< PALAVRA  {cont_palavra}/{len(dict_palavras)} >>'.center(52, '='))
        print(f'| {f"Palavra com {len(palavra)} letras":^48} |\n'
              f'{"=" * 52}')
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
            sleep(2)

    os.system('pause')
    return True


def pontos_acertos(nick_exibe):
    os.system('cls')

    print(cor(3, f'<< {nick_exibe} >>'.center(50, '=')),
          f'\nVocê teve {len(acertos)} acerto(s): ')
    for acerto in acertos:
        print(f' => {acerto}')
    print(f'Pontuação total: {cor(1, str(pontuacao) + " pontos")}\n'
          f'{"-" * 50}')
    os.system('pause')


def reiniciar_jogo(nova_partida=False):
    os.system('cls')
    global copia_palavras, acertos, pontuacao, cont_palavra

    if nova_partida:
        copia_palavras = dict_palavras.copy()
        acertos.clear()
        pontuacao = 0
        cont_palavra = 0
    else:
        print(f'\n{cor(4, "ATENÇÃO!")}: Isso reiniciará o jogo, zerando sua pontuação!')
        if continuar('Deseja reiniciar? [S/N]: ', 'S', 'N'):
            print()
            for i in progressbar(range(100), 'Reiniciando Jogo: ', 50):
                sleep(0.03)

            copia_palavras = dict_palavras.copy()
            acertos.clear()
            pontuacao = 0
            cont_palavra = 0

            print(f'{cor(3, "JOGO REINICIADO COM SUCESSO!")}\n')
            os.system('pause')


def save_placar(arquivo, nick, pontos):
    if pontos != 0:
        with open(arquivo, 'a', encoding='UTF-8') as save:
            save.write(f'{nick}:{pontos}\n')
            save.close()


def exibir_placar(arquivo):
    os.system('cls')
    lista_placares = []

    try:
        with open(arquivo, 'r', encoding='UTF-8') as file:
            for placar in file.readlines():
                placar = placar.split(':')
                lista_placares.append([placar[0], placar[1].replace('\n', '')])

        ranking = sorted(lista_placares, key=itemgetter(1), reverse=True)
        # PRINT -------------------------------------------------------------------------------------
        print(f'<< RANKING >>'.center(33, '='))
        print(f'| {"Noª"} {"NICK":<15} {"PONTUAÇÃO"} |')
        print(f'-' * 33)
        for c, rank in enumerate(ranking):
            if c == 0:
                print(f'|{"👑":^3} {cor(3, f"{rank[0]:.<15}")} {cor(3, f"{rank[1]:<3} Record")}|')
            else:
                print(f'| {c+1:^3} {rank[0]:.<15} {rank[1]:<10}|')
            if c == 8:
                break
        print('=' * 33)
        # ------------------------------------------------------------------------------------- PRINT

    except FileNotFoundError:
        print(erro_cor('\nERRO! Arquivo não encontrado\n'))
