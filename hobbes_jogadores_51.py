import math

import hobbes_jogo_51
import jogos_iia

MAXNORM = 10
MAXSIDES = 4

# TODO:
# Jogadores alfabeta para o jogo hobbes (com funções de avaliação)
# ver peoes_jogadores para exemplo -- SEM BOTAR

# quanto mais acoes tem, melhor é; heuristica 1
def f_aval_hobbes_F1(state, jogador):
    return len(state.moves)


# quanto menor a distancia entrea posicao do outro jogador e a possivel posicao do jogador atual, melhor é;
# heuristica 2
def f_aval_hobbes_F2(state, jogador):
    acts = state.moves
    if len(acts) == 0:
        return 0
    (x, y) = hobbes_jogo_51.find_player(state.board[1], 'p' if (jogador == 'b') else 'b')
    (fs,(ssx, ssy)) = acts[0]
    min = MAXNORM
    for (fs, (ssx, ssy)) in acts:
        norm = math.sqrt(pow(ssy * y, 2) + pow(ssx * x, 2))
        min = norm if norm < min else min
    return MAXNORM - min

#quantos mais espaços livres adjacentes tem, por acoes disponiveis, melhor é; heuristica 3
def f_aval_hobbes_F3(state, jogador):
    (x, y) = hobbes_jogo_51.find_player(state.board[1], 'b' if (jogador == 'b') else 'p')
    tab = state.board[1]
    sum = 4 # lados livres

    if x - 1 > 0 and (x - 1, y) in tab and tab[(x - 1, y)] == 'n':  # primeira casa à esquerda esta ocupada ou é limite
        if x - 2 > 0 and (x - 2, y) in tab and tab[(x - 2, y)] == 'n':  # a segunda casa à esquerda esta ocupada ou é limite
            sum -= 1
    if x + 1 < hobbes_jogo_51.BOARDSIZE and (x + 1, y) in tab and tab[(x + 1, y)] == 'n':  # primeira casa à direita esta ocupada ou é limite
        if x - 2 < hobbes_jogo_51.BOARDSIZE and (x + 2, y) in tab and tab[(x + 2, y)] == 'n':  #a segunda casa à direita esta ocupada ou é limite
            sum -= 1
    if y - 1 > 0 and (x, y - 1) in tab and tab[(x, y - 1)] == 'n':  # primeira casa em baixo esta ocupada ou é limite
        if y - 2 > 0 and (x, y - 2) in tab and tab[(x, y - 2)] == 'n':  #a segunda casa em baixo esta ocupada ou é limite
            sum -= 1
    if y + 1 < hobbes_jogo_51.BOARDSIZE and (x, y + 1) in tab and tab[(x, y + 1)] == 'n':  # primeira casa em cima esta ocupada ou é limite
        if y + 2 < hobbes_jogo_51.BOARDSIZE and (x, y + 2) in tab and tab[(x, y + 2)] == 'n':  #a segunda casa em cima esta ocupada ou é limite
            sum -= 1         

    return sum

def f_aval_hobbes_F4(state, jogador):
    (pl1x, pl1y) = hobbes_jogo_51.find_player(state.board[1], 'p' if (jogador == 'b') else 'b')
    (pl2x, pl2y) = hobbes_jogo_51.find_player(state.board[1], 'b' if (jogador == 'b') else 'p')
    return math.sqrt(pow(pl1x * pl2x, 2) + pow(pl1y * pl2y, 2))


def f_aval_hobbes_F5(state, jogador):
    return f_aval_hobbes_F1(state, jogador) * f_aval_hobbes_F3(state, jogador)


def f_aval_hobbes_F6(state, jogador):
    return f_aval_hobbes_F1(state, jogador) * 0.5 + f_aval_hobbes_F2(state, jogador) * 0.5


def f_aval_hobbes_F7(state, jogador):
    return f_aval_hobbes_F1(state, jogador) * 0.3 + f_aval_hobbes_F2(state, jogador) * 0.3 + \
           f_aval_hobbes_F2(state, jogador) * 0.3

def jogador_hobbes_F1(jogo, state, nivel=5):
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F1)


def jogador_hobbes_F2(jogo, state, nivel=5):
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F2)


def jogador_hobbes_F3(jogo, state, nivel=5):
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F3)


def jogador_hobbes_F4(jogo, state, nivel=5):
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F4)


def jogador_hobbes_F5(jogo, state, nivel=5):
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F5)


def jogador_hobbes_F6(jogo, state, nivel=5):
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F6)


def jogador_hobbes_F7(jogo, state, nivel=5):
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F7)
