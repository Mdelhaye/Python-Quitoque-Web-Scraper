from sqlalchemy import insert, select, or_, and_
from sqlalchemy.sql.dml import Insert
from sqlalchemy.dialects.mysql import insert
from enum import Enum

def generate_insert_query(table, object) -> str:
    """
    Génère une requête SQL INSERT pour un objet donnée en utilisant ses attributs.
    """
    if table is None or not object:
        raise ValueError("La table ou l'objet est vide.")

    return insert(table).values(object)
    

def generate_insert_multiple_query(table, objects: list) -> str:
    """
    Génère une requête SQL INSERT pour plusieurs objets en utilisant leurs attributs.
    """
    if table is None or not objects:
        raise ValueError("La table ou la liste des objets est vide.")

    # Construire les valeurs à insérer
    values = []
    for obj in objects:
        row = {}
        for column in table.columns:
            if column.server_default is None:  # Exclure les colonnes avec des valeurs par défaut côté serveur
                value = getattr(obj, column.name)
                if isinstance(value, Enum):
                    value = value.value  # Convertir l'énumération en sa valeur si nécessaire
                row[column.name] = value
        values.append(row)

    # Générer la requête SQL avec insert() et values()
    return insert(table).values(values)

def generate_select_query(table, object) -> str:
    """
    Génère une requête SQL SELECT pour un objet donnée en utilisant ses attributs.
    """
    if table is None or not object:
        raise ValueError("La table ou l'objet est vide.")

    # Obtenir les colonnes de la table
    columns = [column.name for column in table.columns]

    # Construire la clause WHERE en fonction des attributs de l'objet
    where_clause = []
    for column in columns:
        value = getattr(object, column, None)
        if value is not None:
            if isinstance(value, Enum):
                value = value.value  # Convertir l'énumération en sa valeur si nécessaire
            where_clause.append(getattr(table.c, column) == value)

    # Générer la requête SELECT avec la clause WHERE
    return select(table).where(*where_clause)

def generate_select_multiple_query(table, objects: list) -> str:
    """
    Génère une requête SQL SELECT pour plusieurs objets en utilisant leurs attributs.
    """
    if table is None or not objects:
        raise ValueError("La table ou la liste des objets est vide.")

    # Obtenir les colonnes de la table
    columns = [column.name for column in table.columns]

    # Construire la clause WHERE avec OR pour plusieurs objets
    where_clauses = []
    for obj in objects:
        obj_conditions = []
        for column in columns:
            value = getattr(obj, column, None)
            if value is not None:
                if isinstance(value, Enum):
                    value = value.value  # Convertir l'énumération en sa valeur si nécessaire
                obj_conditions.append(getattr(table.c, column) == value)
        if obj_conditions:
            where_clauses.append(and_(*obj_conditions))  # Combine les conditions d'un objet avec AND

    if not where_clauses:
        raise ValueError("Aucune condition WHERE n'a été générée pour la requête SELECT.")

    # Combine les conditions de tous les objets avec OR
    return select(table).where(or_(*where_clauses))

def run_query(session, query):
    """
    Exécute une requête SQL donnée et retourne le résultat.
    """
    if session is None or query is None:
        raise ValueError("La session ou la requête est vide.")

    return session.execute(query)

def add_on_duplicate_key_update(statement, table):
    """
    Ajoute une clause ON DUPLICATE KEY UPDATE à un statement SQLAlchemy.
    La clause ne modifie rien (elle met à jour les colonnes de la clé primaire avec leurs propres valeurs).
    """
    if not isinstance(statement, Insert):
        raise ValueError("Cette méthode est uniquement compatible avec des statements de type 'insert'.")
    
     # Générer la clause ON DUPLICATE KEY UPDATE
    update_clause = {
        col.name: table.c[col.name]
        for col in table.columns
        if not col.primary_key and not col.autoincrement
    }

    # Si aucune colonne n'est éligible, retourner le statement d'origine
    if not update_clause:
        print("Aucune colonne valide pour ON DUPLICATE KEY UPDATE. La clause sera ignorée.")
        return statement

    # Ajouter la clause au statement
    return statement.on_duplicate_key_update(**update_clause)