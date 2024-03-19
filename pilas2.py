from queue import LifoQueue

def main():
    pila = LifoQueue(maxsize=8)

    operaciones = [
        ("Insertar", "X"),
        ("Insertar", "Y"),
        ("Eliminar", "Z"),
        ("Eliminar", "T"),
        ("Eliminar", "U"),
        ("Insertar", "V"),
        ("Insertar", "W"),
        ("Eliminar", "p"),
        ("Insertar", "R")
    ]

    for operacion, elemento in operaciones:
        if operacion == "Insertar":
            if not pila.full():
                pila.put(elemento)
                print(f"Se ha insertado {elemento}. Pila: {list(pila.queue)}. Tope: {pila.qsize()}")
            else:
                print("La pila está llena, no se puede insertar más elementos.")
        elif operacion == "Eliminar":
            if not pila.empty():
                elemento_eliminado = pila.get()
                print(f"Se ha eliminado {elemento_eliminado}. Pila: {list(pila.queue)}. Tope: {pila.qsize()}")
            else:
                print("La pila está vacía, no se puede eliminar ningún elemento.")


if __name__ == "__main__":
    main()
