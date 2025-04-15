from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_query, generate_select_query, generate_select_multiple_query, run_query
from database.connection import Session

class BaseService:
    def __init__(self) -> None:
        """
        Base service class for handling SQL operations.
        """
        pass
    
    @staticmethod
    def to_sql_insert(table, value) -> str:
        """
        Generates the SQL insert query for a single object.
        """
        return generate_insert_query(table, value)
    
    @staticmethod
    def to_sql_insert_multiple(table, values: list) -> str:
        """
        Generates the SQL insert query for multiple objects.
        """
        return generate_insert_multiple_query(table, values)
    
    @staticmethod
    def to_sql_select(table, value) -> str:
        """
        Generates the SQL select query for a single object.
        """
        return generate_select_query(table, value)
    
    @staticmethod
    def to_sql_select_multiple(table, values: list) -> str:
        """
        Generates the SQL select query for multiple objects.
        """
        return generate_select_multiple_query(table, values)
    
    @staticmethod
    def to_id_dict(keys: list, values: list) -> dict:
        """
        Converts two lists into a dictionary.
        """
        return dict(zip(keys, values))
    
    @staticmethod
    def run_query(query):
        """
        Executes a SQL query and returns the result.
        """
        with Session() as session:
            results = run_query(session, query)
            session.commit()

        return results