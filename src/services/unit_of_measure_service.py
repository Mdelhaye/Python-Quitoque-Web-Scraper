from src.models.unit_of_measure_table import UnitOfMeasure
from .base_service import BaseService

class UnitOfMeasureService(BaseService):
    @classmethod
    def to_sql_insert(cls, unit_of_measure: UnitOfMeasure) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet UnitOfMeasure.
        """
        return super().run_query(super().to_sql_insert(UnitOfMeasure.__table__, unit_of_measure))
    
    @classmethod
    def to_sql_insert_multiple(cls, unit_of_measures: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets UnitOfMeasure.
        """
        return super().run_query(super().to_sql_insert_multiple(UnitOfMeasure.__table__, unit_of_measures))
    
    @classmethod
    def to_sql_select(cls, unit_of_measure: UnitOfMeasure) -> str:
        """
        Génère la requête SQL de sélection pour un seul objet UnitOfMeasure.
        """
        return super().run_query(super().to_sql_select(UnitOfMeasure.__table__, unit_of_measure))
    
    @classmethod
    def to_sql_select_multiple(cls, unit_of_measures: list) -> str:
        """
        Génère la requête SQL de sélection pour plusieurs objets UnitOfMeasure.
        """
        return super().run_query(super().to_sql_select_multiple(UnitOfMeasure.__table__, unit_of_measures))
    
    @classmethod
    def to_id_dict(cls, unit_of_measures: list) -> dict:
        """
        Convertit un objet UnitOfMeasure en dictionnaire.
        """
        return super().to_id_dict([unit_of_measure.unitOfMeasureSymbol for unit_of_measure in unit_of_measures], [unit_of_measure.unitOfMeasureId for unit_of_measure in unit_of_measures])
    
    @classmethod
    def to_sql_insert_multiple_return_ids(cls, unit_of_measures: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets UnitOfMeasure et retourne les IDs insérés.
        """
        cls.to_sql_insert_multiple(unit_of_measures)
        rows = cls.to_sql_select_multiple(unit_of_measures)
        return cls.to_id_dict([UnitOfMeasure(**row._mapping) for row in rows])
    
    @classmethod
    def to_sql_insert_if_not_exists(cls, unit_of_measure: UnitOfMeasure) -> str:
        """
        Génère la requête SQL d'insertion pour un objet UnitOfMeasure s'il n'existe pas déjà. S'il existe, retourne son ID.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_unit_of_measure = cls.to_sql_select(unit_of_measure)
        if existing_unit_of_measure:
            return existing_unit_of_measure.unitOfMeasureId
        
        return cls.to_sql_insert(UnitOfMeasure.__table__, unit_of_measure)
    
    @classmethod
    def to_sql_insert_multiple_if_not_exists(cls, unit_of_measures: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets UnitOfMeasure s'ils n'existent pas déjà. S'ils existent, retourne leurs IDs.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        unit_of_measures = [unit for unit in unit_of_measures if unit.unitOfMeasureSymbol != None]
        existing_unit_of_measures         = cls.to_sql_select_multiple(unit_of_measures)
        existing_unit_of_measures_dict    = cls.to_id_dict([UnitOfMeasure(**row._mapping) for row in existing_unit_of_measures])
        existing_unit_of_measures_symbols = existing_unit_of_measures_dict.keys()

        unit_of_measures_to_insert     = [unit for unit in unit_of_measures if unit.unitOfMeasureSymbol not in existing_unit_of_measures_symbols]
        inserted_unit_of_measures_dict = cls.to_sql_insert_multiple_return_ids(unit_of_measures_to_insert) if len(unit_of_measures_to_insert) > 1 else {}

        return {**existing_unit_of_measures_dict, **inserted_unit_of_measures_dict}