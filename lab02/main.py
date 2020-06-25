# MC102 O -- Alkindar Rodrigues
# lab  02 -- Calculadora simples
# para ler o primeiro operando
op1 = input()
if op1.isdigit():
    op1 = int(op1)
else:
    op1 = float(op1)

# para ler a operação a ser realizada
e = input()

# para ler o segundo operando
op2 = input()
if op2.isdigit():
    op2 = int(op2)
else:
    op2 = float(op2)

# variavel de controle para casos de divisão por zero
erro = False
# para realizar o cálculo
if e == "+":
    calc = op1 + op2
elif e == "-":
    calc = op1 - op2
elif e == "*":
    calc = op1 * op2
elif e == "/":
    if op2 != 0:
        calc = op1 / op2
    else:
        erro = True
elif e == "//":
    if op2 != 0:
        calc = op1 // op2
    else:
        erro = True
elif e == "%":
    if op2 != 0:
        calc = op1 % op2
    else:
        erro = True
elif e == "**":
    calc = op1**op2

    # verifica o tipo do resultado e imprime de acordo
if erro is False:
    if type(calc) == int:
        print(calc)
    else:
        print(format(calc, ".2f"))
else:
    print("Erro.")
