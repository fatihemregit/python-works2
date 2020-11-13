import sqlite3
bağlanti=sqlite3.connect("database.db")
cursor=bağlanti.cursor()
cursor.execute("""INSERT INTO üyeler VALUES ('sad','emre')""")
bağlanti.commit()
bağlanti.close
