h = input('Informe sua altura:  ')
s = input('Informe o sexo 1 para mulheres ou 2 para homens:  ')

p_i_h = 72.7 * float(h) - 58
p_i_m = 62.1 * float(h) - 44.7

if int(s) == 1:
    print(f'Seu peso ideal é {p_i_m}Kg')
elif int(s) == 2:
    print(f'Seu peso ideal é {p_i_h}Kg')
else:
    print(f'Sexo informado não correspondente')
