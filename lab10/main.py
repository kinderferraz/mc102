# MC102 - UNICAMP
# Akindar Ferraz Rodrigues
# 154532


# Funções preliminares, para receber os valores de entrada e formatar a saida
# em ASCII Art e conferir a ordenação de uma lista
def entrada():
    tipo = input()
    lista = [int(numero) for numero in input().split()]
    return tipo, lista


def saida(quadros):
    def moldura():
        """Prepara a moldura que será colocada acima e abaixo de cada quadro"""
        print('.' * (largura + 2))

    def prep(quadro):
        """Preparar o quadro de saida com espaços em branco quando necessário
        """
        for i in range(largura):
            espacos = altura - quadro[i]
            # print(esp)
            for j in range(espacos):
                qdrSaida[j][i] = " "

        moldura()
        for j in range(altura):
            strAux = ""
            for i in range(largura):
                strAux += qdrSaida[j][i]
            print('.' + strAux + '.')
        moldura()

    altura = max(quadros[0])
    largura = len(quadros[0])
    for quadro in quadros:
        qdrSaida = [["|" for i in range(largura)] for j in range(altura)]
        prep(quadro)


def checkOrdered(ultimoPasso):
    """Confere se a lista já está ordenada, procurando pela primeira
inversão que possa estar presente"""
    nElem = len(ultimoPasso) - 1
    ordenou = True
    for i in range(nElem):
        elem1 = ultimoPasso[i]
        elem2 = ultimoPasso[i + 1]
        if elem1 > elem2:
            ordenou = False
            break
    return ordenou


def bubbleSort(lista):
    """Ordena a lista pelo método bubble sort. A cada passo uma copia da
lista é armazenada no vetor 2d 'passos' e confere-se se a lista esta
ordenada. Se não estiver, mais um passo é realizado. Quando o processo
for finalizado, o vetor passos é impresso"""
    passos = [lista.copy()]
    nPassos = len(lista) - 1
    for passo in range(nPassos):
        for elemento in range(nPassos):
            if lista[elemento] > lista[elemento + 1]:
                lista[elemento], lista[elemento +
                                       1] = lista[elemento +
                                                  1], lista[elemento]
        passos += [lista.copy()]
        listaOrdenada = checkOrdered(lista)
        if listaOrdenada:
            break
    # print(passos)
    saida(passos)


def selectionSort(lista):
    """Como na função acima, a lista é copiada para outra, bidimensional,
e conferida. Se estiver ordenada, faz-se a impressão dos passos"""
    passos = [lista.copy()]
    item1 = 0
    itens = len(lista)
    while item1 < itens:
        item2 = item1
        for proximo in range(item1 + 1, itens):
            if lista[item2] > lista[proximo]:
                item2 = proximo
        lista[item1], lista[item2] = lista[item2], lista[item1]
        passos += [lista.copy()]
        item1 += 1
        listaOrdenada = checkOrdered(lista)
        if listaOrdenada:
            break
    saida(passos)


def insertionSort(lista):
    passos = [lista.copy()]
    nPassos = len(lista)
    for indice in range(1, nPassos):
        valor = lista[indice]
        onde = indice
        while onde > 0 and lista[onde - 1] > valor:
            lista[onde] = lista[onde - 1]
            onde -= 1
        lista[onde] = valor
        passos += [lista.copy()]
        ordenada = checkOrdered(lista)
        if ordenada:
            break
    saida(passos)


tipo, teste = entrada()  # Recebe valores de entrada
jaOrdenada = checkOrdered(
    teste)  # Confere se a lista recebida já está ordenada
# se estiver, já a imprimimos
if jaOrdenada:
    saida([teste])
    quit()
# do contrário, usamos o método solicitado para ordená-la
if tipo == "bubble":
    bubbleSort(teste)
elif tipo == "selection":
    selectionSort(teste)
elif tipo == "insertion":
    insertionSort(teste)
