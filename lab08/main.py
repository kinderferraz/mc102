#! /usr/bin/env python3
# TAREFA DE LABORATORIO 08 — CAÇA PALAVRAS
# ALKINDAR RODRIGUES — 154532


# Ler valores de entrada
# nenhum parametro,
def entrada():
    '''Processar valores de entrada. As palavras a serem procuradas são
    adicionadas a um conjunto vazio para consulta posterior.
    '''
    quadroEntrada = []
    palavras = set()
    notDone = True
    while notDone:
        numero = input()
        if numero.isdigit():
            numero = int(numero)
            notDone = False
        else:
            quadroEntrada.append(numero.strip().split())
    size = len(quadroEntrada[0]), len(quadroEntrada)
    for i in range(numero):
        palavras.add(input())
    return size, quadroEntrada, palavras


# Geradores:
def genCoordenadas():
    '''produz as coordenadas da matriz que serão fornecidas para as
    funções de busca'''
    for i in range(largura):
        for j in range(altura):
            yield (j, i)


def search(pal):
    '''Função de busca da palavra: transformamos ela em uma lista com os
    caracteres, para que possamos comparar cada caractere com aqueles
    encontrados na matriz fornecida. São executadas 4 subfunções para
    procurar as palavras nas linhas, colunas, diagonais e diagonais
    secundárias. A matriz auxiliar, criada fora da função, recebe os
    caracteres nas devidas posições conforme as subfunções são
    executadas. Ao fim, esta é retornada.

    '''

    def addNextToCol(xPal, yPal, i, r=False):
        '''Função auxiliar para searchCol(): ao encontrar um caractere na
        posição correta da matriz principal, confere se o caractere
        acima e abaixo estao em posição tambem. Caso estejam, ao
        encontrar o ultimo caractere, todos os demais são posicionados
        na matriz auxiliar.

        '''
        yPal += 1
        if r:
            i -= 1
            caractereFinal = (i == 0)
        else:
            i += 1
            caractereFinal = (i == lenPal - 1)
        caracteresBatem = (quadroEntrada[yPal][xPal] == lstStr[i])

        if caractereFinal and caracteresBatem:
            quadroAux[yPal][xPal] = lstStr[i]
            return True

        elif caracteresBatem:
            proximoOk = addNextToCol(xPal, yPal, i, r)
            if proximoOk:
                quadroAux[yPal][xPal] = lstStr[i]
                return True
        else:
            return False
        # # # # Fim da função addNextToCol

    def addNextToDiag(xPal, yPal, i, r=False):
        '''Função auxiliar de searchDiags(): quando esta encontra um
        caracetre em posição, procura-se pelos proximos caracteres nas
        posições seguintes. Caso o último seja encontrado, este e os
        demais serão devidamente posicionados na matriz auxiliar'''
        yPal += 1
        xPal += 1
        if r:
            i -= 1
            caractereFinal = (i == 0)
        else:
            i += 1
            caractereFinal = (i == lenPal - 1)
        caracteresBatem = (quadroEntrada[yPal][xPal] == lstStr[i])
        if caractereFinal and caracteresBatem:
            quadroAux[yPal][xPal] = lstStr[i]
            return True
        elif quadroEntrada[yPal][xPal] == lstStr[i]:
            proximoOk = addNextToDiag(xPal, yPal, i, r)
            if proximoOk:
                quadroAux[yPal][xPal] = lstStr[i]
                return True

    def addNextToDiagSec(xPal, yPal, i, r=False):
        '''Função auxiliar de serachDiacSec(): como nas duas anteriores,
        é executada quando se encontra um caracetre já posicionado, e
        verifica os caracteres das posições adjacente. Quando o último
        for encontrado, todos serão posicionados.'''

        i += 1

        if r:
            yPal -= 1
            xPal += 1
            if yPal < 0 or xPal >= largura or 0 > i > lenPal - 1:
                return False
        else:
            yPal += 1
            xPal -= 1
            if xPal < 0 or yPal >= altura or i > lenPal - 1:
                return False

        caracteresBatem = (quadroEntrada[yPal][xPal] == lstStr[i])
        caractereFinal = (i == lenPal - 1)

        if caractereFinal and caracteresBatem:
            quadroAux[yPal][xPal] = lstStr[i]
            return True
        elif quadroEntrada[yPal][xPal] == lstStr[i]:
            proximoOk = addNextToDiagSec(xPal, yPal, i, r)
            if proximoOk:
                quadroAux[yPal][xPal] = lstStr[i]
                return True
        else:
            return False

    # LINHAS: procurar linhas: i são coordensdas de linhas. somando a
    # len da palavra à ao possivel ponto inicial da palavra (xPal)
    def searchLinhas(lstStr):
        '''Subfunção: ao encontrar uma slice na linha que
        corresponda a string desejada, posiciona esta string na
        linha correta da matriz auxiliar. Esta funçao não exige
        função auxiliar'''
        linhas = genCoordenadas()
        for i in linhas:
            yPal, xPal = i

            condicao = (xPal+lenPal <= largura)
            palavraAchada = (quadroEntrada[yPal][xPal:(xPal+lenPal)] == lstStr)
            palavraAchadaRev = (
                quadroEntrada[yPal][xPal:(xPal+lenPal)] == lstStr[::-1])

            if condicao:
                if palavraAchada:
                    quadroAux[yPal][xPal:(xPal+lenPal)] = lstStr
                    return

                elif palavraAchadaRev:
                    quadroAux[yPal][xPal:(xPal+lenPal)] = lstStr[::-1]
                    return

    def searchCols(lstStr):
        '''Subfunção de busca em colunas: ao encontrar um caractere desejado
        na matriz de entrada, executa a função auxiliar para averiguar
        os caracteres posicionados acima de abaixo dele.  Ao fim,
        posicona este caracetre na matriz auxiliar.

        '''

        colunas = genCoordenadas()
        for yPal, xPal in colunas:
            if yPal+lenPal <= altura:
                i = 0
                caracteresBatem = (quadroEntrada[yPal][xPal] == lstStr[i])
                if caracteresBatem:
                    tudoOk = addNextToCol(xPal, yPal, i)
                    if tudoOk:
                        quadroAux[yPal][xPal] = lstStr[i]
                        return

                i = (lenPal - 1)
                if quadroEntrada[yPal][xPal] == lstStr[i]:
                    tudoOk = addNextToCol(xPal, yPal, i, True)
                    if tudoOk:
                        quadroAux[yPal][xPal] = lstStr[i]
                        return

    def searchDiags(lstStr):
        '''Subfunção para a procura na diagonais
        Esq-Alto -> Dir-Baixoself.'''

        diagonais = genCoordenadas()

        for yPal, xPal in diagonais:
            if yPal + lenPal <= altura and xPal + lenPal <= largura:
                i = 0
                if (quadroEntrada[yPal][xPal] == lstStr[i]):
                    tudoOk = addNextToDiag(xPal, yPal, i)
                    if tudoOk:
                        quadroAux[yPal][xPal] = lstStr[i]
                        return

            if yPal + lenPal <= altura and xPal + lenPal <= largura:
                i = lenPal - 1
                if (quadroEntrada[yPal][xPal] == lstStr[i]):
                    tudoOkRev = addNextToDiag(xPal, yPal, i, True)
                    if tudoOkRev:
                        quadroAux[yPal][xPal] = lstStr[i]
                        return

    def searchDiagsSec(lstStr):
        '''Subfunção para a procura na diagonais Esq-Baixo -> Dir-Alto.'''
        diagonais = genCoordenadas()
        for yPal, xPal in diagonais:
            tudoOk = False
            i = 0
            if (quadroEntrada[yPal][xPal] == lstStr[i]):
                tudoOk = addNextToDiagSec(xPal, yPal, i)
                if tudoOk:
                    quadroAux[yPal][xPal] = lstStr[i]
                    return

                else:
                    tudoOk = addNextToDiagSec(xPal, yPal, i, True)
                    if tudoOk:
                        quadroAux[yPal][xPal] = lstStr[i]
                        return

    # string a ser procurada
    lenPal = len(pal)
    lstStr = [c for c in pal]

    searchLinhas(lstStr)
    searchCols(lstStr)
    searchDiags(lstStr)
    searchDiagsSec(lstStr)

    return quadroAux


# produce final list to print
def printFinal(quadro):
    '''Função para formatar e imprimir o quadro com as palavras desejadas:
    para cada elemento da matriz auxiliar, imprime o caractere, quando
    presente, ou um ponto, se a posição estiver marcada como False. Ao
    fim o método .strip() remove o espaço que esta ao fim, loga antes
    da impressão

    '''
    for linha in quadro:
        strAux = ''
        for c in linha:
            if not c:
                strAux += ". "
            else:
                strAux += c + " "
        print(strAux.strip())


size, quadroEntrada, palavras = entrada()
largura, altura = size
quadroAux = quadro = [[False for i in range(largura)] for j in range(altura)]

for pal in palavras:
    quadroFinal = search(pal)
printFinal(quadroFinal)
