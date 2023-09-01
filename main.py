with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

listas = []

for linha in linhas:
    valores = linha.strip().split(', ')
    valores = [int(valor) if valor.isdigit() else valor for valor in valores]
    listas.append(valores)

for lista in listas:
    print(lista)

linha1 = int(input("Digite qual a linha do primeiro conjunto: "))
linha2 = int(input("Digite qual a linha do segundo conjunto: "))

conjunto1 = set(listas[linha1])
conjunto2 = set(listas[linha2])

operacao = int(input("Digite qual a operação\n1-União\n2-Intersecção\n3-Diferença\n4-Cartesiano: "))

if operacao == 1:
  resultado_uniao = conjunto1.union(conjunto2)
  print(resultado_uniao)
elif operacao == 2:
  resultado_intersecao = conjunto1.intersection(conjunto2)
  print(resultado_intersecao)
elif operacao == 3:
  resultado_diferenca = conjunto1.difference(conjunto2)
  print(resultado_diferenca)
elif operacao == 4:
  cartesiano = [(a, b) for a in conjunto1 for b in conjunto2]
  print(cartesiano)
else:
  print("Operação inválida")
