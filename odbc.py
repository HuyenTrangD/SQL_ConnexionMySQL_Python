import pyodbc

print(pyodbc.drivers())

for driver in pyodbc.drivers():
    try:
        cn = pyodbc.connect("DRIVER="+ driver +";SERVER=localhost;DATABASE=ventes;UID=root;PWD=root")
        cur = cn.cursor()
        cur.execute("SELECT nom, prenom FROM Client LIMIT 10;")
        row = cur.fetchone()
        print(row.nom)
    except:
        print("An exception occurred")
