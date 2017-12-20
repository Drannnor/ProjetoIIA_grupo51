import hobbes_jogo_51
import jogar

# TODO:
# main do jogo, criar os jogadores e inicializar o jogo,
#  ver peoes_main.py para exemplo -- SEM BOTAR


jogo_hobbes = hobbes_jogo_51.JogoHobbes()

j1 = jogar.Jogador(jogo_hobbes, "Ze")
j2 = jogar.Jogador(jogo_hobbes, "Estriga", f=jogar.random_player)
j3 = jogar.Jogador(jogo_hobbes, "Nisco", f=jogar.random_player)

# 3 = jogar.Jogador(jogo_hobbes, "MaisPeões", hobbes.jogador_2peoes_F1)

resultado = jogar.um_jogo(jogo_hobbes, j2, j3, 3, True)

print(resultado)

# njogos = jogar.n_pares_de_jogos(jogo_hobbes, 10, j2, j3, 5)
# print(njogos)
