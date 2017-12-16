# -*- coding: utf-8 -*-

## Plataforma Alfa-Beta

## Implementação do jogo dos peões

import jogos_iia
from copy import deepcopy

class JogoPeoes(jogos_iia.Game) :
    """Representação para o jogo:
    """

    @staticmethod
    def outro_jogador(j) :
        return 'brancas' if j == 'pretas' else 'pretas'
    
    def __init__(self) :
        self.jogadores = ('brancas','pretas')
        self.sentido = {'brancas':-1,'pretas':1}        
        
        self.linhas = 3 # número de linhas
        self.cols = 3   # número de colunas
        self.objectivo = {'brancas':1,'pretas':self.linhas}
        tabuleiro_inicial = {'brancas':[(3,1),(3,2)],'pretas':[(1,2),(1,3)]}
        movs_possiveis = self.movimentos_possiveis(tabuleiro_inicial,self.jogadores[0])
        self.initial = jogos_iia.GameState(
            to_move = self.jogadores[0],
            utility = 0,
            board = tabuleiro_inicial,
            moves = movs_possiveis)
    
    def movimentos_possiveis(self,tabuleiro,jogador) :
        """Três tipos de movimentos:
        - avança - ('avança',(x,y)) - avança a peça (x,y)
        - come-esq - ('come-esq',(x,y)) - peça (x,y) come à esquerda
        - come-dir - ('come-dir',(x,y)) - peça (x,y) come à direita
        """
        def frente_livre(tab,peca,jog) :
            pecas_todas = tab['brancas']+tabuleiro['pretas']
            x = peca[0]+self.sentido[jog]
            y = peca[1]
            return (1 <= x <= self.linhas) and (x,y) not in pecas_todas
        def pode_comer_esq(tab,peca,jog) :
            x = peca[0]+self.sentido[jog]
            y = peca[1]+self.sentido[jog]
            return (x,y) in tab[JogoPeoes.outro_jogador(jog)]
        def pode_comer_dir(tab,peca,jog) :
            x = peca[0]+self.sentido[jog]
            y = peca[1]-self.sentido[jog]
            return (x,y) in tab[JogoPeoes.outro_jogador(jog)]
        
        pecas = tabuleiro[jogador]
        movs = list()
        for p in pecas :
            if frente_livre(tabuleiro,p,jogador) :
                movs.append(("avança",p))
            if pode_comer_esq(tabuleiro,p,jogador) :
                movs.append(("come-esq",p))
            if pode_comer_dir(tabuleiro,p,jogador) :
                movs.append(("come-dir",p))
        return movs
        
        
    def actions(self,state) :
        return state.moves
    
    def result(self,state,move) :
        """
        Requires: 'move' é uma jogada válida no estado dado ('state')
        """
        accao,peca = move
        jogador = state.to_move
        adversario = JogoPeoes.outro_jogador(jogador)
        tabuleiro = deepcopy(state.board)
        tabuleiro[jogador].remove(peca)
        if accao == 'avança' :
            x = peca[0]+self.sentido[jogador]
            y = peca[1]
            tabuleiro[jogador].append((x,y))
        elif accao == 'come-esq' :
            x = peca[0]+self.sentido[jogador]
            y = peca[1]+self.sentido[jogador]
            tabuleiro[jogador].append((x,y))
            tabuleiro[adversario].remove((x,y))
        else : # come-dir
            x = peca[0]+self.sentido[jogador]
            y = peca[1]-self.sentido[jogador]
            tabuleiro[jogador].append((x,y))
            tabuleiro[adversario].remove((x,y))
        estado = jogos_iia.GameState(to_move = JogoPeoes.outro_jogador(jogador),
                           board = tabuleiro,
                           moves = self.movimentos_possiveis(tabuleiro,JogoPeoes.outro_jogador(jogador)),
                           utility = self.calcular_utilidade(tabuleiro,jogador))
        return estado

    
    def calcular_utilidade(self,tabuleiro,jogador) :
        def objectivo(linha,jogador) :
            return linha in [x for (x,_) in tabuleiro[jogador]]
        
        utilidade = 0
        adversario = JogoPeoes.outro_jogador(jogador)
        if objectivo(self.objectivo[jogador],jogador) \
           or tabuleiro[adversario] == []:
            utilidade = 1
        elif objectivo(self.objectivo[adversario],adversario) \
             or tabuleiro[jogador] == []:
            utilidade = -1
        
        return utilidade
    
    def utility(self, state, player):
        return self.calcular_utilidade(state.board,player)
    
    def terminal_test(self,state) :
        return state.moves == [] or any([self.utility(state,x) != 0 for x in self.jogadores])

    def display(self, state):
        board = state.board
        print("Tabuleiro actual:")
        for x in range(1, self.linhas + 1):
            for y in range(1, self.cols + 1):
                if (x,y) in board['brancas'] :
                    print('O', end=' ')
                elif (x,y) in board['pretas'] :
                    print('*', end=' ')
                else :
                    print('.',end=' ')
                    
            print()
        if self.terminal_test(state) :
            print("FIM do Jogo")
        else :
            print("Próximo jogador:{}\n".format(state.to_move))
    

