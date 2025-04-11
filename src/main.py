import sys
import os

# Ajoutes le dossier 'src' au sys.path pour que Python puisse l'importer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.recipe_table import NutriscoreEnum, Recipe
# from models.recipe_review_table import RecipeReview
# from models.category_table import Category
# from models.recipe_has_category_table import RecipeHasCategory
# from models.equipment_table import Equipment
# from models.recipe_has_equipment_table import RecipeHasEquipment
# from models.unit_of_measure_table import UnitOfMeasure
# from models.ingredient_table import Ingredient
# from models.recipe_has_ingredient_table import RecipeHasIngredient

from services.recipe_service import RecipeService
# from services.recipe_review_service import RecipeReviewService
# from services.category_service import CategoryService
# from services.recipe_has_category_service import RecipeHasCategoryService
# from services.equipment_service import EquipmentService
# from services.recipe_has_equipment_service import RecipeHasEquipmentService
# from services.unit_of_measure_service import UnitOfMeasureService
# from services.ingredient_service import IngredientService
# from services.recipe_has_ingredient_service import RecipeHasIngredientService

from database.connection import Session

from scraper.recipe_scraper import RecipeScraper

def main():
    recipe_scraper = RecipeScraper("https://www.quitoque.fr/recettes")
    recipe_scraper.make_request("salade-de-quinoa-aux-petits-pois-pomelo-avocat-et-pignons-de-pin")
    recipe = recipe_scraper.parse_recipe()

    # Générer la requête d'insertion pour plusieurs objets
    sql, params = RecipeService.to_sql_insert(recipe)
    print(f"Requête SQL générée : {sql}")
    print(f"Paramètres : {params}")

    with Session() as session:
        # Exécute la requête SQL d'insertion
        session.execute(sql, params)
        session.commit()
        print("Recettes insérées avec succès dans la base de données.")

if __name__ == "__main__":
    main()

