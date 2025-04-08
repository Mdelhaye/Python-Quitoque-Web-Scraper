import sys
import os

# Ajoutes le dossier 'src' au sys.path pour que Python puisse l'importer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.recipe_table import NutriscoreEnum, Recipe
from models.recipe_review_table import RecipeReview
from services.recipe_service import RecipeService
from services.recipe_review_service import RecipeReviewService
from database.connection import Session

def main():
    recipes = [
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

    # Générer la requête d'insertion pour plusieurs objets
    sql, params = RecipeService.to_sql_insert_multiple_secure(recipes)
    print(f"Requête SQL générée : {sql}")
    print(f"Paramètres : {params}")

    with Session() as session:
        # Exécute la requête SQL d'insertion
        session.execute(sql, params)
        session.commit()
        print("Recettes insérées avec succès dans la base de données.")

    reviews = [
        RecipeReview(
            fk_RecipeId = 1,
            IsVerified = True,
            TimesCooked = 5,
            Comments = "Délicieuse recette !",
            LastCookedDate = "2023-10-01 12:00:00"
        ),
        RecipeReview(
            fk_RecipeId = 2,
            IsVerified = False,
            TimesCooked = 2,
            Comments = "Un peu trop sucrée à mon goût.",
            LastCookedDate = "2023-10-02 14:30:00"
        )
    ]

    # Générer la requête d'insertion pour plusieurs objets
    sql, params = RecipeReviewService.to_sql_insert_multiple_secure(reviews)
    print(f"Requête SQL générée : {sql}")
    print(f"Paramètres : {params}")

    with Session() as session:
        # Exécute la requête SQL d'insertion
        session.execute(sql, params)
        session.commit()
        print("Avis insérés avec succès dans la base de données.")

if __name__ == "__main__":
    main()