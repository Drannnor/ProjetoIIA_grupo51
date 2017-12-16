# -*- coding: utf-8 -*-
## Main - Jogo dos Peões

#Módulos genéricos
import jogar     # utlidades para realizar jogos

# Módulos específicos do jogo dos peões
import peoes_jogo
import peoes_jogadores

jogo_peoes = peoes_jogo.JogoPeoes()

j1 = jogar.Jogador(jogo_peoes,"Ze")
j2 = jogar.Jogador(jogo_peoes,"Ao Calhas",f = jogar.random_player)


j3 = jogar.Jogador(jogo_peoes,"MaisPeões",peoes_jogadores.jogador_2peoes_F1)

resultado = jogar.um_jogo(jogo_peoes,j2,j3,3,True)

print(resultado)

njogos = jogar.n_pares_de_jogos(jogo_peoes,10,j2,j3,5)
print(njogos)
