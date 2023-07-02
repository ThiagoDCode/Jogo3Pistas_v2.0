"""
Complementos de Personalização e Validação.
"""

import sys
import os


def menu(*options):
    """
    Menu ex: ('option1', 'option2', 'option3')

    :param options: Lista de opções
    :return: Retorna o número da opção
    """

    os.system('cls')
    tamanho = 30

    print(f'+{"=" * tamanho}+')
    print(f'|{"MENU":^{tamanho}}|')
    print(f'+{"-" * tamanho}+')
    for c, op in enumerate(options):
        print(f'|{f" {c+1} - {op}":{tamanho}}|')
    print(f'+{"=" * tamanho}+')

    while True:
        try:
            resposta = int(input('|> '))
        except ValueError:
            print(erro_cor('ERRO! Digite apenas um número INTEIRO...'))
        else:
            if 0 < resposta <= len(options):
                return resposta
            else:
                print(erro_cor('ERRO! Opção inválida, tente novamente...'))


def continuar_parar(continuar, parar, text=''):
    """
    Validação de parada ou continuar

    :param continuar: Valor de continuidade (ex: "S")
    :param parar: Valor de parada (ex: "N")
    :param text: Texto de exibição
    :return: Retorna True ou False
    """

    resposta = ' '
    while continuar != resposta != parar:
        resposta = input(text).strip()

        if resposta.upper() == continuar:
            return True
        elif resposta.upper() == parar:
            return False

        print(erro_cor(f'ERRO! Responda apenas "{continuar}" ou "{parar}"...'))


def erro_cor(txt):
    return '\033[1;31m' + txt + '\033[m'


def progressbar(it, prefix='', size=60, file=sys.stdout):
    """
    Barra de loading

    :param it: range da barra (ex: range(100))
    :param prefix: Texto de Exibição
    :param size: tamanho
    """

    count = len(it)

    def show(j):
        x = int(size*j/count)
        file.write('%s[%s%s] %i/%i\r' % (prefix, '#'*x, '.'*(size-x), j, count))
        file.flush()
    show(0)

    for cont, item in enumerate(it):
        yield item
        show(cont+1)
    file.write('\n')
    file.flush()


def cor(cor=0, txt=''):
    """
    Colore uma string.
    :param cor: Número da cor
    :param txt: String que será colorida
    :return: Retorna a string colorida
    """

    cores = {
        0: '\033[m',    # Neutro
        1: '\033[34m',  # Azul
        2: '\033[32m',  # Verde
        3: '\033[93m',  # Amarelo
        4: '\033[31m'   # Vermelho
    }

    return cores[cor] + txt + cores[0]
