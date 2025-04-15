from scraper.recipe_scraper import RecipeScraper
from models.category_table import Category

class CategoryScraper(RecipeScraper):
    def __init__(self, recipe_scraper: RecipeScraper):
        """
        Initialise CategoryScraper en réutilisant l'instance de RecipeScraper.
        """
        if not recipe_scraper.base_url:
            raise ValueError("RecipeScraper n'est pas encore initialisé avec une URL de base.")

        if not recipe_scraper.soup:
            raise ValueError("RecipeScraper n'a pas encore chargé de contenu HTML. Appelez 'make_request' d'abord.")
        
        super().__init__(recipe_scraper.base_url, recipe_scraper.endpoint, recipe_scraper.soup)

    def parse_categories(self):
        """
        Parse les catégories à partir de l'HTML.
        """
        categories = self.soup.select("#product-tags > span")
        return [Category(categoryName = super().clean_data(category.get_text())) for category in categories]