

#modo 1
#Para descobrir se um número é par, usamos a condição numero%2 == 0, que verifica se o resto de uma divisão por 2 é zero
inteiros = [1,3,4,5,7,8,9]
pares = []
for num in inteiros:
    if num % 2 == 0:
        pares.append(num)
print("1", pares)


#modo 2 - List Comprehension relativo ficaria muito mais enxuto:

inteiros = [1,3,4,5,7,8,9]
pares = [numero for numero in inteiros if numero % 2 == 0] # x para cada x da lista inteiro se "x % 2" for zero
print("2",pares)

