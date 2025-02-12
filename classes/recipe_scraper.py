import requests
from bs4 import BeautifulSoup

from classes import RecipeCard

class RecipeScraper:
    BASE_URL = "https://www.quitoque.fr/recettes"
    
    @staticmethod
    def get_recipes():
        response = requests.get(RecipeScraper.BASE_URL)
        if response.status_code != 200:
            print("Error while retrieving recipes.")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        recipes_html = soup.select(".card.product.recipe")  ## Select recipe cards
        return [RecipeCard.from_html(recipe_html) for recipe_html in recipes_html]