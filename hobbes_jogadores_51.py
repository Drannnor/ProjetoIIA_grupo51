import jogos_iia
import hobbes_jogo_51

# TODO: 
# Jogadores alfabeta para o jogo hobbes (com funções de avaliação)
# ver peoes_jogadores para exemplo -- SEM BOTAR

# quanto mais jogadas tem, mais pontos tem, heuristica 1
def f_aval_hobbes_F1(estado, jogador):
    return len(hobbes_jogo_51.actions(estado)) #FIXME: hobbes_jogo_51 eh o ficheiro nao a classe


# TODO:
def f_aval_hobbes_F2(estado,jogador):
    return 


# TODO:
def f_aval_hobbes_F3(estado,jogador):
    return 


# TODO:
def f_aval_hobbes_F4(estado,jogador):
    return 

def jogador_hobbes_F1(jogo,estado, nivel = 5) : #FIXME:
    return jogos_iia.alphabeta_cutoff_search(estado,jogo,nivel,eval_fn=f_aval_hobbes_F1)