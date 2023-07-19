print('Para esse jogo, todas intruções devem ser escritas com letras minusculas e sem acentuação')

jogador_1 = input('\nQual seu nome? ')
jogador_2 = input('\nQual nome do seu oponente? ')

escolha_jg1 = input(f'\nVocê quer ser PAR ou IMPAR, {jogador_1}: ').lower()
escolha_jg2 = input(f'\nVocê quer ser PAR ou IMPAR, {jogador_2}: ').lower()

while (escolha_jg1 == escolha_jg2):
  
  print('\n\nEscolheram a mesma opção, tentem denovo!')
  
  escolha_jg1 = input(f'\nVocê quer ser PAR ou IMPAR, {jogador_1}: ').lower()
  escolha_jg2 = input(f'\nVocê quer ser PAR ou IMPAR, {jogador_2}: ').lower()
  
num_jg1 = int(input(f'\nEscolha um numero para {jogador_1}: '))
num_jg2 = int(input(f'\nEscolha um numero para {jogador_2}: '))

soma = num_jg1 + num_jg2

if (escolha_jg1 == 'impar') and ((soma%2) != 0):
  print(f'\nO vencedor é o jogador {jogador_1}')

elif (escolha_jg1 == 'par') and ((soma%2) == 0):
  print(f'\nO vencedor é o jogador {jogador_1}')

elif (escolha_jg2 == 'impar') and ((soma%2) != 0):
  print(f'\nO vencedor é o jogador {jogador_2}')
  
elif (escolha_jg2 == 'par') and ((soma%2) == 0):
  print(f'\nO vencedor é o jogador {jogador_2}')