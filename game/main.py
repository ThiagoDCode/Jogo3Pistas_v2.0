import game
import control_filters as op
from time import sleep
import os


# Cria o arquivo onde serão armazenados as pontuações
if not os.path.exists('placar_geral.txt'):
    with open('placar_geral.txt', 'w', encoding='UTF-8') as file:
        file.write(f'{"Bot"}:{6}\n')
        file.close()


os.system('cls')
# PRINT ------------------------------------------------------------------------------------------------
print(f"""
{'='*76}
|{'JOGO DAS 3 PISTAS'.center(74)}|
{'[ Regras ]'.center(76, '=')}
1. Você deve descobrir a palavra secreta através das pistas dadas!
2. Você tem até 3 tentativas; cada tentativa te dá uma dica extra!
3. Cada dica vale uma pontuação, quanto menos tentativas, maior a pontuação!

{op.cor('[1ª Dica: 10 pontos] [2ª Dica: 8 pontos] [3ª Dica: 6 pontos]', 2).center(84, '=')}
""")
# ------------------------------------------------------------------------------------------------ PRINT
os.system('pause')


game.exibir_placar('placar_geral.txt'), print()
for i in op.progressbar(range(100), 'DCode', 20):
    sleep(0.04)


while True:
    match op.menu('INICIAR JOGO', 'PLACAR GERAL', 'SAIR DO JOGO'):

        case 3:  # SAIR DO JOGO
            print(op.cor('\nObrigado por brincar 0/\n', 2))
            sleep(2), exit()

        case 1:  # INICIAR JOGO
            nick_name = op.nick_name('placar_geral.txt')
            if not nick_name:
                continue
            print(f'\nVamos aos jogos 🎲, {op.cor(nick_name, 3)}')
            sleep(2)

            while True:
                match op.menu('JOGAR PALAVRA', 'PONTUAÇÃO', 'REINICIAR PARTIDA', 'FINALIZAR PARTIDA'):
                    case 4:  # FINALIZAR PARTIDA
                        if not game.save_placar('placar_geral.txt', nick_name, game.pontuacao):
                            continue
                        game.reiniciar_jogo(nova_partida=True)
                        break

                    case 1:  # JOGAR PALAVRA
                        if not game.palavra_dica():
                            print('\nParabéns! Você ZEROU todas as palavras.\n'), sleep(2)

                    case 2:  # PONTUAÇÃO
                        game.pontos_acertos(nick_name)

                    case 3:  # REINICIAR PARTIDA
                        game.reiniciar_jogo()

        case 2:  # PLACAR GERAL
            game.exibir_placar('placar_geral.txt')
            os.system('pause')
