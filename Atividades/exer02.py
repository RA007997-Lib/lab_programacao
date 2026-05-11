vetor = []

for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

x = int(input("Digite o valor a procurar: "))

if x in vetor:
    print(vetor.index(x))
else:
    print(-1)