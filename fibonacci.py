''' 1TDCG - 44SEC
Suellen Guedes Rufino
Rakel de Macedo Oliveira
João Victor Santos Alves
Felipe de Resende Madeira
Pedro Henrique Lima Vieira
'''


################################################ MENSAGENS ################################################
boas_vindas = '\nBem-vindo(a) ao contador sequêncial Fibonacci!\n'
sequencia = 'Insira um número para gerar a sequência de Fibonnaci: '
erro_str = '\nOps! Você insiriu letras, por favor insira um número e que seja maior que 2!\n'
erro_numero = '\nPor favor, insira um número que seja maior que 2!\n'
erro_numero_grande = '\nVocê insiriu um número muito grande! Por favor, insira um número menor que 5.000!\n'


# Boas-vindas
print(boas_vindas)

# Tratando o input do usuário  
try:
    # Insira o número
    numero = int(input(sequencia))

    # Se o número for menor do que 2, insira um número maior 
    while numero < 2:
        print(erro_numero)
        numero = int(input(sequencia))

    # Se o número for maior do que 5.000, insira um número menor
    while numero > 5000:
        print(erro_numero_grande)
        numero = int(input(sequencia))

# Tratando inputs que não são do tipo int 
except ValueError:
    print(erro_str)
    numero = int(input(sequencia))

# Primeiro número, segundo número e numero atual
anterior = 0
proximo = 1
atual = 0


# Lista para adicionarmos os números da sequência gerada
lista_fibonacci = []


# Percorrendo a lista de números que o usuário passou
for i in range(numero):
    
    # adicionando o primeiro número na nossa lista 
    lista_fibonacci.append(anterior)
    
    # Gerando nosso número atual 
    atual = proximo
    
    # transformando ele no próximo número da sequência de Fibonnaci
    proximo = anterior
    
    # O próximo número da sequência é o número atual mais o número anterior
    anterior = atual + proximo


# Mostrando para o usuário a sequência de números Fibonnaci
print(f'\nSequência de Fibbonnaci: {lista_fibonacci}\n')
