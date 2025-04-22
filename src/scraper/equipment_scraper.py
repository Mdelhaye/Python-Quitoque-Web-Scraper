from scraper.recipe_scraper import RecipeScraper
from models.equipment_table import Equipment

class EquipmentScraper(RecipeScraper):
    def __init__(self, recipe_scraper: RecipeScraper):
        """
        Initialise EquipmentScraper en réutilisant l'instance de RecipeScraper.
        """
        if not recipe_scraper.base_url:
            raise ValueError("RecipeScraper n'est pas encore initialisé avec une URL de base.")

        if not recipe_scraper.soup:
            raise ValueError("RecipeScraper n'a pas encore chargé de contenu HTML. Appelez 'make_request' d'abord.")
        
        super().__init__(recipe_scraper.base_url, recipe_scraper.endpoint, recipe_scraper.soup)

    def parse_equipments(self):
        """
        Parse les équipements à partir de l'HTML.
        """
        equipments = self.soup.select("div#equipment > ul > li")
        return [Equipment(equipmentName = super().clean_data(equipment.get_text()).lower()) for equipment in equipments]