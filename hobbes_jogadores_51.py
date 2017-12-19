from math import sqrt
import jogos_iia
import hobbes_jogo_51

MAXNORM = 10
MAXSIDES = 4

# TODO:
# Jogadores alfabeta para o jogo hobbes (com funções de avaliação)
# ver peoes_jogadores para exemplo -- SEM BOTAR

# quanto mais acoes tem, melhor é; heuristica 1
def f_aval_hobbes_F1(state, jogador):
    return len(state.moves)

# quanto menor a distanciaentrea posicao do outro jogador e a possivel posicao do jogador atual, melhor é; heuristica 2
def f_aval_hobbes_F2(state, jogador):
    acts = state.moves
    (x,y) = find_player(state, 'p' if (jogador == 'b') else 'b')
    (fs,(ssx, ssy)) = acts[0]
    min = MAXNORM
    for (fs,(ssx,ssy) in acts:
        norm = math.sqrt(pow(ssy * y,2), pow(ssx * x,2))
        min = norm if norm < min else min
    return MAXNORM - min

#quantos mais espaços livres adjacentes tem, por acoes disponiveis, melhor é; heuristica 3
def f_aval_hobbes_F3(state, jogador):
    (x,y) = find_player(state, 'b' if (jogador == 'b') else 'p')
    tab = state.board.tabuleiro
    sum = 0 # lados livres
    for i in range 4:
        if x-1 > 0 and tab[(x,y)] == none
            sum += 1
        if x+1 <= BOARDSIZE and tab[(x+1,y)] == none
            sum += 1
        if y-1 > 0 and tab[(x,y-1)] == none
            sum += 1
        if y+1 <=  BOARDSIZE and tab[(x,y)] == none
            sum += 1
         
    h1 = f_aval_hobbes_F1(state, jogador)

    return h1/(MAXSIDES - sum + 1) // menor divisor, melhor


# TODO:
def f_aval_hobbes_F4(state, jogador):
    return

def jogador_hobbes_F1(jogo, state, nivel=5): #FIXME:
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F1)
