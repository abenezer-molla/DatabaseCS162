import psycopg2


con = psycopg2.connect(

    dbname="cs162",
    host="localhost",
    port="5432",
    password="Iamawesome@2012"

)

con.autocommit = True

print("ABEN")

cur = con.cursor()

cur.execute("select * from agent")

output = cur.fetchall()

print(output, "output")

for each in output:

    print("Val is", each[1])

cur.close()
