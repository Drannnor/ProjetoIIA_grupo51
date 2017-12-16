import jogos_iia
import hobbes_jogo

# TODO: 
# Jogadores alfabeta para o jogo hobbes (com funções de avaliação)
# ver peoes_jogadores para exemplo -- SEM BOTAR


def f_aval_hobbes_F1(estado,jogador) :
     #TODO:
    return 

def jogador_hobbes_F1(jogo,estado, nivel = 5) : #FIXME:
    return jogos_iia.alphabeta_cutoff_search(estado,jogo,nivel,eval_fn=f_aval_hobbes_F1)