# def main():
    # recipes = [
    #     Recipe(
    #         title = "Salade César",
    #         subTitle = "Avec du poulet",
    #         url = "https://example.com/recette/saladecesar",
    #         totalTime = 15,
    #         cookTime = 10,
    #         nutriscore = NutriscoreEnum.B
    #     ),
    #     Recipe(
    #         title = "Tarte aux pommes",
    #         subTitle = "Avec de la cannelle",
    #         url = "https://example.com/recette/tarteauxpommes",
    #         totalTime = 45,
    #         cookTime = 30,
    #         nutriscore = NutriscoreEnum.C
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = RecipeService.to_sql_insert_multiple_secure(recipes)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
    #     # Exécute la requête SQL d'insertion
    #     session.execute(sql, params)
    #     session.commit()
    #     print("Recettes insérées avec succès dans la base de données.")

    # reviews = [
    #     RecipeReview(
    #         fk_RecipeId = 1,
    #         IsVerified = True,
    #         TimesCooked = 5,
    #         Comments = "Délicieuse recette !",
    #         LastCookedDate = "2023-10-01 12:00:00"
    #     ),
    #     RecipeReview(
    #         fk_RecipeId = 2,
    #         IsVerified = False,
    #         TimesCooked = 2,
    #         Comments = "Un peu trop sucrée à mon goût.",
    #         LastCookedDate = "2023-10-02 14:30:00"
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = RecipeReviewService.to_sql_insert_multiple_secure(reviews)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
    #     # Exécute la requête SQL d'insertion
    #     session.execute(sql, params)
    #     session.commit()
    #     print("Avis insérés avec succès dans la base de données.")

    # categories = [
    #     Category(
    #         categoryName = "Healthy"
    #     ),
    #     Category(
    #         categoryName = "Express"
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = CategoryService.to_sql_insert_multiple_secure(categories)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
    #     # Exécute la requête SQL d'insertion
    #     session.execute(sql, params)
    #     session.commit()
    #     print("Catégories insérées avec succès dans la base de données.")

    # recipe_has_categories = [
    #     RecipeHasCategory(
    #         fk_RecipeId = 1,
    #         fk_CategoryId = 1
    #     ),
    #     RecipeHasCategory(
    #         fk_RecipeId = 2,
    #         fk_CategoryId = 2
    #     ),
    #     RecipeHasCategory(
    #         fk_RecipeId = 1,
    #         fk_CategoryId = 2
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = RecipeHasCategoryService.to_sql_insert_multiple_secure(recipe_has_categories)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
    #     # Exécute la requête SQL d'insertion
    #     session.execute(sql, params)
    #     session.commit()
    #     print("Relations recette-catégorie insérées avec succès dans la base de données.")

    # equipments = [
    #     Equipment(
    #         equipmentName = "Four"
    #     ),
    #     Equipment(
    #         equipmentName = "Mixeur"
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = EquipmentService.to_sql_insert_multiple_secure(equipments)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
    #     # Exécute la requête SQL d'insertion
    #     session.execute(sql, params)
    #     session.commit()
    #     print("Equipements insérés avec succès dans la base de données.")

    # recipe_has_equipments = [
    #     RecipeHasEquipment(
    #         fk_RecipeId = 1,
    #         fk_EquipmentId = 1
    #     ),
    #     RecipeHasEquipment(
    #         fk_RecipeId = 2,
    #         fk_EquipmentId = 2
    #     ),
    #     RecipeHasEquipment(
    #         fk_RecipeId = 1,
    #         fk_EquipmentId = 2
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = RecipeHasEquipmentService.to_sql_insert_multiple_secure(recipe_has_equipments)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
    #     # Exécute la requête SQL d'insertion
    #     session.execute(sql, params)
    #     session.commit()
    #     print("Relations recette-équipement insérées avec succès dans la base de données.")

    # unit_of_measures = [
    #     UnitOfMeasure(
    #         unitOfMeasureSymbol = "g"
    #     ),
    #     UnitOfMeasure(
    #         unitOfMeasureSymbol = "ml"
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = UnitOfMeasureService.to_sql_insert_multiple_secure(unit_of_measures)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
    #     # Exécute la requête SQL d'insertion
    #     session.execute(sql, params)
    #     session.commit()
    #     print("Unités de mesure insérées avec succès dans la base de données.")

    # ingredients = [
    #     Ingredient(
    #         ingredientName = "Poulet",
    #         fk_UnitOfMeasureId = 1
    #     ),
    #     Ingredient(
    #         ingredientName = "Eau",
    #         fk_UnitOfMeasureId = 2
    #     ), 
    #     Ingredient(
    #         ingredientName = "Pomme",
    #         fk_UnitOfMeasureId = 1
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = IngredientService.to_sql_insert_multiple_secure(ingredients)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
    #     # Exécute la requête SQL d'insertion
    #     session.execute(sql, params)
    #     session.commit()
    #     print("Ingrédients insérés avec succès dans la base de données.")

    # recipe_has_ingredients = [
    #     RecipeHasIngredient(
    #         fk_RecipeId = 1,
    #         fk_IngredientId = 1,
    #         quantity = 200
    #     ),
    #     RecipeHasIngredient(
    #         fk_RecipeId = 2,
    #         fk_IngredientId = 2,
    #         quantity = 100
    #     ),
    #     RecipeHasIngredient(
    #         fk_RecipeId = 1,
    #         fk_IngredientId = 3,
    #         quantity = 150
    #     )
    # ]

    # # Générer la requête d'insertion pour plusieurs objets
    # sql, params = RecipeHasIngredientService.to_sql_insert_multiple_secure(recipe_has_ingredients)
    # print(f"Requête SQL générée : {sql}")
    # print(f"Paramètres : {params}")

    # with Session() as session:
        # # Exécute la requête SQL d'insertion
        # session.execute(sql, params)
        # session.commit()
        # print("Relations recette-ingrédient insérées avec succès dans la base de données.")