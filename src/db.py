import os
import psycopg2
from dotenv import load_dotenv

def get_db_connection():
    """Establish and return a database connection."""
    load_dotenv()  # Load environment variables
    return psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )

def get_table_names(schema: str = 'public') -> list:
    """Retrieve all table names from a specified schema."""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = %s
                    """, (schema,)
                )
                return [row[0] for row in cursor.fetchall()]
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return []

def get_columns_info(schema: str, table: str) -> list:
    """Retrieve column information for a given table."""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT column_name, data_type, is_nullable 
                    FROM information_schema.columns 
                    WHERE table_schema = %s AND table_name = %s
                    """, (schema, table)
                )
                return [{"column_name": row[0], "data_type": row[1], "is_nullable": row[2]} for row in cursor.fetchall()]
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return []

def create_table(schema: str, table: str, columns: dict):
    """Create a new table with the given name and columns."""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                columns_definition = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
                query = f"""
                    CREATE TABLE {schema}.{table} (
                        {columns_definition}
                    )
                """
                cursor.execute(query)
                conn.commit()
                print(f"Table '{table}' created successfully in schema '{schema}'.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

def add_row(schema: str, table: str, row_data: dict):
    """Insert a new row into the specified table."""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                columns = ", ".join(row_data.keys())
                values_placeholders = ", ".join(["%s"] * len(row_data))
                values = tuple(row_data.values())
                query = f"""
                    INSERT INTO {schema}.{table} ({columns})
                    VALUES ({values_placeholders})
                """
                cursor.execute(query, values)
                conn.commit()
                print(f"Row inserted successfully into '{schema}.{table}'.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    schema_name = 'public'  # Change this if needed
    tables = get_table_names(schema_name)
    print(f"Tables in schema '{schema_name}':", tables)
    
    if tables:
        table_name = tables[0]  # Example: Get columns for the first table
        columns_info = get_columns_info(schema_name, table_name)
        print(f"Columns in table '{table_name}':", columns_info)
    
    # Example usage of create_table function
    new_table_name = 'example_table'
    new_table_columns = {
        'id': 'SERIAL PRIMARY KEY',
        'name': 'VARCHAR(255) NOT NULL',
        'created_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
    }
    create_table(schema_name, new_table_name, new_table_columns)
    
    # Example usage of add_row function
    new_row_data = {
        'name': 'Test Entry',
        'created_at': 'NOW()'
    }
    add_row(schema_name, new_table_name, new_row_data)