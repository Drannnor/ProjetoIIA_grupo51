import hobbes_jogadores_51
import hobbes_jogo_51
import jogar

# TODO:
# main do jogo, criar os jogadores e inicializar o jogo,
#  ver peoes_main.py para exemplo -- SEM BOTAR


jogo_hobbes = hobbes_jogo_51.JogoHobbes()

j1 = jogar.Jogador(jogo_hobbes, "Ze1", f=hobbes_jogadores_51.jogador_hobbes_F1)
j2 = jogar.Jogador(jogo_hobbes, "Ze2", f=hobbes_jogadores_51.jogador_hobbes_F2)
j3 = jogar.Jogador(jogo_hobbes, "Ze3", f=hobbes_jogadores_51.jogador_hobbes_F3)
j4 = jogar.Jogador(jogo_hobbes, "Ze4", f=hobbes_jogadores_51.jogador_hobbes_F4)
j5 = jogar.Jogador(jogo_hobbes, "Ze5", f=hobbes_jogadores_51.jogador_hobbes_F5)
j5 = jogar.Jogador(jogo_hobbes, "Estriga", f=jogar.random_player)
j6 = jogar.Jogador(jogo_hobbes, "Nisco", f=jogar.random_player)

# 3 = jogar.Jogador(jogo_hobbes, "MaisPeões", hobbes.jogador_2peoes_F1)

resultado = jogar.um_jogo(jogo_hobbes, j2, j5, 3, True)

print(resultado)

# njogos = jogar.n_pares_de_jogos(jogo_hobbes, 10, j2, j3, 5)
# print(njogos)
