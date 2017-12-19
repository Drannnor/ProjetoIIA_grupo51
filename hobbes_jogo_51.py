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

def other_player(player):
    return "rei preto" if player == "rei branco" else "rei branco"

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

        self.initial = jogos_iia.GameState(
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
        if 
        while

    def second_step(self, tabuleiro, pos_ini, player):
        (x, y) = pos_ini

        if tabuleiro[(x + 1, y)] == self.pecas[other_player(player)]
            return 

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
            result += self.second_step(tabuleiro, pos, state.to_move)

        return result

    def result(self, state, move):
        """Obtencao do estado que se obtem ao executar uma dada jogada num dado estado."""
        # TODO: pelo Nisco
        player = state.to_move
        old_tabuleiro = state.board.tabuleiro
        new_tabuleiro = {}
        ((x1,y1),(x2,y2)) = move
        pos_jogador = find_player(state, self.pecas[player]) #FIXME: pos_jogador => pos_jogador
        posicao_antiga = old_tabuleiro[pos_jogador]
        
        (Vx,Vy) = (x2-x1, y2-y1)
        
        if(Vy == 0): #andou na horizontal
            if(Vx > 0):#andou para a direita
                if(old_tabuleiro[(x1 + 1,y1)] == other_player(pos_jogador)):
                    new_tabuleiro[(x1 + 1,y1)] = pos_jogador  
                elif(old_tabuleiro[(x1 + 1,y1)] == 'n'):
                    pos_neut_old = (x1 + 1,y1)
                    new_tabuleiro[(x2,y2)] = pos_jogador
                    new_tabuleiro[(x2 + 1,y2)] = 'n'
                else:
                    pos_neut_old = (x1 - 1,y1)
                    new_tabuleiro[(x2,y2)] = pos_jogador
                    new_tabuleiro[(x2 - 1,y2)] = 'n'  

            else:# andou para a esquerda
                if(old_tabuleiro[(x1 - 1,y1)] == other_player(pos_jogador)):
                    new_tabuleiro[(x1 - 1,y1)] = pos_jogador
                    
                elif(old_tabuleiro[(x1 - 1,y1)] == 'n'):
                    pos_neut_old = (x1 - 1,y1)
                    new_tabuleiro[(x2,y2)] = pos_jogador
                    new_tabuleiro[(x2 - 1,y2)] = 'n'
                else:
                    pos_neut_old = (x1 + 1,y1)
                    new_tabuleiro[(x2,y2)] = pos_jogador
                    new_tabuleiro[(x2 + 1,y2)] = 'n'

        else: #andou na vertical
            if(Vy > 0):#andou para cima
                if(old_tabuleiro[(x1,y1 + 1)] == other_player(pos_jogador)):
                    new_tabuleiro[(x1,y1 + 1)] = pos_jogador
                    
                elif(old_tabuleiro[(x1,y1 + 1)] == 'n'):
                    pos_neut_old = (x1,y1 + 1)
                    new_tabuleiro[(x2,y2)] = pos_jogador
                    new_tabuleiro[(x2,y2 + 1)] = 'n'
                else:
                    pos_neut_old = (x1,y1 - 1)
                    new_tabuleiro[(x2,y2)] = pos_jogador
                    new_tabuleiro[(x2,y2 - 1)] = 'n'
                    
            else: # andou para baixo
                if(old_tabuleiro[(x1,y1 - 1)] == other_player(pos_jogador)):
                    new_tabuleiro[(x1,y1 - 1)] = pos_jogador
                    
                elif(old_tabuleiro[(x1,y1 - 1)] == 'n'):
                    pos_neut_old = (x1,y1 - 1)
                    new_tabuleiro[(x2,y2)] = pos_jogador
                    new_tabuleiro[(x2,y2 - 1)] = 'n'
                else:
                    pos_neut_old = (x1,y1 + 1)
                    new_tabuleiro[(x2,y2)] = pos_jogador
                    new_tabuleiro[(x2,y2 + 1)] = 'n'

        board_key_list = old_tabuleiro.keys()
        for pos in board_key_list:
            if(pos != pos_neut_old AND pos != posicao_antiga):
                new_tabuleiro[(pos)] = old_tabuleiro[(pos)]

        result = jogos_iia.GameState(
            to_move = other_player(state.to_move),
            utility = self.calcular_utilidade(new_tabuleiro,other_player(player)), #FIXME: TODO:
            board = (state.board[0] + 1, new_tabuleiro),
            moves = self.possible_moves(new_tabuleiro, other_player(player))) #TODO:

        return result
    
    def calcular_utilidade(tabuleiro, player):
        res = 0
        pcs = tabuleiro.keys()# FIXME: DIOOOOGOOOOOO!!!!
        for curr in pecas:
            if pcs[curr] in ('p', 'b'):
                res += 1 if pcs[curr] == self.pecas[player] else -1
        return res

    def utility(self, state, player):
        """Calculo da utilidade de um estado na perspectiva de um dado jogador.
        Devera ter o valor 1, para o caso de vitoria, ou −1, para o caso de derrota."""

        return state.utility

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
