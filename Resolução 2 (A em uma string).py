def contar_letra_a(texto):
    return texto.lower().count('a')

texto = input("Digite uma palavra para contar as ocorrências da letra 'a': ")
ocorrencias = contar_letra_a(texto)
print(f"A letra 'a' ocorre {ocorrencias} vezes na string.")