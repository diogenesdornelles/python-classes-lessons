from databases import MySQLRepo, PostgresRepo
from user import User

postgres = PostgresRepo()
mysql = MySQLRepo()
user = User()

user.search(postgres)
