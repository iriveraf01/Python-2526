from collections import Counter

texto = "Python es genial y PYTHON es práctico. Aprender python es útil"

# Procesamiento: Convertimos a minúsculas y separamos por espacios
palabras = texto.lower().split()
# Creamos el Counter, que es un diccionario {palabra:frecuencia}
contador = Counter(palabras)
print(contador)

# 1. Las 5 palabras más frecuentes. Método most_common
print(f"Las 5 palabras más frecuentes: {contador.most_common(5)}")

# 2. Cuántas palabras distintas hay. El tamaño del dict. 
print(f"Cantidad de palabras distintas: {len(contador)}")

# 3. Cuántas veces aparece la palabra 'python'. 
# Contador es un diccinario, se puede indexar por la palabra.
print(f"Veces que aparece 'python': {contador['python']}")



