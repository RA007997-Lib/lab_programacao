vetor =[ 10,20,30,40]
soma = 0

for valor in vetor:
    soma += valor
media=soma/len(vetor)
mais_proximo=min(vetor,key=lambda x:abs(x - media))

print(f"Medis{media}")
print(f"Valor mais proximo da média{mais_proximo}")