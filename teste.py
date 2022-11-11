import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM PEDIDO WHERE id=%s", (42,))

conn.commit()

# Retrieve query results
records = cur.fetchall()
