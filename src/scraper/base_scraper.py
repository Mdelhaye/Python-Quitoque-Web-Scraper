from bs4 import BeautifulSoup, Tag
import requests
import re

class BaseScraper:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.soup = None

    def make_request(self, endpoint: str) -> str:
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    
    def parse_html(self, html_content):
        return BeautifulSoup(html_content, 'html.parser')
    
    def check_soup(self) -> None:
        if not self.soup:
            raise Exception("No soup available. Please make a request first.")

    def clean_data(self, data):
        return data.strip() if isinstance(data, str) else data  # Example cleaning method

    def clean_data_number(self, data: str) -> int:
        match = re.search(r"(?:(\d+)h)?(?:(\d+)m?)?", data)

        if match:
            hours = int(match.group(1)) if match.group(1) else 0
            minutes = int(match.group(2)) if match.group(2) else 0
            return hours * 60 + minutes
        else:
            return 0