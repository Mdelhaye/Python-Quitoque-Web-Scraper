import requests
from bs4    import BeautifulSoup
from bs4    import Tag              ## To type the HTML entry

from classes import RecipeCard
from classes.database import QuitoqueDatabase

class RecipeScraper:
    BASE_URL    = "https://www.quitoque.fr/recettes"

    @staticmethod
    def main() -> None:
        quitoque_db = QuitoqueDatabase()
        recipe_cards_number_before = len(quitoque_db.recipe_cards.get_all_recipes())
        
        recipes = RecipeScraper.get_recipes_from_url("")
        print(f"{len(recipes)} recipe cards retrieved.")

        quitoque_db.recipe_cards.insert_recipes(recipes)
        
        recipe_cards_number_after  = len(quitoque_db.recipe_cards.get_all_recipes())

        print(f"{recipe_cards_number_after - recipe_cards_number_before} recipe cards created.")
        print(f"{recipe_cards_number_after} recipe cards in base.")

    @staticmethod
    def get_recipes_from_url(url: str) -> set[RecipeCard]:
        current_url = url if url != "" else RecipeScraper.BASE_URL

        response = requests.get(current_url)
        if response.status_code != 200:
            print("Error while retrieving recipes.")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        recipes_html = soup.select(".card.product.recipe")  ## Select recipe cards

        recipes_set = set()
        for recipe_html in recipes_html:
            recipe = RecipeCard.from_html(recipe_html)
            recipe.page_number = RecipeCard.extract_page_number(url)
            recipes_set.add(recipe)

        next_url = RecipeScraper.get_next_page(soup)
        if next_url != "":
            next_url = "https://www.quitoque.fr" + next_url
            recipes_set = recipes_set.union(RecipeScraper.get_recipes_from_url(next_url))

        return recipes_set
    
    @staticmethod
    def get_next_page(current_page_html: Tag) -> str:
        next_page_tag = current_page_html.select_one(".pagination__item--next-page")
        return next_page_tag["href"] if next_page_tag and "href" in next_page_tag.attrs else ""