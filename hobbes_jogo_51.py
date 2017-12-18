from collections import namedtuple
import jogos_iia


class JogoHobbes(jogos_iia.Game):

    Board = namedtuple('Board', 'jogadas, tabuleiro')

    def __init__(self):
        """O construtor."""

        self.jogadores = ('rei preto', 'rei branco')
        self.pecas = {'rei preto':'p', 'rei branco':'b'} #FIXME: nao faltam as neutras?
        self.size = 5
        tabuleiro_inicial = {(2, 1): 'n', (2, 2): 'n', (2, 4): 'n', (2, 5): 'n',
                             (3, 1): 'p', (3, 2): 'n', (3, 4): 'n', (3, 5): 'b',
                             (4, 1): 'n', (4, 2): 'n', (4, 4): 'n', (4, 5): 'n'}

        movimentos_iniciais = [((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (4, 1))]

        self.initial = jogos_iia.GameState(
            to_move=self.jogadores[0],
            utility=0,
            board=tabuleiro_inicial,
            moves=movimentos_iniciais)

    def first_step(self, tabuleiro, pos_real): #TODO:
        stepped = {}
        for coluna in range(1, self.size + 1):
            for linha in range(1, self.size + 1):
                stepped[(coluna, linha)] = False

        return self.first_step_rec(tabuleiro, stepped)

    def first_step_rec(self, tabuleiro, stepped): # TODO:

        return

    def second_step(self, tabuleiro, pos):

        return


    def find_player(self, state): # maybe TODO: serah preciso a funcao receber o nome do player,
                                  # caso seja necessario descobrir a posicao do outro jogado
        tabuleiro = state.board.tabuleiro
        posicoes = tabuleiro.keys()

        i = 0
        pos = posicoes[i]
        while tabuleiro[pos] != self.pecas[state.to_move]:
            pos = posicoes[i]
            i += 1

        return pos


    def actions(self, state):
        """Obtencao das jogadas possiveis, dado um estado do jogo."""
        # TODO:
        result = []
        tabuleiro = state.board.tabuleiro

        rei = self.find_player(state)
        first_steps = self.first_step(tabuleiro, rei)
        for pos in first_steps:
            result = result + self.second_step(pos, tabuleiro)
        return result

    def result(self, state, move):
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
        if not self.actions(state) or state.board[0] >= 50: #ou não há mais açoes ou ja se chegou ao limite de jogadas
            return True
        else: # se fazes return o que eh que este else esta aqui a fazer? quando ainda podiam haver jogadas, mas um rei ja estao ao lado do outro
            search = (0, 0)
            for x in range(1, self.size + 1):
                for y in range(x, self.size + 1):
                    if state.board[(x, y)] in ('p', 'b'):
                        if search == (0, 0):
                            search = (x, y)
                        else:
                            (col,lin) = search
                            search = (abs(col - x), abs(lin - y)) # FIXME: podemos usar pathern matching, em vez de search[0] -
                                                                              # (col,lin) = search
                            if (col == 0 and lin <= 1) or (col <= 0 and lin == 1):
                                return True
            return False

    def display(self, state): #FIXME:
        """Mostra uma representacao de um estado do jogo."""

        dicLinhas = {1 : '5', 2 : '4', 3 : '3', 4 : '2', 5 : '1'}
        dicColunas = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e'}
        board = state.board.tabuleiro
        print("Tabuleiro actual:")
        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                if y == 1:
                    print(dicLinhas[x], end='  |')
                elif (y, x) in board['b']:
                    print(' b', end=' |')
                elif (y, x) in board['p']:
                    print(' p', end=' |')
                else:
                    print('  ', end=' |')

            print('------------------------') # 4 traços x 6 vezes = 24 traços
        print('     ' + dicColunas[1] + '   ' + dicColunas[2] + '   ' + dicColunas[3] + '   ' + dicColunas[4] + '   ' + dicColunas[5])
        # FIXME:  NISCO isto continua igual
        # faz com um for, se for para fazer assim nao precisavas do dicionario neh?

        #FIXME: isto esta comentado porque?
        #if self.terminal_test(state) :
        #   print("FIM do Jogo")
        #else :
        #    print("Próximo jogador:{}\n".format(state.to_move))