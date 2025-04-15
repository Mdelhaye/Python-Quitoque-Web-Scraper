from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

class RecipeListScraper(BaseScraper):
    def __init__(self, base_url: str, endpoint: str = None, soup: BeautifulSoup = None) -> None:
        super().__init__(base_url)
        self.endpoint = endpoint
        self.soup = soup

    def make_request(self, endpoint: str) -> str:
        if not endpoint:
            raise ValueError("Endpoint cannot be empty.")
        
        self.endpoint = endpoint
        self.soup = self.parse_html(
                super().make_request(self.endpoint)
            ).select('a[class="card__content_header"]')
        return self.soup if self.soup else None