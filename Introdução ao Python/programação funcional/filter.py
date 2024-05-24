'''
Aplica uma função lógica (que retorna um booleano) em todos os elementos de uma coleção (`list`, `dict`, etc.) e retorna **apenas** aqueles que resultaram em verdadeiro (`True`).

variavel = filter(função, coleção)
'''


numeros = [1, 2, 3]

numeros_par = filter(lambda num: num % 2 == 0, numeros)

print(list(numeros_par))


#### **3.2. Função de alta ordem** 

emails = ['andre.perez@gmail.com', 'andre.perez@live.com', 'andre.perez@yahoo.com']
provedor_da_google = lambda email: 'gmail' in email


emails_google = []
for email in emails:
  if provedor_da_google(email) == True:
    emails_google.append(email)

print(emails_google)


emails_google = filter(provedor_da_google, emails)
print(emails_google)

emails_google = list(filter(provedor_da_google, emails))
print(emails_google)

emails_google = filter(lambda email: 'gmail' in email, emails)
...
print(list(emails_google))