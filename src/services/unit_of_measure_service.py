from src.models.unit_of_measure_table import UnitOfMeasure
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class UnitOfMeasureService:
    @staticmethod
    def to_sql_insert(unit_of_measure: UnitOfMeasure) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet UnitOfMeasure.
        """
        sql, params = generate_insert_query(unit_of_measure)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(unit_of_measures: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets UnitOfMeasure.
        """
        query = generate_insert_multiple_secure_query(unit_of_measures)
        return query