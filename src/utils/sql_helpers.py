from sqlalchemy.inspection import inspect
from sqlalchemy.sql import text
from enum import Enum

def generate_insert_query(obj) -> str:
    """
    Génère une requête SQL INSERT pour un objet donnée en utilisant ses attributs.
    """
    if not obj:
        return "", {}

    table = obj.__tablename__
    mapper = inspect(obj).mapper
    columns = [
        column.name for column in mapper.columns
        if column.server_default is None
    ]
    values_placeholder = ", ".join([f":{col}" for col in columns])

    sql = text(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({values_placeholder});")

    # Génère les paramètres pour la requête
    params = {}
    for col in columns:
        value = getattr(obj, col)
        if isinstance(value, Enum):
            value = value.value  # Convertit l'énumération en sa valeur si nécessaire
        params[col] = value

    return sql, params

def generate_insert_multiple_secure_query(objects: list) -> str:
    """
    Génère une requête SQL INSERT pour plusieurs objets avec des placeholders sécurisés.
    """
    if not objects:
        return ""

    table = objects[0].__tablename__
    mapper = inspect(objects[0]).mapper
    columns = [
        column.name for column in mapper.columns
        if column.server_default is None
    ]
    values_placeholder = ", ".join([f"({', '.join([f':{col}{i}' for col in columns])})" for i in range(len(objects))])
    
    sql = text(f"INSERT INTO {table} ({', '.join(columns)}) VALUES {values_placeholder};")
    
    params = {}
    for i, obj in enumerate(objects):
        for col in columns:
            value = getattr(obj, col)
            if isinstance(value, Enum):
                value = value.value
            params[f"{col}{i}"] = value
    
    return sql, params