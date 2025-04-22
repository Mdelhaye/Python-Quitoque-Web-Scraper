from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

from models.recipe_table import Recipe, NutriscoreEnum

class RecipeScraper(BaseScraper):
    def __init__(self, base_url: str, endpoint: str = None, soup: BeautifulSoup = None) -> None:
        super().__init__(base_url)
        self.endpoint = endpoint
        self.soup     = soup

    def make_request(self, endpoint: str) -> str:
        if not endpoint:
            raise ValueError("Endpoint cannot be empty.")
        
        self.endpoint = endpoint
        self.soup = self.parse_html(
                super().make_request(self.endpoint)
            ).select_one('#product-show')
        return self if self else None

    def parse_recipe(self) -> Recipe:
        self.check_soup()

        [value, key] = [[self.clean_data_number(value.text) for value in self.soup.select('div:nth-of-type(2) > div:nth-of-type(5) > div > div > p:nth-child(2n+1)')],
                        [self.clean_data(key.text) for key in self.soup.select('div:nth-of-type(2) > div:nth-of-type(5) > div > div > p:nth-child(2n)')]]
        times = dict(zip(key, value))

        title      = self.clean_data(self.soup.select_one('#sylius-product-name').text).capitalize()
        subtitle   = self.clean_data(self.soup.select_one('div:nth-of-type(2) > div:nth-of-type(3)').text).capitalize()
        url        = f"{self.base_url}{self.endpoint}"
        totalTime  = times["Total"] if "Total" in times.keys() else 0
        cookTime   = times["En cuisine"] if "En cuisine" in times.keys() else 0
        nutriscore = getattr(NutriscoreEnum,
                            self.soup.select_one('span[class*="nutri-score"]')["class"][-1].split('-')[-1].upper(),
                            "Unknown")

        return Recipe(title = title, subTitle = subtitle, url = url, totalTime = totalTime, cookTime = cookTime, nutriscore = nutriscore)