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


def continuar(Y, N, C=False):
    """ Validação de continuar/parar/cancelar

    :param y: Valor retornará True (ex: "S")
    :param n: Valor retornará False (ex: "N")
    :param c: (opcional) Retorna o valor da resposta
    """
    while True:
        resposta = input("|> ").strip().upper()
        if resposta == str(Y):
            return True
        elif resposta == str(N):
            return False
        elif resposta == str(C):
            return C

        print(cor(f"ERRO! Opção inválida, tente novamente...", 4))


def nickname(arquivo):
    """ Valida o Nick Name e verifica se o mesmo já existe ou não

    :param arquivo: Arquivo .TXT onde está armazenado os nicknames e pontuações
    :return: Retorna o Nick-Name caso disponível, retorna False para cancelar
    """
    os.system('cls')

    while True:
        nick_available = True

        nick = input('Seu Nickname: ').strip()
        if nick == '':  # Saída da criação de Nickname, caso player não digite nada
            return False
        
        # Nick deve ter entre 3 e 12 caracteres, e ser alpha numérico
        elif 3 <= len(nick) <= 12 and nick.isalnum():
            
            with open(arquivo, 'r', encoding='UTF-8') as file:
                for name in file.readlines():
                    if name[:name.index(':')].lower() == nick.lower():
                        print(cor('ERRO! Nickname indisponível\n', 4))
                        nick_available = False
                        break
            
            if nick_available:
                return nick
        
        else:
            print(cor("ERRO! Nickname deve conter de 3 a 12 caracteres (apenas letras e ou números) \n", 4))
