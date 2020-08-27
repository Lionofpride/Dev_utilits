num1 = input('Informe o 1º número inteiro  ')
num2 = input('Informe o 2º número inteiro  ')
num3 = input('Informe um número real  ')

op1 = int(num1) * 2 + int(num2) / 2
op2 = int(num1) * 3 + float(num3)
op3 = float(num3) ** 3

print(f'Produdo do dobro do 1º com metade do 2º é {op1}')
print(f'A soma do triplo do 1º com o 3º é {op2}')
print(f'O 3º elevado ao cubo é {op3}')
