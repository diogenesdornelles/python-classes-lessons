from dataclasses import dataclass, field
from databases import MySQLRepo, PostgresRepo


@dataclass
class User:
    user_name: str = field(default='DDC23', init=False)

    def search(self, db_repo: [PostgresRepo | MySQLRepo]):
        print(f'Query by {self.user_name}...')
        db_repo.connect()
        print(f'Connected to {db_repo.name_conn}...')
        print('Performing a SEARCH * FROM...')
        print('Query carried out...')
        db_repo.disconnect()
