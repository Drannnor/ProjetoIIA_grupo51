import jogos_iia.py

class JogoPeoes(jogos_iia.Game) :

    def __init__(game, state, nivel = 0):# TODO:
        """O construtor."""

        return 

    def actions(self, state):# TODO:
        """Obtencao das jogadas possiveis, dado um estado do jogo."""
        
        return

    def result(self,state, move):# TODO:
        """Obtencao do estado que se obtem ao executar uma dada jogada num dado estado."""

        return

    def utility(self, state, player):# TODO:
        """Calculo da utilidade de um estado na perspectiva de um dado jogador.
        Devera ter o valor 1, para o caso de vitoria, ou −1, para o caso de derrota."""

        return

    def terminal_test(self, state):# TODO:
        """metodo booleano que verifica se um estado dado eh final."""

        return


    def display():# TODO:
        """Mostra uma representacao de um estado do jogo."""

        return

