import sys
import os


def menu(*options):
    """ Menu dinâmico.

    :param options: Tupla de opções ('option1', 'option2', 'option3'...)
    :return: Retorna o número da opção
    """
    os.system('cls')
    
    print("+=============================+")
    print(f"|{'MENU'.center(29)}|")
    print("+-----------------------------+")
    for num, opt in enumerate(options):
        print(f"| {f'[{num+1}] - {opt}':28}|")
    print("+=============================+")

    while True:
        try:
            resposta = int(input("|> "))
            if 0 < resposta <= len(options):
                return resposta
            raise Exception()
        except (ValueError, Exception):
            print(cor("ERRO! Opção inválida, tente novamente...", 4))


"""def erro_cor(txt):
    return '\033[1;31m' + txt + '\033[m'"""


def progressbar(it, prefix='', size=60, file=sys.stdout):
    """ Barra de loading (Necessário ativar a RUM do IDE como saída em terminal)

    :param file:
    :param it: range da barra (ex: range(100))
    :param prefix: Texto de Exibição
    :param size: Tamanho da barra de loading
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


def cor(texto, num_cor=0):
    """ Colore uma string.

    :param cor_txt: Número da cor
    :param txt: String que será colorida
    :return: Retorna a string colorida
    """
    cores = {
        0: '\033[m',       # Neutro
        1: '\033[34m',     # Azul
        2: '\033[32m',     # Verde
        3: '\033[93m',     # Amarelo
        4: '\033[1;31m',   # Vermelho Negrito
        5: '\033[1;7;32m'  # Fundo Verde
    }

    return cores[num_cor] + texto + cores[0]


def verify_entry(txt: str) -> str:
    """ Valida a entrada do usuário, evitando entradas vazias ('')

    Args:
        txt (str): Texto exibido ao usuário

    Returns:
        str: Retorna a resposta do usuário validada
    """
    
    while True:
        resposta = input(txt).strip()

        if resposta == '':
            print(cor('ERRO! Responda com algo válido', 4))
        else:
            return resposta


def continuar(y, n, c=False):
    """ Validação de continuar/parar/cancelar

    :param y: Valor retornará True (ex: "S")
    :param n: Valor retornará False (ex: "N")
    :param c: (opcional) Retorna o valor da resposta
    """
    while True:
        resposta = input("|> ").strip().upper()
        if resposta == str(y).upper():
            return True
        elif resposta == str(n).upper():
            return False
        elif resposta == str(c).upper():
            return c

        print(cor(f'ERRO! Responda apenas "{y}" ou "{n}"', 4), end=' '), print(cor(f'ou "{c}"' if c else '', 4))


def nick_name(arquivo):
    """ Valida o Nick Name e verifica se o mesmo já existe ou não

    :param arquivo: Arquivo .TXT onde está armazenado os placares
    :return: Retorna o Nick-Name caso disponível, retorna False para saída
    """
    os.system('cls')

    while True:
        disponivel = True

        nick = input('Nick Name: ').strip()
        # Saída da criação de Nick-name, caso player não digite nada
        if nick == '':
            return False
        # Nick deve ter entre 3 e 12 caracteres, e ser alpha numérico
        elif 3 <= len(nick) <= 12 and nick.isalnum():
            with open(arquivo, 'r', encoding='UTF-8') as file:
                for name in file.readlines():
                    if name[:name.index(':')].lower() == nick.lower():
                        print(cor('ERRO! Nick Name indisponível\n', 4))
                        disponivel = False
                        break
            if disponivel:
                return nick
        else:
            print(cor('ERRO! Nick Name deve conter apenas letras e/ou números '
                           'de 3 a 12 caracteres no máximo\n', 4))
