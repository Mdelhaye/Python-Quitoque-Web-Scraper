from src.models.unit_of_measure_table import UnitOfMeasure
from .base_service import BaseService

class UnitOfMeasureService(BaseService):
    @classmethod
    def to_sql_insert(cls, unit_of_measure: UnitOfMeasure) -> str:
        """
        Generates the SQL insert query for a single object UnitOfMeasure.
        """
        return super().run_query(super().to_sql_insert(UnitOfMeasure.__table__, unit_of_measure))
    
    @classmethod
    def to_sql_insert_multiple(cls, unit_of_measures: list) -> str:
        """
        Generates the SQL insert query for multiple objects UnitOfMeasure.
        """
        return super().run_query(super().to_sql_insert_multiple(UnitOfMeasure.__table__, unit_of_measures))
    
    @classmethod
    def to_sql_select(cls, unit_of_measure: UnitOfMeasure) -> str:
        """
        Generates the SQL select query for a single object UnitOfMeasure.
        """
        return super().run_query(super().to_sql_select(UnitOfMeasure.__table__, unit_of_measure))
    
    @classmethod
    def to_sql_select_multiple(cls, unit_of_measures: list) -> str:
        """
        Generates the SQL select query for multiple objects UnitOfMeasure.
        """
        return super().run_query(super().to_sql_select_multiple(UnitOfMeasure.__table__, unit_of_measures))
    
    @classmethod
    def to_id_dict(cls, unit_of_measures: list) -> dict:
        """
        Converts an object UnitOfMeasure into a dictionary.
        """
        return super().to_id_dict([unit_of_measure.unitOfMeasureName for unit_of_measure in unit_of_measures], [unit_of_measure.unitOfMeasureId for unit_of_measure in unit_of_measures])
    
    @classmethod
    def to_sql_insert_multiple_return_ids(cls, unit_of_measures: list) -> str:
        """
        Generates the SQL insert query for multiple objects UnitOfMeasure and returns the inserted IDs.
        """
        cls.to_sql_insert_multiple(unit_of_measures)
        rows = cls.to_sql_select_multiple(unit_of_measures)
        return cls.to_id_dict([UnitOfMeasure(**row._mapping) for row in rows])