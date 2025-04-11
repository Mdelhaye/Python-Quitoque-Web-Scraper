from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class BaseService:
    def __init__(self) -> None:
        """
        Base service class for handling SQL operations.
        """
        pass
    
    @staticmethod
    def to_sql_insert(obj) -> str:
        """
        Generates the SQL insert query for a single object.
        """
        sql, params = generate_insert_query(obj)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(objs: list) -> str:
        """
        Generates the SQL insert query for multiple objects.
        """
        query = generate_insert_multiple_secure_query(objs)
        return query