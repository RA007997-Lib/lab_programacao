vetor = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

diferentes = len(set(vetor))

print("Quantidade de valores diferentes:", diferentes)