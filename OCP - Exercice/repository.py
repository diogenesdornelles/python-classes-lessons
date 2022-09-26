# https://www.youtube.com/watch?v=IlSut-fcKvs&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=10
# Orientação a Objetos em Python — Exercício Princípio Aberto / Fechado

# In object-oriented programming, the open–closed principle states "software entities (classes, modules, functions,
# etc.) should be open for extension, but closed for modification"; that is, such an entity can allow its behaviour
# to be extended without modifying its source code.

# Pt: Em suma, deve procurar-se agregar funcionalidades ao código, caso necessário, sem que o código existente tenha
# que ser alterado, de modo que este, em sua implementação, deve estar aberto para extensões futuras.

from dataclasses import dataclass


@dataclass
class Repository:

    @staticmethod
    def select(db_connection: any) -> None:
        db_connection.connect()
        print(f'Connected to {db_connection.connection}...')
        print('Performing a SELECT * FROM...')
        db_connection.disconnect()

    @staticmethod
    def insert(db_connection: any) -> None:
        db_connection.connect()
        print(f'Connected to {db_connection.connection}...')
        print('Performing a INSERT VALUES...')
        db_connection.disconnect()
