from palavras import dict_palavras
from control_filters import *
from random import choice
from time import sleep
from operator import itemgetter
import os

palavras_jogadas = 0
acertos = []
pontuacao = 0
copia_palavras = dict_palavras.copy()
record = []
lista_placares = []


def jogar_palavra():
    """ Seleciona a palavra (e suas dicas) para o jogo

    :return: False (caso não haja mais palavras para jogar)
    """
    os.system('cls')
    global palavras_jogadas

    # Verifica se ainda há palavras para jogar
    if not copia_palavras:
        return False

    palavra_selecionada, dicas_palavra = choice(list(copia_palavras.items()))  # Seleciona a palavra e dicas a ser jogada
    palavras_jogadas += 1                                                      # Contabiliza ao total de palavras jogadas
    copia_palavras.pop(palavra_selecionada)                                    # Remove a palavra jogada

    return verificar_resp(palavra_selecionada, dicas_palavra)


def verificar_resp(palavra, dicas):
    """ Exibe as dicas da palavra secreta, e compara a resposta do player com a palavra secreta.
    Adicionando a pontuação do player, de acordo com sua resposta e dica usada.

    :param palavra: Palavra secreta selecionada
    :param dicas: Dicas da palavra secreta selecionada
    :return: Finaliza a jogada
    """
    global acertos, pontuacao
    dica_iter = iter(dicas)

    for cont, pontos in enumerate([10, 8, 6]):
        os.system('cls')

        # PRINT ---------------------------------------------------------------------------------------------
        print(f'<< PALAVRA  {palavras_jogadas}/{len(dict_palavras)} >>'.center(52, '='))
        print(f'| {f"Palavra com {len(palavra)} letras":^48} |\n'
              f'{"=" * 52}')
        for dica in dicas[:cont + 1]:
            print(cor(f'[ {dica.upper()} ]', 5), end=' ')
        print()
        # --------------------------------------------------------------------------------------------- PRINT

        print(f'\nA {cont + 1}ª dica é [{cor(next(dica_iter), 2)}], Qual a palavra? ')
        while True:
            resposta = input('|> ')
            if resposta == "":
                print(cor("ERRO! Resposta inválida, tente novamente...", 4))
            else:
                break

        # Verifica a resposta
        if resposta.lower() == palavra:
            print(f'\nAcertou! {cor(palavra.upper(), 1)} => ganhou {cor(str(pontos) + " pontos", 1)}\n')

            # Adiciona a palavra e pontos na lista "acertos", e soma os pontos na pontuação total "pontuacao"
            acertos.append(f'{cor(palavra.upper(), 1)} (acertou na {cont + 1}ª dica: {pontos}P)')
            pontuacao += pontos

            sleep(1)
            break

        else:
            # Se errada, passa para a próxima dica
            print(f'\n{cor("ERROOOUU!", 3)}', end=' ')
            print('Próxima dica...\n' if cont < 2 else 'Que pena, mas sorte na próxima!\n')
            sleep(1)
    
    print("[ 1 ] Próxima Palavra \n[ 2 ] Voltar ao Menu")
    if continuar(1, 2):
        jogar_palavra()

    return True


def pontos_acertos(nick_pts=''):
    """ Exibe a pontuação atual do player

    :param nick_pts: (opcional) Exibe o nick name do player, quando bate recorde
    """
    os.system('cls')

    # PRINT (pontuação) --------------------------------------------------------------------
    print(f'<< {cor("SUA PONTUAÇÃO", 1)} >>'.center(50, '='),
          f'\nVocê teve {len(acertos)} acerto(s):')
    for acerto in acertos:
        print(f' => {acerto}')
    print(f'\nPontuação total: {cor(str(pontuacao) + " pontos", 1)}\n'
          f'{"-" * 42}')

    # PRINT (record) -----------------------------------------------------------------------
    if pontuacao > record[1]:
        print(f'Parabéns 🎉 {cor(nick_pts, 3)}, é o novo Recordista\n')
        print(f' RECORD [ {pontuacao}P 👑{cor(nick_pts, 3)} ]'.center(49))
    else:
        print(f'RECORD [ {record[1]}P 👑{cor(record[0], 3)} ]'.center(49))
    print()
    # -------------------------------------------------------------------------------- PRINT
    os.system('pause')


