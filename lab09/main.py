"""Tarefa de laborátorio 09
Alkindar Rodrigues
154531
"""


def get_vizinhos(cell_at):
    '''Gerador de tuplas correspondentes as células vizinhas de uma
       célula dada.'''
    cell_y, cell_x = cell_at
    for y_pos in range(cell_y - 1, cell_y + 2):
        for x_pos in range(cell_x - 1, cell_x + 2):
            if (y_pos, x_pos) != cell_at:
                yield (y_pos, x_pos)


class Jogo():
    '''Classe para execução do Jogo da Vida'''

    def __init__(self, tabuleiro, game_rounds):
        '''Função para preparar atributos necessários ao jogo, como
           tabuleiro inicial e numero de game_rounds. Tambem são iniciados o
           tabuleiro final, de 3 dimensões, sendo a primeira delas o quadro
           dado, a altura e largura de um determinado tabuleiro.'''

        self.tab_entrada = tabuleiro.copy()
        self.tab_final = [self.tab_entrada.copy()]
        self.game_rounds = game_rounds
        self.largura = len(tabuleiro[0])
        self.altura = len(tabuleiro)

    def get_cells(self, game_round):
        '''Prepara um dicionário com a posição e o estado de cada célula no
           tabuleiro, caso se trate de uma celula da moldura, seu
           valor será False, do contrário, uma string indicando
           morte ou vida'''

        cells = {}
        for y_pos in range(self.altura):
            for x_pos in range(self.largura):
                elmt = self.tab_final[game_round][y_pos][x_pos]
                if elmt in '-+|':
                    cells[(y_pos, x_pos)] = False
                elif elmt == '@':
                    cells[(y_pos, x_pos)] = "viva"
                else:
                    cells[(y_pos, x_pos)] = "morta"
        return cells

    def tab_aux(self):
        '''Função para preprar um novo tabuleiro, que será entregue a função
           new_rounds(). A moldura já será colocada, e os valores das demais
           células será inicicado com None'''

        tab_aux = [[None for x in range(self.largura)]
                   for y in range(self.altura)]
        cells = self.get_cells(0)
        for pos, state in cells.items():
            if not state:
                y_pos, x_pos = pos
                tab_aux[y_pos][x_pos] = self.tab_entrada[y_pos][x_pos]
        return tab_aux

    def count_vizinhos_vivos(self, cell_at, state, game_round_anterior):
        """Função para contar as células vivas vizinhas a uma celula
           dada que estão vivas. Só será executada se o estado desta
           célula for verdadeiro, no caso, uma string não
           vazia. O parametro game_round_anterior recebe um inteiro da
           funçnao new_rounds() que corresponde ao valor de último
           game_round produzido, isto é, para o primeiro game_round é
           passado o valor 0, que corresponde ao primeiro quadro
           do tab_final."""

        if state:
            viz_vivos = 0
            for viz in get_vizinhos(cell_at):
                y_viz, x_viz = viz
                if self.tab_final[game_round_anterior][y_viz][x_viz] == '@':
                    viz_vivos += 1
            return viz_vivos
        return 0

    def new_rounds(self, game_rounds):
        '''Função para produzir um game_round e adicioná-lo ao tabuleiro
           final.  Para cada célula presente no dicionário, produzido
           a partir do game_round anterior, conta-se o número de
           vizinhos vivos e posiciona novas células, de acordo com as
           regras estabelecidas, no próximo tabuleiro. Por fim, este é
           adicionado ao tab_final.'''

        for game_round in range(game_rounds):
            cells = self.get_cells(game_round)
            next_tab = self.tab_aux()
            for position, state in cells.items():
                viz = self.count_vizinhos_vivos(position, state, game_round)
                y_pos, x_pos = position
                if state == "viva" and 2 <= viz <= 3:
                    next_tab[y_pos][x_pos] = "@"
                elif state == "morta" and viz == 3:
                    next_tab[y_pos][x_pos] = "@"
                elif not state:
                    pass
                else:
                    next_tab[y_pos][x_pos] = " "
            self.tab_final.append(next_tab)

    def saida(self):
        '''Função para processar o tab_final e imprimí-lo.'''
        self.new_rounds(self.game_rounds)
        for j in range(self.altura):
            str_final = ""
            for i in range(self.game_rounds + 1):
                str_aux = ""
                for k in range(self.largura):
                    str_aux += self.tab_final[i][j][k]
                str_final += str_aux + " "
            print(str_final.strip())


def main():
    '''A função principal, que roda o jogo.'''
    quadro = []
    while True:
        linha = input()
        if not linha.isdigit():
            lista = []
            for char in linha:
                lista.append(char)
            quadro.append(lista)
        else:
            game_rounds = int(linha)
            break

    jogo = Jogo(quadro, game_rounds)
    jogo.saida()


if __name__ == "__main__":
    main()
