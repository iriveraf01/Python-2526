# 14. Programar una agenda de contactos.
# Definir la clase Contacto con los atributos nombre, teléfono y correo del contacto.
# a. Añade el método __str__ para que retorne todos los atributos con el formato:
# Nombre - teléfono - correo.
# b. Programa también __repr__ para que retorne los datos del contacto con el
# formato: Contacto(nombre, teléfono, correo).
# c. Programa el método __eq__ para determinar si dos contactos son iguales. En
# este caso serán iguales si coinciden todos los valores de sus atributos.
# Programa la clase Agenda. Esta clase tendrá una lista de contactos y los métodos.
# - Buscar contacto por nombre y retornar el contacto.
# - Obtener el teléfono de un contacto. Retornar el teléfono.
# - Obtener el correo de un contacto. Retornar el correo.
# - Cambiar el teléfono de un contacto. Retornar True si se pudo hacer el cambio,
# False en caso contrario.
# - Cambiar el correo de un contacto. Retornar True si se pudo hacer el cambio,
# False en caso contrario.
# - Listar todos los contactos.
# - Obtener el número de contactos.

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        if valor == 0:
            raise ValueError("El telefono no puede ser 0.")
        self._telefono = valor

    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, valor):
        if valor == "":
            raise ValueError("El correo no puede ser vacío")
        self._correo = valor

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.correo}"
    
    def __repr__(self):
        return f"Contacto(nombre='{self.nombre}', telefono='{self.telefono}', correo='{self.correo}')"

    def __eq__(self, otro):
        if isinstance(otro, Contacto):
            return self.nombre == otro.nombre and self.telefono == otro.telefono and self.correo == otro.correo
        return False 
    
class Agenda:
    lista_contactos = []

    @classmethod
    def buscar_contacto_por_nombre(cls, nombre):
        for contacto in cls.lista_contactos:
            if contacto.nombre == nombre:
                return contacto

    @classmethod
    def telefono_por_contacto(cls, nombre):
        for contacto in cls.lista_contactos:
            if contacto.nombre == nombre:
                return contacto.telefono
            
    @classmethod
    def correo_por_contacto(cls, nombre):
        for contacto in cls.lista_contactos:
            if contacto.nombre == nombre:
                return contacto.correo
            
    @classmethod
    def cambiar_telefono(cls, nombre):
        for contacto in cls.lista_contactos:
            if contacto.nombre == nombre:
                telefono_nuevo = str(input("Introduce un nuevo número: "))
                contacto.telefono = telefono_nuevo
                return contacto
    
    @classmethod
    def cambiar_correo(cls, nombre):
        for contacto in cls.lista_contactos:
            if contacto.nombre == nombre:
                correo_nuevo = str(input("Introduce un nuevo correo: "))
                contacto.correo = correo_nuevo
                return contacto
            
    @classmethod
    def todos_los_contactos(cls):
        for contacto in cls.lista_contactos:
            print(contacto)

    @classmethod
    def numero_de_contactos(cls):
        return len(cls.lista_contactos)
Contacto1 = Contacto("Paco", 123456789, "paco@gmail.com")
Contacto2 = Contacto("Ana", 987654321, "ana@gmail.com")
Agenda.lista_contactos.append(Contacto1)
Agenda.lista_contactos.append(Contacto2)

print(Agenda.buscar_contacto_por_nombre("Ana"))
print(Agenda.telefono_por_contacto("Ana"))
print(Agenda.correo_por_contacto("Ana"))
# print(Agenda.cambiar_telefono("Ana"))
# print(Agenda.cambiar_correo("Ana"))
Agenda.todos_los_contactos()
print(Agenda.numero_de_contactos())