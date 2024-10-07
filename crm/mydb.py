import psycopg2

con = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password='admin'
)

cursor = con.cursor()

print ("success")