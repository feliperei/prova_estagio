# String a ser invertida
string = "Hello, world!"

# Conversão da string para uma lista de caracteres
lista_caracteres = list(string)

# Índices inicial e final para inversão
inicio = 0
fim = len(lista_caracteres) - 1

# Inversão dos caracteres
while inicio < fim:
    # Troca de posições dos caracteres usando uma variável auxiliar
    aux = lista_caracteres[inicio]
    lista_caracteres[inicio] = lista_caracteres[fim]
    lista_caracteres[fim] = aux

    # Atualização dos índices
    inicio += 1
    fim -= 1

# Conversão da lista de caracteres de volta para uma string
string_invertida = "".join(lista_caracteres)

# Exibição do resultado
print(string_invertida)
