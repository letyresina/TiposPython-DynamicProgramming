# Relembrando: tupla é uma sequência de items mas >não é possível modificar<

tupla = 4, 5, 6
print(tupla)
print(tupla[1]) # pegando o valor do indíce de tal tupla

# Tupla dentro de uma tupla -> tupla de tupla
tuplaTupla = (4, 5, 6), (7, 8) # posso ter várias sequências, mas isso vai gerar uma matriz
print(tuplaTupla)
# SE você pedir para retornar o indice de uma tupla de tupla, vai retornar a tupla que tá na ordem, como exemplo:
print(tuplaTupla[0])
#Se quiser acessar o valor de uma tupla específico, você precisa especificar os dois 
print(tuplaTupla[0][0])
print(tuplaTupla[1][0])

# Exemplo com string
tuplaString = tuple('string') # isso vai destrinchar a palavra
print(tuplaString)
print(tuplaString[3])

# Reforçando novamente, a tupla é imutável, mas você pode ter vários valores diferentes nela como
tuplaDiversos = tuple(['for', [1,2], True])
print(tuplaDiversos)
print(tuplaDiversos[2])
# só daria para inserir CASO e APENAS dentro da tupla houver algo mutável, como uma lista, em que:
tuplaDiversos[1].append(4)
print(tuplaDiversos)