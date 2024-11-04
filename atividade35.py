# Ler uma lista de 10 números reais e
# mostre-os na ordem inversa.

listanumeros = []

for i in range(1,11):
    numero = int(input("Digite seus números: "))
    listanumeros.append(numero)

for i in reversed(listanumeros):
    print(i)