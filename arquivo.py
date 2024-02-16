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

# Outra forma de modificar seria transformar a tupla em lista e depois alterar...

# Então, uma forma 
# Reforçando novamente, a tupla é imutável, mas você pode ter vários valores diferentes nela como
tuplaDiversos2 = tuple(['for', [1,2], True])
print(tuplaDiversos2)
listaDiversa = list(tuplaDiversos2)
posicaoInsercao = listaDiversa.index('for')+1 # pego um index de referência para meu ponto de inserção
listaDiversa.insert(posicaoInsercao, 'hoje') # insiro depois da posição desejada que defini anteriormente
novaTuplaDiversa = tuple(listaDiversa)
print(novaTuplaDiversa)

# Concatenando tuplas
tuplaConcatenada = tuplaDiversos + tuplaString
print(tuplaConcatenada)

# Descompactando tuplas e nomeando variáveis de cada uma
tuplaDescompactando = (4, 5, 6)
a, b, c = tuplaDescompactando # a = 4; b = 5; c = 6
print(a) # posso chamar então pela variável

# exemplo com tupla de tupla
tuplaDescompactando2 = (2, 4), (6, 8)
print(tuplaDescompactando2)
(a, b), (c, d) = tuplaDescompactando2
print(c)

# Descompactação de variáveis e iterar sobre sequência de tplas ou listar
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Nessa parte, ele vai pegar cada indice de cada tupla dentro da lista e chamar pela variável
for a, b, c in seq:
    print('a={0}; b={1}, c={2}'.format(a, b, c))
# Ou seja, o a da primeira tupla é 1, o a da segunda tupla é 4, o a da terceira tupla é 7 e assim sucessivamente

# count - quantidade de vezes que um item aparece na lista/tupla
a = (1, 2, 2, 2, 2, 3, 4, 2)
print(a.count(2))