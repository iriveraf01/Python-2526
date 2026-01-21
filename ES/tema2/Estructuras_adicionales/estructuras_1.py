from collections import deque

# 1. Inicializar las deques
historial = deque() # almacena páginas visitadas. Se insertan y se eliminan por la derecha
revertidos = deque() # páginas sacadas del historial. Se insertan y se liminan por la izquierda

def visitar_pagina(url):
    """Simula la visita a una nueva página."""
    historial.append(url)
    revertidos.clear() # Limpia el historial de "revertidos" al visitar algo nuevo
    print(f"Visitando: {url} | Historial: {list(historial)}")

def ir_atras():
    """Retrocede una página."""
    # Solamente se puede retroceder si en el historial hay más de 1
    # ya que la última del historial es la actualmente visible
    if len(historial) > 1:
        pagina_actual = historial.pop() # Sacamos la de la derecha del historial
        revertidos.appendleft(pagina_actual) # La metemos en revertidos por la izquierda
        print(f"Volviendo a: {historial[-1]} | Historial: {list(historial)}")
        print(f"    | Revertidos: {list(revertidos)}")
    else:
        print("No hay páginas anteriores para retroceder.")

def ir_adelante():
    """Avanza una página (si es posible)."""
    # Si existe alguna en revertivos podemos ir adelante
    if revertidos:
        pagina_adelante = revertidos.popleft() # Sacamos la última insertada de revertidos
        historial.append(pagina_adelante) # La guardamos en historial
        print(f"Avanzando a: {pagina_adelante} | Historial: {list(historial)}")
        print(f"    | Revertidos: {list(revertidos)}")
    else:
        print("No hay páginas futuras para avanzar.")

# --- Simulación ---
visitar_pagina("google.com")
visitar_pagina("python.org")
visitar_pagina("docs.python.org")

ir_atras() # Vuelve a python.org
ir_atras() # Vuelve a google.com
ir_adelante() # Avanza a python.org




