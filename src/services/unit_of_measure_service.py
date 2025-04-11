from src.models.unit_of_measure_table import UnitOfMeasure
from .base_service import BaseService

class UnitOfMeasureService(BaseService):
    @classmethod
    def to_sql_insert(cls, unit_of_measure: UnitOfMeasure) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet UnitOfMeasure.
        """
        sql, params = super().to_sql_insert(unit_of_measure)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, unit_of_measures: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets UnitOfMeasure.
        """
        sql, params = super().to_sql_insert_multiple_secure(unit_of_measures)
        return sql, params