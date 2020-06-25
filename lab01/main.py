# para definir se o objeto 1 (representado pela variavel obj_1) é um
# int ou float, com base no input da letra i ou f %%
type1 = input()
if type1 == "i":
    obj1 = int(input())
else:
    obj1 = float(input())

# o mesmo procedimento para o objeto 2
type2 = input()
if type2 == "i":
    obj2 = int(input())
else:
    obj2 = float(input())

# soma do objetos 1 com o objeto 2
# %%

soma = obj1 + obj2

# para imprimir o resultado no caso da soma de dois inteiros

if type1 == "i" and type2 == "i":
    print(soma)

# para imprimir a soma entre dois floats
else:
    print(format(soma, ".2f"))
