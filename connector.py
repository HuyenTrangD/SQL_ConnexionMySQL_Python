from mysql.connector import connect, Error

cn = connect(
    host="localhost",
    user="root",
    password="root",
    database="ventes"
)

requete = "SELECT * FROM client LIMIT 10;"
cur = cn.cursor()
cur.execute(requete)
resultat = cur.fetchall()
for row in resultat:
    print(row)