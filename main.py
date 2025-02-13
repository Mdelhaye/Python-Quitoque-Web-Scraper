import re

from classes          import RecipeScraper
from classes.database import QuitoqueDatabase

def main():
    quitoque_db = QuitoqueDatabase()
    recipe_cards_number_before = len(quitoque_db.recipe_cards.get_all_recipes())
    
    recipes = RecipeScraper.get_recipes_from_url("")
    print(f"{len(recipes)} recipe cards retrieved.")

    quitoque_db.recipe_cards.insert_recipes(recipes)
    
    recipe_cards_number_after  = len(quitoque_db.recipe_cards.get_all_recipes())

    print(f"{recipe_cards_number_after - recipe_cards_number_before} recipe cards created.")
    print(f"{recipe_cards_number_after} recipe cards in base.")

## Script entry point
if __name__ == "__main__":
    print("MAIN MENU".center(80, "-"))
    print("1. Scraper.")

    selection = 0
    while int(selection) !=1:
        selection = input("--> Choose between the options (default 1): ")
        selection = int(selection) if re.match(r'^(\d)$', selection) else 1

    if selection == 1:
        main()