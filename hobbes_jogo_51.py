import jogos_iia.py

table_size = 5

class JogoPeoes(jogos_iia.Game) :

    def __init__(game, state, nivel = 0):
        """O construtor."""
        # TODO:

        return 

    def actions(self, state):
        """Obtencao das jogadas possiveis, dado um estado do jogo."""
        # TODO:


        
        return

    def result(self,state, move):
        """Obtencao do estado que se obtem ao executar uma dada jogada num dado estado."""
        # TODO:
        return

    def utility(self, state, player):
        """Calculo da utilidade de um estado na perspectiva de um dado jogador.
        Devera ter o valor 1, para o caso de vitoria, ou −1, para o caso de derrota."""
        # TODO:
        return

    def terminal_test(self, state):
        """metodo booleano que verifica se um estado dado eh final."""
        # TODO:
        return


    def display(self, state):
        """Mostra uma representacao de um estado do jogo."""
        # TODO:
        return

    def first_step(self, tabuleiro): #TODO:

        for i in range (1,table_size):
            for j in range (1, table_size):

        return first_step_rec(tabuleiro,stepped)


    def first_step_rec(self, tabuleiro, stepped): # TODO:




