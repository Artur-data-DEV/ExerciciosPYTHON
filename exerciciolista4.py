# -*- coding: utf-8 -*-
"""ExercicioLista4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iPzo1CmApD3ahcws4lKREqv30MsrSz5P
"""

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4

nlados = int (input( "Quantos lados têm o poligono regular escolhido? Digite: ")) #recebe o numero de lados
medidaLado = float (input("Digite a medida de um destes lados: ")) #recebe a medida de um destes lados

if nlados == 3: #função que calcula a área do poligono, caso o numero de lados for 3
  area = ((medidaLado ** 2) * (3 ** (1/2))) /4 #formula de calculo da area de um triangulo 
  print("Este TRIANGULO tem uma área de: %.2f cm²" %area) #printa resultado do programa

elif nlados == 4: #função que calcula a área do poligono, caso o numero de lados for 4
  area = medidaLado ** 2 #formula de calculo da area de um triangulo 
  print("Este QUADRADO tem uma área de: %.2f cm²" %area) #printa resultado do programa

elif nlados == 5: #função que printa pentagono caso digitem o valor 5
  print("Isso é um PENTÁGONO !!!!!")

elif nlados != 5 or nlados != 4 or nlados != 3:
  print('Os valores informados não correspondem a um poligono regular, escreva o numero de lados corretamente e tente novamente mais tarde.')

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4

nlados = int (input( "Quantos lados têm o poligono regular escolhido? Digite: ")) #recebe o numero de lados
medidaLado = float (input("Digite a medida de um destes lados: ")) #recebe a medida de um destes lados

if nlados < 3: #função que imprime mensagem caso o numero de lados seja menor que 3
  print("Isso ai não é poligono...")

elif nlados > 5: #função que imprime mensagem caso o numero de lados seja maior que 5
  print("Poligono não identificado, tente novamente...")

elif nlados == 3: #função que calcula a área do poligono, caso o numero de lados for 3
  area = ((medidaLado ** 2) * (3 ** (1/2))) /4 #formula de calculo da area de um triangulo 
  print("Este TRIANGULO tem uma área de: %.2f cm²" %area) #printa resultado do programa

elif nlados == 4: #função que calcula a área do poligono, caso o numero de lados for 4
  area = medidaLado ** 2 #formula de calculo da area de um triangulo 
  print("Este QUADRADO tem uma área de: %.2f cm²" %area) #printa resultado do programa

elif nlados == 5: #função que printa pentagono caso digitem o valor 5
  print("Isso é um PENTÁGONO !!!!!")

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4

numero1 = int (input( "Digite o primeiro número: ")) #recebe o primeiro numero
numero2 = int (input( "Digite o segundo número: ")) #recebe o segundo numero
numero3 = int (input( "Digite o terceiro número: ")) #recebe o terceiro numero

if numero1 > numero2 and numero1 > numero3: #condição para printar o numero 1 como maior numero
  numeroMaior = numero1 
  print("O maior numero é o numero %2i" %numeroMaior)

elif numero2 > numero1 and numero2 > numero3: #condição para printar o numero 2 como maior numero
  numeroMaior = numero2
  print("O maior numero é o numero %2i" %numeroMaior)
  
elif numero3 > numero2 and numero3 > numero1:#condição para printar o numero 3 como maior numero
  numeroMaior = numero3
  print("O maior numero é o numero %2i" %numeroMaior)

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4

ado1 = float (input( "Digite o valor em centímentros para o primeiro lado do triangulo: ")) #recebe o primeiro lado
lado2 = float (input( "Digite o valor em centímentros para o segundo lado do triangulo: ")) #recebe o segundo lado
lado3 = float (input( "Digite o valor em centímentros para o terceiro lado do triangulo: ")) #recebe o terceiro numero

if lado1 == lado2 and lado2 == lado3: #condição para printar equilaterio
  print(" Este Triangulo é um triangulo EQUILATERO")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: #condição para printar isosceles
  print(" Este Triangulo é um triangulo ISOSCELES")

elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1: #condição para printar escaleno
  print(" Este Triangulo é um triangulo ESCALENO")

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4

lado1 = float (input( "Digite o valor em centímentros para o primeiro lado do triangulo: ")) #recebe o primeiro lado
lado2 = float (input( "Digite o valor em centímentros para o segundo lado do triangulo: ")) #recebe o segundo lado
lado3 = float (input( "Digite o valor em centímentros para o terceiro lado do triangulo: ")) #recebe o terceiro lado

if lado1 == lado2 and lado2 == lado3: #condição para printar equilaterio
  print(" Este Triangulo é um triangulo EQUILATERO")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: #condição para printar isosceles
  print(" Este Triangulo é um triangulo ISOSCELES")

elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1: #condição para printar escaleno
  print(" Este Triangulo é um triangulo ESCALENO")

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4

angulo1 = int (input( "Digite o valor do primeiro ângulo do triangulo: ")) #recebe o primeiro angulo
angulo2 = int (input( "Digite o valor do segundo ângulo do triangulo: ")) #recebe o segundo angulo
angulo3 = int (input( "Digite o valor do terceiro ângulo do triangulo: ")) #recebe o terceiro angulo


if angulo1 == 90 or angulo2 == 90 or angulo3 == 90: #condição para printar Retângulo
  print(" Este Triangulo é um triangulo retângulo")

elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90: #condição para printar Acutângulo
  print(" Este Triangulo é um triangulo acutângulo")


elif angulo1 or angulo2 or angulo3 > 90: #condição para printar obtusângulo
  print(" Este Triangulo é um triangulo obtusângulo")

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4
numero = int (input( "Digite o valor do numero: ")) #recebe o primeiro numero

for numero in range(0,numero+1):#printa tudo de 0 até o numero digitado
  print("%2i" %numero)

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4

numero = int (input( "Digite o valor do numero entre 1 e 4: ")) #recebe um numero de 1 a 4

if numero == 1 or numero == 2 or numero == 3 or numero == 4: #valida se o numero é 1,2,3 ou 4
        print("Acesso concedido")
       
elif numero > 4 or numero < 1: # valida se o numero é maior que 4 ou menor que 1
  while True: #laço de repetição para retornar ao primeiro comando input caso o usuário digite um numero incorreto
      print("Numero inválido!")
      print("Tente novamente!")
      numero = int (input( "Digite o valor do numero entre 1 e 4: ")) #recebe novamente o digito
      
      if numero == 1 or numero == 2 or numero == 3 or numero == 4: #verifica novamente se o digito está correto
        print("Acesso concedido")
        break #encerra o loop

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4
lista = [] #declarando uma lista vazia
while True: #criando laço para guardar os inputs na lista enquanto ela existir
    n = int(input("Digite os números ou pressione '0' para encerrar: ")) #coletando os dados digitados para inserir na lista
    lista.append(n) #cria um item na lista a cada digito do usuario
    if n == 0: #condição para parar o programa
        print ("O maior número digitado é: ", max(lista)) 
        break

# Disciplina: Probabilidade e Estatística
# Aluno: Artur Campos Batista - 2014290012
# Lista 4
numero = int (input( "Digite um numero de 4 digitos (Ex: 1234) para decompormos este numero: ")) #recebe um numero de 4 digitos
n = str (numero) #declarando uma string para armazenar os dados do numero informado

if numero <1000 or numero >9999: #condição caso o numero não tenha 4 digitos  
  while True: #laço de repetição para toda vez que o usuário digitar um numero que não contenha 4 digitos
    print("O numero informado não têm 4 digitos! Tente novamente")
    numero = int (input( "Digite um numero de 4 digitos (Ex: 1234) para decompormos este numero: ")) #recebe um numero de 4 digitos     
    n = str (numero) #declarando uma string para armazenar os dados do numero informado
    
    if numero >= 1000 and numero <= 9999: #condição para identificar se o numero tem 4 digitos  novamente
      print("Fazendo varredura do numero informado, aguarde... Numero: {}" .format(numero)) #utilizando .format para inserir o numero na string
      print("Unidade: {}" .format (n[3])) #imprimindo a string na posição 3
      print("Dezena: {}" .format (n[2]))  #imprimindo a string na posição 2
      print("Centena: {}" .format (n[1])) #imprimindo a string na posição 1
      print("Milhar: {}" .format (n[0])) #imprimindo a string na posição 0
      break

elif numero >= 1000 and numero <= 9999: #condição para identificar se o numero tem 4 digitos
   print("Fazendo varredura do numero informado, aguarde... Numero: {} " .format(numero)) #utilizando .format para inserir o numero na string
   print("Unidade: {}" .format (n[3])) #imprimindo a string na posição 3
   print("Dezena: {}" .format (n[2]))  #imprimindo a string na posição 2
   print("Centena: {}" .format (n[1])) #imprimindo a string na posição 1
   print("Milhar: {}" .format (n[0])) #imprimindo a string na posição 0