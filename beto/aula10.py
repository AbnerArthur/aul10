'import math'
'''
Lambda function

sintaxe: lambda argumentos: expressão 


dobro = lambda  x: x * 2

print('exmplo 1 - dobro de 5', dobro(5))

soma = lambda x, y: x + y 

print('exmplo 2 - Soma de 3 e 4', soma(3, 4))'''

'c = lambda cateto1, cateto2: (cateto1 ** 2 + cateto2 ** 2) ** 0.5'
'print("Valor da hipotenusa:", c(3, 4))'

'hipo = lambda a, b: math.sqrt(a ** 2 + b ** 2) '

# filter, map

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print('Exemplo 3 - Numeros pares:', pares )
