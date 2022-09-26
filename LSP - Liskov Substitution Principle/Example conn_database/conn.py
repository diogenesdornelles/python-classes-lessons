from dataclasses import dataclass, field

Con = str


@dataclass
class Connection:
    name_conn: Con = field(default='Connection', init=False)

    def connect(self):
        print(f'Connecting to database {self.name_conn}...')

    def disconnect(self):
        print(f'Disconnecting to database {self.name_conn}...')

