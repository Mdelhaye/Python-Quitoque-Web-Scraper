from sqlalchemy     import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

from classes.custom_objects.recipe_card import RecipeCard

from db.config import DATABASE_CONFIG
from db.recipe_card import RecipeCardDB

Base = declarative_base()

class QuitoqueDatabase:
    def __init__(self, host = DATABASE_CONFIG["host"], user = DATABASE_CONFIG["user"], password = DATABASE_CONFIG["password"], database = DATABASE_CONFIG["database"]) -> None:
        self.engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}", echo = False)
        self.Session = sessionmaker(bind = self.engine)
        self.create_tables()

        # Subclasses
        self.recipe_cards = self.RecipeCardTable(self)

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)

    class RecipeCardTable():
        def __init__(self, db_instance):
            self.db = db_instance

        def insert_recipes(self, recipes: set[RecipeCard]):
            session = self.db.Session()
            try:
                query = """
                    INSERT INTO RecipeCards (CardTitle, RecipeURL, ImageURL, RecipeDuration, CardCategories, RecipeNutriScore, CardPageNumber)
                    VALUES (:CardTitle, :RecipeURL, :ImageURL, :RecipeDuration, :CardCategories, :RecipeNutriScore, :CardPageNumber)
                    ON DUPLICATE KEY UPDATE 
                        CardTitle = VALUES(CardTitle),
                        ImageURL = VALUES(ImageURL),
                        RecipeDuration = VALUES(RecipeDuration),
                        CardCategories = VALUES(CardCategories),
                        RecipeNutriScore = VALUES(RecipeNutriScore),
                        CardPageNumber = VALUES(CardPageNumber);
                """

                # Transformer les objets en une liste de dictionnaires
                values = [
                    {
                        "CardTitle": recipe.title,
                        "RecipeURL": recipe.url,
                        "ImageURL": recipe.image_url,
                        "RecipeDuration": recipe.recipe_duration,
                        "CardCategories": ";".join(recipe.categories),
                        "RecipeNutriScore": recipe.nutri_score.value,
                        "CardPageNumber": recipe.page_number
                    }
                    for recipe in recipes
                ]

                # Exécuter toutes les requêtes en une seule fois
                session.execute(text(query), values)
                session.commit()
                print(f"✅ Inserted or updated {len(recipes)} recipes.")
            except Exception as e:
                session.rollback()
                print(f"❌ Error during insertion: {e}")
            finally:
                session.close()


        def get_all_recipes(self) -> None:
            session = self.db.Session()
            recipes = session.query(RecipeCardDB).all()
            session.close()
            return recipes