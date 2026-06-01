numeros = []
#ler notas
for i in range(6):
    numero = int(input("Digite o {i+1}. numero: "))
    numeros.append(numero)

x = int(input("\nQual o numero deseja pesquisar?"))
ocorrencias = numeros.count(x)
print("-"*30)
if ocorrencias >0:
    print(f"O numero {x} aparece {ocorrencias} vez(es) na lista")
    print(f"Sua primeira aparição foi no índice: {numeros.index(x)}")
else:
    print(f"o numero {x} não foi encontrado na lista.")