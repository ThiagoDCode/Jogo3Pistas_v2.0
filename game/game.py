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


def pontos_acertos(final=False):
    os.system('cls')

    if final:  # TODO: invés, será exibido o rankin dos 10 primeiros, por exemplo
        print(cor(3, '<< FIM DE JOGO! >>'.center(50, '=')),
              f'\nPalavras acertadas:')
        for acerto in acertos:
            print(f' => {acerto}')
        print(f'Acertos totais: {cor(1, str(len(acertos)))}\n'
              f'Pontuação final: {cor(1, str(pontuacao) + " pontos")}\n')
    else:
        print(cor(3, '<< PONTUAÇÃO >>'.center(50, '=')),
              f'\nVocê teve {len(acertos)} acerto(s): ')
        for acerto in acertos:
            print(f' => {acerto}')
        print(f'Pontuação: {cor(1, str(pontuacao) + " pontos")}\n')
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


def nick_name():
    os.system('cls')
    while True:
        nick = input('Nick Name: ').strip()
        if 3 <= len(nick) <= 12:
            return nick
        else:
            print(erro_cor('ERRO! Nick Name deve conter de 3 a 12 caracteres no máximo'))


def save_placar(arquivo, nick, pontos):
    placar = [{nick: pontos}]
    if not os.path.exists(arquivo):
        with open(arquivo, 'w', encoding='UTF-8') as save:
            save.write(f'{nick}:{pontos}\n')
            save.close()
    else:
        with open(arquivo, 'a', encoding='UTF-8') as save:
            save.write(f'{nick}:{pontos}\n')
            save.close()


def exibir_placar(arquivo):
    lista_placares = []
    try:
        with open(arquivo, 'r', encoding='UTF-8') as file:
            for placar in file.readlines():
                placar = placar.split(':')
                lista_placares.append([placar[0], placar[1].replace('\n', '')])

        ranking = sorted(lista_placares, key=itemgetter(1), reverse=True)
        for rank in ranking:
            print(f'Nick: {rank[0]} -> Pontuação: {rank[1]}')

    except FileNotFoundError:
        print(erro_cor('\nERRO! Arquivo não encontrado\n'))
        os.system('pause')


if __name__ == '__main__':
    print(nick_name())
