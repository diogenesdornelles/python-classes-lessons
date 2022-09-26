from repository import Repository
from databases import PostgresDB, MysqlDB

db_01 = PostgresDB()
db_02 = MysqlDB()
rep1 = Repository()

rep1.insert(db_01)
print()
rep1.select(db_01)
print()
rep1.insert(db_02)
print()
rep1.select(db_02)
