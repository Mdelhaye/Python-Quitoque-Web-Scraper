from sqlalchemy     import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base

from models.enums import NutriScore

Base = declarative_base()

class RecipeCardDB(Base):
    __tablename__     = "RecipeCards"
    CardId            = Column(Integer, primary_key = True, autoincrement = True)
    CardTitle         = Column(String(255), nullable = False)
    RecipeURL         = Column(String(512), nullable = False, unique = True)
    ImageURL          = Column(String(512))
    RecipeDuration    = Column(Integer, nullable = False)
    CardCategories    = Column(String(255)) 
    RecipeNutriScore  = Column(Enum(NutriScore), nullable = False)
    CardPageNumber    = Column(Integer, default = 0)