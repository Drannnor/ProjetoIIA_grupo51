import jogos_iia.py

class JogoPeoes(jogos_iia.Game) :

    def __init__(game, state, nivel = 0):# TODO:
        """O construtor."""


        return 

    def actions(self, state):
        """Obtencao das jogadas possiveis, dado um estado do jogo."""
        # TODO:

        
        return

    def result(self,state, move):
        """Obtencao do estado que se obtem ao executar uma dada jogada num dado estado."""
        # TODO:
        return

    def utility(self, state, player):
        """Calculo da utilidade de um estado na perspectiva de um dado jogador.
        Devera ter o valor 1, para o caso de vitoria, ou −1, para o caso de derrota."""
        # TODO:
        return

    def terminal_test(self, state):
        """metodo booleano que verifica se um estado dado eh final."""
        # TODO:
        return


    def display(self, state): #FIXME:
        """Mostra uma representacao de um estado do jogo."""
        dicLinhas = {1 : '5', 2 : '4', 3 : '3', 4 : '2', 5 : '1'}
        dicColunas = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e'}
        board = state.board.tabuleiro
        print("Tabuleiro actual:")
        for x in range(1, 6):
            for y in range(1, 6):
                if y == 1:
                    print(dicLinhas[x], end = '  |')
                
                if (y,x) in board['b'] :
                    print(' b',end = ' |')
                elif (y,x) in board['p'] :
                    print(' p', end = ' |')
                else :
                    print('  ', end = ' |')
                    
            print('------------------------') # 4 traços x 6 vezes = 24 traços
        print('     ' + dicColunas[1] + '   ' + dicColunas[2] + '   ' + dicColunas[3] + '   ' + dicColunas[4] + '   ' + dicColunas[5])
        
        #FIXME:
        #if self.terminal_test(state) :
        #   print("FIM do Jogo")
        #else :
        #    print("Próximo jogador:{}\n".format(state.to_move))