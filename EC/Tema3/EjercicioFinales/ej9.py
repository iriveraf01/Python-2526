# Ejercicio 9 - Ejercicio completo (Herencia + Polimorfismo + Composición + ABC)
# Tema: Gestión de contenido multimedia en una plataforma educativa
# Se quiere desarrollar un sistema básico para gestionar distintos tipos de recursos
# educativos.
# Todos los recursos comparten:
# • título
# • tamaño en MB
# • método mostrar_info()
# Define una clase abstracta Recurso con dicho método.
# Se deben implementar 3 tipos de recursos:
# 1. Video
# • duración en minutos
# • sobrescribe mostrar_info():[VIDEO] X | Duración: X min | Tamaño: X MB.
# 2. DocumentoPDF
# • número de páginas
# • sobrescribe mostrar_info(): [PDF] X | Páginas: X | Tamaño: X MB.
# 3. CursoInteractivo
# • Composición: contiene una lista de recursos (vídeos o pdfs) internos
# • sobrescribe mostrar_info() para mostrar: [CURSO] X. Tamaño total: X MB.
# Recursos incluidos: - Titulo (X MB)…
# • tamaño total (suma de los recursos)
# • lista de títulos internos
# Tareas adicionales
# 1. Crear un curso interactivo con varios recursos dentro.
# 2. Crear una lista con objetos de tipos diferentes (Video, DocumentoPDF,
# CursoInteractivo).
# 3. Recorrer la lista mostrando la información de todos los recursos usando
# polimorfismo.
from abc import ABC, abstractmethod

class Recurso(ABC):
    def __init__(self, titulo, mb):
        self.titulo = titulo
        self.mb = mb

    @abstractmethod
    def mostrar_info(self):
        pass

class Video(Recurso):
    def __init__(self, titulo, mb, duracion):
        super().__init__(titulo, mb)
        self.duracion = duracion

    def mostrar_info(self):
        print(f"[VIDEO] {self.titulo} | Duración: {self.duracion} min | Tamaño: {self.mb} MB.")

class DocumentoPDF(Recurso):
    def __init__(self, titulo, mb, numero_paginas):
        super().__init__(titulo, mb)
        self.numero_paginas = numero_paginas
    
    def mostrar_info(self):
        print(f"[PDF] {self.titulo} | Páginas: {self.numero_paginas} | Tamaño: {self.mb} MB.")

class CursoInteractivo(Recurso):
    def __init__(self, titulo, recursos):
        # recursos: lista de objetos Recurso (Video o DocumentoPDF)
        total_mb = sum(recurso.mb for recurso in recursos)
        super().__init__(titulo, total_mb)
        self.recursos = list(recursos)

    def mostrar_info(self):
        print(f"[CURSO] {self.titulo}. Tamaño total: {self.mb} MB.")
        print("Recursos incluidos:")
        for recurso in self.recursos:
            print(f"- {recurso.titulo} ({recurso.mb} MB)")


v1 = Video("Introducción a Redes", 300.0, 45)
v2 = Video("Práctica VLANs", 250.0, 35)
d1 = DocumentoPDF("Apuntes de Subredes", 5.0, 40)
curso = CursoInteractivo("Curso de Redes Básicas", [v1, v2, d1])
recursos: list[Recurso] = [
    v1,
    d1,
    curso,
]
for r in recursos:
    r.mostrar_info()
    print("-" * 40)