def reiniciar_jogo(nova_partida=False):
    """ Reinicia a partida, zerando a pontuação e palavras jogadas

    :param nova_partida: (opcional) Usada para reiniciar o jogo, sempre ao iniciar uma nova partida
    """
    os.system('cls')
    global copia_palavras, acertos, pontuacao, palavras_jogadas

    if nova_partida:
        copia_palavras = dict_palavras.copy()
        acertos.clear()
        pontuacao = 0
        palavras_jogadas = 0
    else:
        print(f'\n{cor("ATENÇÃO!", 4)}: Isso reiniciará o jogo, zerando sua pontuação! '
              f'Deseja continuar [S/N]?')
        if continuar('S', 'N'):
            print()
            for i in progressbar(range(100), 'Reiniciando Partida: ', 30):
                sleep(0.03)

            copia_palavras = dict_palavras.copy()
            acertos.clear()
            pontuacao = 0
            palavras_jogadas = 0

            print(f'{cor("PARTIDA REINICIADA COM SUCESSO!", 3)}\n')
            os.system('pause')


def save_placar(arquivo, nick, pontos):
    """ Salva no arquivo o Nick name do player e sua pontuação

    :param arquivo: Arquivo .TXT
    :param nick: Nick Name do player
    :param pontos: Pontuação do player
    """

    print("\nSair e salvar pontuação [S/N] ou [C] para cancelar? ")
    resposta = continuar('S', 'N', 'C')

    if pontos != 0 and resposta is True:
        with open(arquivo, 'a', encoding='UTF-8') as save:
            save.write(f'{nick}:{pontos}\n')
            save.close()

        for i in progressbar(range(100), 'Salvando: ', 22):
            sleep(0.04)
        print(cor('\nPONTUAÇÃO SALVA COM SUCESSO!', 3))
        os.system('pause')
        return True
    elif resposta == 'C':
        return False
    else:
        return True


def exibir_placar(arquivo):
    """ Exibe o ranking de placares dos players

    :param arquivo: Arquivo .TXT com os placares armazenados
    """
    os.system('cls')
    global record

    try:
        with open(arquivo, 'r', encoding='UTF-8') as file:
            placares = file.readlines()
            file.close()

        # Separa Nick-name e Pontuação de acordo com, os dois pontos (:)
        # Adiciona Nick e Pontuação numa lista, removendo a expressão "\N" da pontuação
        for placar in placares:
            placar = placar.split(':')
            lista_placares.append([placar[0], int(placar[1].replace('\n', ''))])

        # Ordena a lista de placares de acordo com os valores numéricos
        ranking = sorted(lista_placares, key=itemgetter(1), reverse=True)
        cont = 0

        # PRINT -------------------------------------------------------------------------------------
        print(f'<< RANKING >>'.center(33, '='))
        print(f'| {"Noª"} {"NICK":<15} {"PONTUAÇÃO"} |')
        print(f'-' * 33)
        for nick, pontos in ranking:
            if cont == 0:
                record = [nick, pontos]
                print(f'|{"👑":>2}  {cor(f"{nick:.<15}", 3)} {cor(f"{pontos:<3} Record", 3)}|')
            else:
                print(f'| {cont + 1:^3} {nick:.<15} {pontos:<10}|')
            if cont == 8:
                break
            cont += 1
        print(f"{'=' * 33} \n")
        # ------------------------------------------------------------------------------------- PRINT

        # Limpa a lista para receber novas consultas
        lista_placares.clear()

    except FileNotFoundError:
        print(cor('\nERRO! Arquivo não encontrado\n', 4))
