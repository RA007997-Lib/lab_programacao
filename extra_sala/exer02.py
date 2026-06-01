num = int(input("Digite um numero"))
produto = 1
for i in range (1,num + 1, 2):
    produto *= i

print(f"O produto dos impares até {num} é: {produto}")