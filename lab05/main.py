# Tarefa de laboratorio de MC102 - LESMAS
# Alkindar Rodrigues
# 154532

# ler o numero de lesmas e iniciar a variavel de controle
numLesmas = int(input())
lesmaMaisRapida = 0

# caso haja mais de 100 lesmas, imprimir mensagem de erro e sair do programa.
if numLesmas > 100:
    print("Valor inválido na linha 1.")
    quit()

# ler o valor de cada lesma e associar o mair valor à variavel
# "lesmaMaisRapida" se sair do parametro (50), imprimir mensagem de erro
# e sair.
for i in range(2, numLesmas + 2):
    lesma_i = int(input())
    if lesma_i > lesmaMaisRapida:
        lesmaMaisRapida = lesma_i
    if lesma_i > 50:
        print("Valor inválido na linha " + str(i) + ".")
        quit()

# avaliar o nivel da lesma mais rapida e imprimi-lo
if lesmaMaisRapida < 10:
    nivelLesmas = 1
elif lesmaMaisRapida < 20:
    nivelLesmas = 2
else:
    nivelLesmas = 3
print(nivelLesmas)
