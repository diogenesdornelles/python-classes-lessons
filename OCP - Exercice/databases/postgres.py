from dataclasses import dataclass, field


@dataclass
class PostgresDB:
    connection: str = field(default='Postgres')

    def connect(self) -> str:
        print(f'Connecting to databank {self.connection}...')
        return self.connection

    def disconnect(self) -> None:
        print(f'Disconnected from databank {self.connection}.')
