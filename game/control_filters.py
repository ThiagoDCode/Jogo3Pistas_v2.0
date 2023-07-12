import game
import sys
import os


def menu(*options):
    """ Menu Dict, exemplo: ('1:option1', '2:option2', '3:option3')

    :param options: Parâmetros chave/valor ('1:option1'...)
    :return: Retorna o nome da opção (VALOR da chave)
    """

    os.system('cls')
    tamanho = 30
    opt_dict = {}

    for opt in options:
        opt_split = opt.split(':')
        opt_dict[opt_split[0]] = opt_split[1]

    print(f'+{"=" * tamanho}+')
    print(f'|{"MENU":^{tamanho}}|')
    print(f'+{"-" * tamanho}+')
    for k, v in opt_dict.items():
        print(f'|{f" [{k}] - {v}":{tamanho}}|')
    print(f'+{"=" * tamanho}+')

    while True:
        resposta = input('|> ')

        if resposta not in opt_dict:
            print(erro_cor('ERRO! Opção inválida, tente novamente...'))
        else:
            return opt_dict[resposta]


def erro_cor(txt):
    return '\033[1;31m' + txt + '\033[m'


def progressbar(it, prefix='', size=60, file=sys.stdout):
    """ Barra de loading (Necessário ativar a RUM do IDE como saída em terminal)

    :param it: range da barra (ex: range(100))
    :param prefix: Texto de Exibição
    :param size: tamanho
    """

    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write('%s[%s%s] %i/%i\r' % (prefix, '#' * x, '.' * (size - x), j, count))
        file.flush()

    show(0)

    for cont, item in enumerate(it):
        yield item
        show(cont + 1)
    file.write('\n')
    file.flush()


def cor(cor=0, txt=''):
    """ Colore uma string.

    :param cor: Número da cor
    :param txt: String que será colorida
    :return: Retorna a string colorida
    """

    cores = {
        0: '\033[m',     # Neutro
        1: '\033[34m',   # Azul
        2: '\033[32m',   # Verde
        3: '\033[93m',   # Amarelo
        4: '\033[31m',   # Vermelho
        5: '\033[7;32m'  # Fundo Verde
    }

    return cores[cor] + txt + cores[0]


def verify_entry(txt: str) -> str:
    """ Valida a entrada do usuário

    Args:
        txt (str): Texto exibido ao usuário

    Returns:
        str: Retorna a resposta do usuário validada
    """
    
    while True:
        resposta = input(txt).strip()

        if resposta == '':
            print(erro_cor('ERRO! Responda com algo válido'))
        else:
            return resposta


def continuar(texto, y, n):
    """ Validação de continuar/parar

    :param texto: Texto exibido ao usuário
    :param y: Valor retornará True (ex: "S")
    :param n: Valor retornará False (ex: "N")
    """

    while True:
        resposta = input(texto).strip().lower()
        if resposta == str(y).lower():
            return True
        elif resposta == str(n).lower():
            return False

        print(erro_cor(f'ERRO! Responda apenas "{y}" ou "{n}"...'))


def nick_name(arquivo):
    os.system('cls')

    while True:
        disponivel = True

        nick = input('Nick Name: ').strip()
        if nick == '':
            return False

        elif 3 <= len(nick) <= 12 and nick.isalnum():
            with open(arquivo, 'r', encoding='UTF-8') as file:
                for nick_name in file.readlines():
                    if nick_name[:nick_name.index(':')].lower() == nick.lower():
                        print(erro_cor('ERRO! Nick Name indisponível\n'))
                        disponivel = False
                        break
            if disponivel:
                return nick
        else:
            print(erro_cor('ERRO! Nick Name deve conter apenas letras e/ou números'
                           'de 3 a 12 caracteres no máximo\n'))
