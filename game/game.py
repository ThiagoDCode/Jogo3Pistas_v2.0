from palavras import lista_palavras
from control_filters import *
from random import choice
from time import sleep
from operator import itemgetter
import os

copia_palavras = lista_palavras.copy()  # Faz uma cópia da Lista de Palavras
palavras_jogadas = 0                    # Número de palavras jogadas
acertos = []                            # Guarda as palavras acertadas pelo jogador
pontos_jogador = 0                      # Pontuação total do jogador
record = []                             # Armazena o recordista do ranking
lista_raking = []                       # Armazena o ranking de jogadores


def jogar_palavra():
    
    global palavras_jogadas, pontos_jogador
    global acertos

    if not copia_palavras:
        print(f"\nParabéns você ZEROU O GAME! Sua pontuação final foi de: {cor(str(pontos_jogador), 1)} PONTOS \n")
        os.system("pause")
        return False

    palavra_selecionada, dicas_palavra = choice(list(copia_palavras.items()))
    palavras_jogadas += 1

    # Loop com cada dica e sua respectiva pontuação
    for cont, pontos in enumerate([10, 8, 6]):
        os.system("cls")

        # PRINT ---------------------------------------------------------------------------------------------
        print(f"<< PALAVRA {palavras_jogadas}/{len(lista_palavras)} >>".center(52, "="))
        print(f"| {f'Palavra com {len(palavra_selecionada)} letras':^48} |")
        print("="*52)
        for dica in dicas_palavra[:cont+1]:
            print(cor(f"[ {dica.upper()} ]", 5), end=' ')
        print("\n")
        # --------------------------------------------------------------------------------------------- PRINT

        print(f"A {cont+1}ª dica é [{cor(dicas_palavra[cont], 2)}]. Qual a palavra?")
        while True:
            resposta = input("|> ")
            if resposta == "":
                print(cor("ERRO! Resposta inválida, tente novamente...", 4))
                continue
            break

        # Verificação da resposta
        if resposta.lower() == palavra_selecionada:
            print(f"\nACERTOU!!! {cor(palavra_selecionada.upper(), 1)} => ganhou {cor(str(pontos), 1)} pontos \n")

            acertos.append(f"{cor(palavra_selecionada.upper(), 1)} (Acertou na {cont+1}ª dica: +{pontos}P)")
            pontos_jogador += pontos

            sleep(1)
            break

        # Se resposta errada, passa para a próxima dica
        else:
            print(f"\n{cor('ERROOOUU!!!', 3)}", end=' ')
            print("Próxima dica... \n" if cont < 2 else "Que pena, mas sorte na próxima! \n")
            sleep(1)

    copia_palavras.pop(palavra_selecionada)  # Remove a palavra jogada da lista de palavras
    
    print("[ 1 ] PRÓXIMA PALAVRA \n[ 2 ] VOLTAR AO MENU")
    if continuar(1, 2):
        jogar_palavra()


def pontos_acertos(nick_pts=''):
    """ Exibe a pontuação atual do player

    :param nick_pts: (opcional) Exibe o nick name do player, quando bate recorde
    """
    os.system('cls')

    # PRINT (pontuação) --------------------------------------------------------------------
    print(f"<< {cor('SUA PONTUAÇÃO', 1)} >>".center(50, "="))
    print(f"Você teve {len(acertos)} acerto(s)".center(42))
    for acerto in acertos:
        print(f' => {acerto}')
    print(f'\nPontuação atual: {cor(str(pontos_jogador) + " pontos", 1)}')
    print(f"-"*42)

    # PRINT (record) -----------------------------------------------------------------------
    if pontos_jogador > record[1]:
        print(f'Parabéns 🎉 {cor(nick_pts, 3)}, é o novo Recordista!\n')
        print(f' RECORD [ {pontos_jogador}P 👑{cor(nick_pts, 3)} ]'.center(49))
    else:
        print(f'RECORD [ {record[1]}P 👑{cor(record[0], 3)} ]'.center(49))
    print()
    # -------------------------------------------------------------------------------- PRINT
    os.system('pause')


def restart_game(reiniciar_partida=False):
    """ Reinicia a partida.

    Args:
        reiniciar_partida (bool, optional): True reinicia a partida e pontuação do jogador. Defaults to False.
    """
    os.system('cls')
    global copia_palavras, acertos
    global pontos_jogador, palavras_jogadas
    
    if reiniciar_partida:
        for i in progressbar(range(100), 'Reiniciando Partida: ', 30):
            sleep(0.02)

    copia_palavras = lista_palavras.copy()
    acertos.clear()
    pontos_jogador = 0
    palavras_jogadas = 0


def save_placar(arquivo, nick, pontos):
    """ Salva no arquivo o Nickname do jogador e sua pontuação.

    :param arquivo: Arquivo .TXT
    :param nick: Nickname do jogador
    :param pontos: Pontuação do jogador
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
            lista_raking.append([placar[0], int(placar[1].replace('\n', ''))])

        # Ordena a lista de placares de acordo com os valores numéricos
        ranking = sorted(lista_raking, key=itemgetter(1), reverse=True)
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
        lista_raking.clear()

    except FileNotFoundError:
        print(cor('\nERRO! Arquivo não encontrado\n', 4))
