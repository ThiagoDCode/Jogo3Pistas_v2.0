import game
import control_filters as op
from time import sleep
import os


# Cria o arquivo onde serão armazenados os placares
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

{op.cor(2, '[1ª Dica: 10 pontos] [2ª Dica: 8 pontos] [3ª Dica: 6 pontos]').center(84, '=')}
""")
# ------------------------------------------------------------------------------------------------ PRINT


os.system('pause')
game.exibir_placar('placar_geral.txt')
print()
for i in op.progressbar(range(100), 'DCode', 20):
    sleep(0.04)

while True:
    match op.menu('1:INICIAR JOGO', '2:PLACAR GERAL', '3:SAIR DO JOGO'):

        case 'SAIR DO JOGO':
            print(op.cor(2, '\nObrigado por brincar 0/\n'))
            sleep(2), exit()

        case 'INICIAR JOGO':
            nick_name = op.nick_name('placar_geral.txt')
            if not nick_name:
                continue
            print(f'\nVamos aos jogos 🎲, {op.cor(3, nick_name)}')
            sleep(2)

            while True:
                match op.menu('1:JOGAR PALAVRA', '2:PONTUAÇÃO', '3:REINICIAR PARTIDA', '4:FINALIZAR PARTIDA'):
                    case 'FINALIZAR PARTIDA':
                        if not game.save_placar('placar_geral.txt', nick_name, game.pontuacao):
                            continue
                        game.reiniciar_jogo(nova_partida=True)
                        break

                    case 'JOGAR PALAVRA':
                        if not game.palavra_dica():
                            print('\nParabéns! Você ZEROU todas as palavras.\n'), sleep(2)

                    case 'PONTUAÇÃO':
                        game.pontos_acertos(nick_name)

                    case 'REINICIAR PARTIDA':
                        game.reiniciar_jogo()

        case 'PLACAR GERAL':
            game.exibir_placar('placar_geral.txt')
            os.system('pause')
