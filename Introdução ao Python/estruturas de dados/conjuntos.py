# Definição
# Armazenam sequências imutáveis e desordenadas valores, sem repetição. São do tipo `set`:

frutas = {'banana', 'maca', 'uva', 'uva'}

print(frutas)
print(type(frutas))

# Operações
#- (diferença)

norte_europa = {'reino unido', 'suecia', 'russia', 'noruega', 'dinamarca'}
escandinavia = {'noruega', 'dinamarca', 'suecia'}

norte_europa_nao_escandivano = norte_europa - escandinavia
print(norte_europa_nao_escandivano)

escandivano_nao_norte_europa = escandinavia - norte_europa
print(escandivano_nao_norte_europa)

# Métodos
cursos = {'Exatas', 'Humanas', 'Biológicas'}
print(cursos)

# inserir um elemento no conjunto: set.add(val)
cursos.add('Saúde')
print(cursos)

# remover um elemento no conjunto: set.remove(val)
cursos.remove('Saúde')
print(cursos)

# Conversão
times_paulistas = {'São Paulo', 'Palmeiras', 'Corinthians', 'Santos'}

print(times_paulistas)
print(type(times_paulistas))

print(list(times_paulistas))
print(type(list(times_paulistas)))
