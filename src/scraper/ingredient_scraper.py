from scraper.recipe_scraper import RecipeScraper
from models.ingredient_table import Ingredient
from models.unit_of_measure_table import UnitOfMeasure
import re

class IngredientScraper(RecipeScraper):
    def __init__(self, recipe_scraper: RecipeScraper):
        """
        Initialise IngredientScraper en réutilisant l'instance de RecipeScraper.
        """
        if not recipe_scraper.base_url:
            raise ValueError("RecipeScraper n'est pas encore initialisé avec une URL de base.")

        if not recipe_scraper.soup:
            raise ValueError("RecipeScraper n'a pas encore chargé de contenu HTML. Appelez 'make_request' d'abord.")
        
        super().__init__(recipe_scraper.base_url, recipe_scraper.endpoint, recipe_scraper.soup)

    def parse_ingredients(self):
        """
        Parse les ingrédients à partir de l'HTML.
        """
        quantity_with_unit  = self.soup.select("ul.ingredient-list > li > span:nth-child(2n+1)")

        quantities = []
        units      = []

        for result in quantity_with_unit:
            match = re.match(r"([\d\s]+à[\d\sà]+)(cm)", self.clean_data(result.get_text()))
            if match:
                quantities.append(match.group(1).strip().split(" ")[-1] if match.group(1) else None)
                units.append(match.group(2) if match.group(2) else None)
                continue
            match = re.match(r"([\d.,]+)?\s*(.*)", self.clean_data(result.get_text()))
            if match:
                quantities.append(match.group(1) if match.group(1) else None)
                units.append(match.group(2) if match.group(2) else None)

        ingredients = self.soup.select("ul.ingredient-list > li > span:nth-child(2n)")

        for ingredient in ingredients:
            result = super().clean_data(ingredient.find(text = True).strip())
            if len(result) > 99:
                raise ValueError("Data exceeds maximum length of 45 characters.")
            
        
        return [Ingredient(ingredientName = super().clean_data(ingredient.find(text = True)).lower()) for ingredient in ingredients], quantities, [UnitOfMeasure(unitOfMeasureSymbol = symbol) for symbol in units]