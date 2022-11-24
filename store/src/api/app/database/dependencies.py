import psycopg2

def get_connection() :
    """Session getter for database. Used as dependency for database itself."""
    conn = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="postgres")
    return conn.cursor()