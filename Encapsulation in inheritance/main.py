# https://www.youtube.com/watch?v=Io28NuNnhhs&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=14
# Orientação a Objetos em Python — Encapsulamento em Heranças
# Attribute status protected are accessible by own classes and your heritage.
# Attribute status private are accessible only in classes context.

from dataclasses import dataclass, field


@dataclass
class DataBaseConn:
    __database: str = field(default='Postgres', init=False)  # __ = encapsulation private (UML symbol: -)
    _conn: str = field(default='//connection_string', init=False)  # _ encapsulation protected (UML symbol: #)
    user: str = field(default='DDC23', init=False)

    def __get_database(self) -> None:
        print(self.__database)

    def _testing_conn(self) -> str:
        return f'Connection {self.__database} is OK!'

    @property
    def conn(self):
        return self._conn


@dataclass
class Repository(DataBaseConn):
    def select(self) -> str:
        return f'Request from user {self.user}.\n{self._testing_conn()}\nConnecting to {self._conn}\n' \
               f'SELECT * FROM table\nend operation.'


rp = Repository()
db = DataBaseConn()
var = rp.select()
print(var)
