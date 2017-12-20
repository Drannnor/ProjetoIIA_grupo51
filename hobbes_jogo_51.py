from collections import namedtuple

import jogos_iia

Board = namedtuple('Board', 'jogadas, tabuleiro')
BOARDSIZE = 5


def find_player(tabuleiro, player):

    posicoes = tabuleiro.keys()

    for pos in posicoes:
        if tabuleiro[pos] == player:
            return pos

    return None


def other_player(player):
    return "rei preto" if player == "rei branco" else "rei branco"


class JogoHobbes(jogos_iia.Game):

    def __init__(self):
        """O construtor."""

        self.jogadores = ('rei preto', 'rei branco')
        self.pecas = {'rei preto': 'p', 'rei branco': 'b', 'neutras': 'n'}
        self.size = BOARDSIZE
        tabuleiro_inicial = {(2, 1): 'n', (2, 2): 'n', (2, 4): 'n', (2, 5): 'n',
                             (3, 1): 'p', (3, 2): 'n', (3, 4): 'n', (3, 5): 'b',
                             (4, 1): 'n', (4, 2): 'n', (4, 4): 'n', (4, 5): 'n'}

        movimentos_iniciais = [((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (4, 1))]

        self.initial = jogos_iia.GameState(
            to_move=self.jogadores[0],
            utility=0,
            board=Board(0, tabuleiro_inicial),
            moves=movimentos_iniciais)

    def valida(self, posicao):
        (x, y) = posicao
        return self.size >= x > 0 and self.size >= y > 0

    def possible_moves(self, tabuleiro, player):
        result = []
        pos_real = find_player(tabuleiro, self.pecas[player])
        enemy = other_player(player)

        def first_step():
            stepped = {}
            for coluna in range(1, self.size + 1):
                for linha in range(1, self.size + 1):
                    stepped[(coluna, linha)] = False

            def first_step_rec(pos):
                (x, y) = pos

                if pos not in stepped or (pos in tabuleiro and (tabuleiro[pos] == self.pecas['neutras'] or
                                                                tabuleiro[pos] != player)):
                    return []

                stepped[pos] = True
                return [pos] + first_step_rec((x + 1, y)) + \
                       first_step_rec((x, y + 1)) + \
                       first_step_rec((x - 1, y)) + \
                       first_step_rec((x, y - 1))

            return first_step_rec(pos_real)

        def second_step(pos_ini):

            def second_step_direction(direction):
                res = []
                (dirx, diry) = direction
                (posx, posy) = pos_ini
                push = False
                curr_x = posx + dirx
                curr_y = posy + diry

                if not self.valida((curr_x, curr_y)):
                    return res

                if tabuleiro[(curr_x, curr_y)] == self.pecas[enemy]:
                    return [(pos_ini, (curr_x, curr_y))]

                if tabuleiro[(curr_x, curr_y)] == self.pecas['neutra']:
                    curr_x += dirx
                    curr_y += diry
                    push = True
                elif tabuleiro[(posx - dirx, posy - diry)] != self.pecas['neutra']:
                    return res

                while self.valida((curr_x, curr_y)) and tabuleiro[(curr_x, curr_y)] not in ['n', self.pecas[enemy]]:
                    if push:
                        res.append((pos_ini, (curr_x - dirx, curr_y - diry)))
                    else:
                        res.append((pos_ini, (curr_x, curr_y)))

            return second_step_direction((1, 0)) + \
                   second_step_direction((0, 1)) + \
                   second_step_direction((-1, 0)) + \
                   second_step_direction((0, -1))

        first_steps = first_step()
        for posi in first_steps:
            result += second_step(posi)
        return result

    def actions(self, state):
        """Obtencao das jogadas possiveis, dado um estado do jogo."""
        return state.moves

    def result(self, state, move):
        """Obtencao do estado que se obtem ao executar uma dada jogada num dado estado."""
        player = state.to_move
        old_tabuleiro = state.board.tabuleiro
        new_tabuleiro = {}
        ((x1, y1), (x2, y2)) = move
        pos_jogador = find_player(old_tabuleiro, self.pecas[player])
        posicao_antiga = old_tabuleiro[pos_jogador]
        pos_neut_old = (0, 0)

        (Vx, Vy) = (x2 - x1, y2 - y1)

        if Vy == 0:  # andou na horizontal
            if Vx > 0:  # andou para a direita
                if old_tabuleiro[(x1 + 1, y1)] == other_player(pos_jogador):
                    new_tabuleiro[(x1 + 1, y1)] = pos_jogador

                elif old_tabuleiro[(x1 + 1, y1)] == 'n':
                    pos_neut_old = (x1 + 1, y1)
                    new_tabuleiro[(x2, y2)] = pos_jogador
                    new_tabuleiro[(x2 + 1, y2)] = 'n'
                else:
                    pos_neut_old = (x1 - 1, y1)
                    new_tabuleiro[(x2, y2)] = pos_jogador
                    new_tabuleiro[(x2 - 1, y2)] = 'n'

            else:  # andou para a esquerda
                if old_tabuleiro[(x1 - 1, y1)] == other_player(pos_jogador):
                    new_tabuleiro[(x1 - 1, y1)] = pos_jogador

                elif old_tabuleiro[(x1 - 1, y1)] == 'n':
                    pos_neut_old = (x1 - 1, y1)
                    new_tabuleiro[(x2, y2)] = pos_jogador
                    new_tabuleiro[(x2 - 1, y2)] = 'n'
                else:
                    pos_neut_old = (x1 + 1, y1)
                    new_tabuleiro[(x2, y2)] = pos_jogador
                    new_tabuleiro[(x2 + 1, y2)] = 'n'

        else:  # andou na vertical
            if Vy > 0:  # andou para cima
                if old_tabuleiro[(x1, y1 + 1)] == other_player(pos_jogador):
                    new_tabuleiro[(x1, y1 + 1)] = pos_jogador

                elif old_tabuleiro[(x1, y1 + 1)] == 'n':
                    pos_neut_old = (x1, y1 + 1)
                    new_tabuleiro[(x2, y2)] = pos_jogador
                    new_tabuleiro[(x2, y2 + 1)] = 'n'
                else:
                    pos_neut_old = (x1, y1 - 1)
                    new_tabuleiro[(x2, y2)] = pos_jogador
                    new_tabuleiro[(x2, y2 - 1)] = 'n'

            else:  # andou para baixo
                if old_tabuleiro[(x1, y1 - 1)] == other_player(pos_jogador):
                    new_tabuleiro[(x1, y1 - 1)] = pos_jogador

                elif old_tabuleiro[(x1, y1 - 1)] == 'n':
                    pos_neut_old = (x1, y1 - 1)
                    new_tabuleiro[(x2, y2)] = pos_jogador
                    new_tabuleiro[(x2, y2 - 1)] = 'n'
                else:
                    pos_neut_old = (x1, y1 + 1)
                    new_tabuleiro[(x2, y2)] = pos_jogador
                    new_tabuleiro[(x2, y2 + 1)] = 'n'

        board_key_list = old_tabuleiro.keys()
        for pos in board_key_list:
            if pos != pos_neut_old and pos != posicao_antiga:
                new_tabuleiro[pos] = old_tabuleiro[pos]

        to_be_moves = self.possible_moves(new_tabuleiro, other_player(player))
        next_player = other_player(state.to_move)
        result = jogos_iia.GameState(
            to_move=next_player,
            utility=self.calcular_utilidade(new_tabuleiro, to_be_moves, next_player, other_player(player)),
            board=(state.board[0] + 1, new_tabuleiro),
            moves=to_be_moves)

        return result

    def calcular_utilidade(self, tabuleiro, moves, to_move, player):

        res = 0
        pcs = tabuleiro.keys()
        for curr in pcs:
            if tabuleiro[curr] in ['p', 'b']:
                res += 1 if tabuleiro[curr] == self.pecas[player] else -1

        if res == 0 and len(moves) == 0:
            res = -1 if to_move == player else 1

        return res

    def utility(self, state, player):
        """Calculo da utilidade de um estado na perspectiva de um dado jogador.
        Devera ter o valor 1, para o caso de vitoria, ou −1, para o caso de derrota."""

        return state.utility

    def terminal_test(self, state):
        return self.utility(state, 'rei branco') != 0 or state.board.jogadas == 50

    def display(self, state):
        """Mostra uma representacao de um estado do jogo."""
        dic_linhas = {1: '5', 2: '4', 3: '3', 4: '2', 5: '1'}

        tab = state.board[1]  # FIXME:
        print("Tabuleiro actual:" + "\n")
        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                if y == 1:
                    print(dic_linhas[x], end='  |')
                if (x, y) in tab:
                    if tab[(x,y)] == 'b':
                        print(' b ', end='|')
                    elif tab[(x, y)] == 'p' :
                        print(' p ', end='|')
                    elif tab[(x, y)] == 'n' :
                        print(' n ', end='|')
                else:
                    print('   ', end='|')
            print('\n')
            print('------------------------\n')  # 4 traços x 6 vezes = 24 traços
        print('     A    B   C   D    E')

        if self.terminal_test(state):
            print("FIM do Jogo")
        else:
            print("Próximo jogador:{}\n".format(state.to_move))