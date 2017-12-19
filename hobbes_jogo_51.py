from collections import namedtuple
import jogos_iia

Board = namedtuple('Board', 'jogadas, tabuleiro')


def find_player(state, player):
    tabuleiro = state.board.tabuleiro
    posicoes = tabuleiro.keys()

    i = 0
    pos = posicoes[i]
    while tabuleiro[pos] != player:
        pos = posicoes[i]
        i += 1

    return pos

class JogoHobbes(jogos_iia.Game):


    def __init__(self):
        """O construtor."""

        self.jogadores = ('rei preto', 'rei branco')
        self.pecas = {'rei preto':'p', 'rei branco':'b', 'neutras':'n'}
        self.size = 5
        tabuleiro_inicial = {(2, 1): 'n', (2, 2): 'n', (2, 4): 'n', (2, 5): 'n',
                             (3, 1): 'p', (3, 2): 'n', (3, 4): 'n', (3, 5): 'b',
                             (4, 1): 'n', (4, 2): 'n', (4, 4): 'n', (4, 5): 'n'}

        movimentos_iniciais = [((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (4, 1))]

        self.state = jogos_iia.GameState(
            to_move=self.jogadores[0],
            utility=0,
            board=Board(0,tabuleiro_inicial),
            moves=movimentos_iniciais)

    def first_step(self, tabuleiro, pos_real, player):
        stepped = {}
        for coluna in range(1, self.size + 1):
            for linha in range(1, self.size + 1):
                stepped[(coluna, linha)] = False

        return self.first_step_rec(tabuleiro, stepped, pos_real, player)

    def first_step_rec(self, tabuleiro, stepped, pos, player):
        (x, y) = pos
        ocup = tabuleiro[pos]

        if ocup == self.pecas['neutras'] and ocup != player and stepped[pos]:
            return []

        stepped[pos] = True
        return [pos] + self.first_step_rec(tabuleiro, stepped, (x + 1, y), player) +\
                       self.first_step_rec(tabuleiro, stepped, (x, y + 1), player) +\
                       self.first_step_rec(tabuleiro, stepped, (x - 1, y), player) +\
                       self.first_step_rec(tabuleiro, stepped, (x, y - 1), player)

    def second_step_direction(self,tabuleiro, pos, dir):

        result = []
        (posx, posy) = pos
        (dirx, diry) = dir
        curr_pos = pos
        while 
        


    def second_step(self, tabuleiro, pos_ini):
        (x, y) = pos_ini

        return self.second_step_direction(tabuleiro, pos_ini, (1, 0))  +\
               self.second_step_direction(tabuleiro, pos_ini, (0, 1))  +\
               self.second_step_direction(tabuleiro, pos_ini, (-1, 0)) +\
               self.second_step_direction(tabuleiro, pos_ini, (0, -1)) 

    def actions(self, state):
        """Obtencao das jogadas possiveis, dado um estado do jogo."""

        result = []
        tabuleiro = state.board.tabuleiro

        pos_real = find_player(state, self.pecas[state.to_move])

        first_steps = self.first_step(tabuleiro, pos_real, state.to_move)
        for pos in first_steps:
            result = result + self.second_step(pos, tabuleiro)

        return result

    def result(self, state, move):
        """Obtencao do estado que se obtem ao executar uma dada jogada num dado estado."""
        # TODO: pelo Nisco
        return

    def utility(self, state, player):
        """Calculo da utilidade de um estado na perspectiva de um dado jogador.
        Devera ter o valor 1, para o caso de vitoria, ou −1, para o caso de derrota."""
        search = 0
        pecas = state.board.tabuleiro.keys() # FIXME: 
        for curr in pecas:
            if pecas[curr] in ('p', 'b'):
                search += 1 if pecas[curr] == self.pecas[player] else -1
        return search

    def terminal_test(self, state):
        return self.utility(state, 'rei branco') != 0 or state.board.jogadas == 50


    def display(self, state): #FIXME:
        """Mostra uma representacao de um estado do jogo."""

        dicLinhas = {1 : '5', 2 : '4', 3 : '3', 4 : '2', 5 : '1'}

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
        print('     A    B   C   D    E')

        #FIXME: isto esta comentado porque?
        #if self.terminal_test(state) :
        #   print("FIM do Jogo")
        #else :
        #    print("Próximo jogador:{}\n".format(state.to_move)