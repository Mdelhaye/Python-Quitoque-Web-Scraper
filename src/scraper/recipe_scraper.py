from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

from models.recipe_table import Recipe, NutriscoreEnum

class RecipeScraper(BaseScraper):
    def __init__(self, base_url: str) -> None:
        super().__init__(base_url)
        self.endpoint = None

    def make_request(self, endpoint: str) -> str:
        if not endpoint:
            raise ValueError("Endpoint cannot be empty.")
        
        self.endpoint = endpoint
        self.soup = self.parse_html(
                super().make_request(self.endpoint)
            ).select_one('#product-show')
        return self.soup if self.soup else None

    def parse_recipe(self) -> Recipe:
        self.check_soup()

        [value, key] = [[self.clean_data_number(value.text) for value in self.soup.select('div:nth-of-type(2) > div:nth-of-type(5) > div > div > p:nth-child(2n+1)')],
                        [self.clean_data(key.text) for key in self.soup.select('div:nth-of-type(2) > div:nth-of-type(5) > div > div > p:nth-child(2n)')]]
        times = dict(zip(key, value))

        title      = self.clean_data(self.soup.select_one('#sylius-product-name').text)
        subtitle   = self.clean_data(self.soup.select_one('div:nth-of-type(2) > div:nth-of-type(3)').text)
        url        = f"{self.base_url}/{self.endpoint}"
        totalTime  = times["Total"]
        cookTime   = times["En cuisine"]
        nutriscore = getattr(NutriscoreEnum,
                            self.soup.select_one('span[class*="nutri-score"]')["class"][-1].split('-')[-1].upper(),
                            "Unknown")

        return Recipe(title = title, subTitle = subtitle, url = url, totalTime = totalTime, cookTime = cookTime, nutriscore = nutriscore)