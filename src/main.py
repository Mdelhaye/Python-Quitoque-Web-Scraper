import sys
import os

# Ajoutes le dossier 'src' au sys.path pour que Python puisse l'importer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.recipe_table import NutriscoreEnum, Recipe
from services.recipe_service import RecipeService
from database.connection import Session

def main():
    new_recipe = Recipe(
        title = "Spaghetti au citron",
        subTitle = "Avec un peu de viande",
        url = "https://example.com/recette/spaghettiaucitron",
        totalTime = 25,
        cookTime = 20,
        nutriscore = NutriscoreEnum.A
    )

    list = [
        Recipe(
            title = "Salade César",
            subTitle = "Avec du poulet",
            url = "https://example.com/recette/saladecesar",
            totalTime = 15,
            cookTime = 10,
            nutriscore = NutriscoreEnum.B
        ),
        Recipe(
            title = "Tarte aux pommes",
            subTitle = "Avec de la cannelle",
            url = "https://example.com/recette/tarteauxpommes",
            totalTime = 45,
            cookTime = 30,
            nutriscore = NutriscoreEnum.C
        )
    ]

    sql, params = RecipeService.to_sql_insert(new_recipe)
    print(f"Requête SQL générée : {sql}")
    print(f"Paramètres : {params}")

    with Session() as session:
        # Exécute la requête SQL d'insertion
        session.execute(sql, params)
        session.commit()
        print("Recette insérée avec succès dans la base de données.")

    # Générer la requête d'insertion pour plusieurs objets
    sql, params = RecipeService.to_sql_insert_multiple_secure(list)
    print(f"Requête SQL générée : {sql}")
    print(f"Paramètres : {params}")

    with Session() as session:
        # Exécute la requête SQL d'insertion
        session.execute(sql, params)
        session.commit()
        print("Recettes insérées avec succès dans la base de données.")

if __name__ == "__main__":
    main()