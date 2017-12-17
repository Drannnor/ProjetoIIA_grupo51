import jogos_iia

table_size = 5

class JogoHobbes(jogos_iia.Game):

    def __init__(self):
        """O construtor."""
        # TODO:
        return

    def actions(self, state):
        """Obtencao das jogadas possiveis, dado um estado do jogo."""
        # TODO:
        result = []
        tabuleiro = state.board.tabuleiro
        posicoes = 
        rei
        first_steps = self.first_step(tabuleiro, rei)
        for pos in first_steps:
            result = result + self.second_step(pos,tabuleiro)
        return result

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
        board = state.board.tabuleiro #FIXME: para poderes fazer isto tens de "criar" a estrutura Board, tal como o stor faz com o GameState
        print("Tabuleiro actual:")
        for x in range(1, 6):
            for y in range(1, 6):
                if y == 1:
                    print(dicLinhas[x] + '  |')
                if (y,x) in board['b']:
                    print(' b |')
                elif (y,x) in board['p']:
                    print(' p |')
                else:
                    print('   |')
                    
            print('------------------------') # 4 traços x 6 vezes = 24 traços
        print('     ' + dicColunas[1] + '   ' + dicColunas[2] + '   ' + dicColunas[3] + '   ' + dicColunas[4] + '   ' + dicColunas[5])# FIXME: 
                                                                                                                                      # faz com um for, se for para fazer assim nao precisavas do dicionario neh?     
        #FIXME:
        #if self.terminal_test(state) :
        #   print("FIM do Jogo")
        #else :
        #    print("Próximo jogador:{}\n".format(state.to_move))
        

    def first_step(self, tabuleiro): #TODO:
        stepped = {}
        for coluna in range(1, table_size):
            for linha in range(1, table_size):
                stepped[(coluna, linha)] = False

        return self.first_step_rec(tabuleiro, stepped)

    def first_step_rec(self, tabuleiro, stepped): # TODO:
        
        return

    def second_step(self, tabuleiro, pos):

        return