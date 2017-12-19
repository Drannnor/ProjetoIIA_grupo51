import jogos_iia
import hobbes_jogo_51

# TODO:
# Jogadores alfabeta para o jogo hobbes (com funções de avaliação)
# ver peoes_jogadores para exemplo -- SEM BOTAR

# quanto mais jogadas tem, mais pontos tem, heuristica 1
def f_aval_hobbes_F1(state, jogador):
    return len(state.moves)


# TODO:
def f_aval_hobbes_F2(state, jogador):
    return


# TODO:
def f_aval_hobbes_F3(state, jogador):
    return


# TODO:
def f_aval_hobbes_F4(state, jogador):
    return

def jogador_hobbes_F1(jogo, state, nivel=5): #FIXME:
    return jogos_iia.alphabeta_cutoff_search(state, jogo, nivel, eval_fn=f_aval_hobbes_F1)
