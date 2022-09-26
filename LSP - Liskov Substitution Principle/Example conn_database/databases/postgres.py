from dataclasses import dataclass, field
from conn import Connection

Con = str


@dataclass
class PostgresRepo(Connection):
    name_conn: Con = field(default='Postgres', init=False)

    def select(self) -> None:
        self.connect()
        print(f'Connected to {self.name_conn}...')
        print('Performing a SELECT * FROM...')
        self.disconnect()

    def insert(self) -> None:
        self.connect()
        print(f'Connected to {self.name_conn}...')
        print('Performing a INSERT VALUES...')
        self.disconnect()
