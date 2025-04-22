from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, func
from sqlalchemy.orm import relationship
from .base import Base

class RecipeReview(Base):
    __tablename__ = 'RecipeReviewTable'

    fk_RecipeId     = Column(Integer, ForeignKey('RecipeTable.recipeId', ondelete = 'CASCADE', onupdate = 'NO ACTION'), primary_key = True, nullable = False)
    IsVerified      = Column(Boolean, nullable = False, default = False)
    TimesCooked     = Column(Integer, nullable = True)
    Comments        = Column(String(500), nullable = True)
    LastCookedDate  = Column(TIMESTAMP, server_default = func.current_timestamp(), server_onupdate = func.current_timestamp(), nullable = True)

    recipe = relationship("Recipe", back_populates = "reviews", uselist = False)

    def __str__(self):
        return f"RecipeReview(fk_RecipeId={self.fk_RecipeId}, IsVerified={self.IsVerified}, TimesCooked={self.TimesCooked}, Comments={self.Comments}, LastCookedDate={self.LastCookedDate})"