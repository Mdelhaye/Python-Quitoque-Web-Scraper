from models import NutriScore
from bs4    import Tag          ## To type the HTML entry

import re

class RecipeCard:
    def __init__(self, recipe_duration: int, title: str, url: str, image_url: str, categories: set[str], nutri_score: NutriScore) -> None:
        self.recipe_duration = recipe_duration
        self.title = title
        self.url = url
        self.image_url = image_url
        self.categories = categories
        self.nutri_score = nutri_score

    def __repr__(self) -> str:
        return (
            f"Recipe \t (\n"
            f"\tTitle :\t\t{self.title},\n"
            f"\tDuration :\t{self.recipe_duration},\n"
            f"\tLink :\t\t{self.url},\n"
            f"\tImage :\t\t{self.image_url},\n"
            f"\tCategories :\t{self.categories},\n"
            f"\tNutri Score :\t{self.nutri_score.value}\n"
            f")"
        )
    
    @staticmethod
    def from_html(recipe_html: Tag):
        """Construct RecipeCard from HTML."""

        title_tag = recipe_html.select_one(".card__content_title a")
        title = title_tag.text.strip() if title_tag else "Unknow title"

        url = "https://www.quitoque.fr" + title_tag["href"] if title_tag else "#"

        image_tag = recipe_html.select_one("img.lazy")
        image_url = image_tag["data-srcset"] if image_tag else ""

        duration_tag = recipe_html.select_one(".recipe-duration p")
        duration_text = duration_tag.text.strip() if duration_tag else "0 min"

        match = re.search(r"(?:(\d+)h)?(?:(\d+)m?)?", duration_text)

        if match:
            hours = int(match.group(1)) if match.group(1) else 0
            minutes = int(match.group(2)) if match.group(2) else 0
            recipe_duration = hours * 60 + minutes
        else:
            recipe_duration = 0

        category_tag = recipe_html.select_one(".card__content_subtitle p")
        categories = set(category_tag.text.strip().split(" · ")) if category_tag else set()

        nutri_score_tag = recipe_html.select_one(".card__content_action .icon")
        nutri_score_class = nutri_score_tag["class"][1] if nutri_score_tag and len(nutri_score_tag["class"]) > 1 else "nutri-score-unknown"
        nutri_score_value = nutri_score_class.split("-")[-1].upper()
        nutri_score = NutriScore(nutri_score_value) if nutri_score_value in ["A", "B", "C", "D", "E"] else NutriScore("Unknown")

        return RecipeCard(recipe_duration, title, url, image_url, categories, nutri_score)