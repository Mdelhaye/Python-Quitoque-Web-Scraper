import re

from classes import RecipeScraper

def main():
    recipes = RecipeScraper.get_recipes_from_url("")
    for recipe in recipes:
        print(recipe)
    print(len(recipes))
    
    print("Scraping ended.")

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