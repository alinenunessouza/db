"""
    FastAPI dependencies
"""

import psycopg2

def get_db() :
    """Session getter for database. Used as dependency for database itself."""
    conexao = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="postgres")

    cursor = conexao.cursor()

    return cursor
