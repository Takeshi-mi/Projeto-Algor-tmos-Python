
'''
4. Criptografar uma palavra
• A Cifra de César é uma técnica de criptografia bastante simples e
provavelmente a mais conhecida de todas.
• Trata-se de um tipo de cifra de substituição, na qual cada letra de um texto
a ser criptografado é substituída por outra letra, presente no alfabeto,
porém deslocada um certo número de posições à esquerda ou à direita.
• Por exemplo, se usarmos uma troca de quatro posições à esquerda, cada
letra é substituída pela letra que está quatro posições adiante no alfabeto,
e nesse caso a letra A seria substituída pela letra E, B por F, C por G, e
assim sucessivamente.
• Peça para o usuário inserir uma palavra e uma chave (numero de trocas),
e faça a criptografia dessa palavra. Mostre a palavra inserida e a palavra
criptografada.
'''

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

chave = int(input('Digite um número para definir a chave da criptografia: '))
palavra = input('Digite a palavra a ser criptografada: ').lower().strip()
crypt = ''
for i in palavra:
  indice = alfabeto.index(i)
  nova_letra = alfabeto[(indice+chave)%26] # Tira o módulo de 26 que é a quantidade de letras do alfabeto
  crypt += nova_letra
print('Palavra: ',palavra)
print('Criptografia: ', crypt)