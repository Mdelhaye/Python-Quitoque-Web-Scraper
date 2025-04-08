from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.config import DATABASE_CONFIG

# Connection à la base de données
engine = create_engine(f"mysql+pymysql://{DATABASE_CONFIG["user"]}:{DATABASE_CONFIG["password"]}@{DATABASE_CONFIG["host"]}/{DATABASE_CONFIG["database"]}", echo = False)

# Session SQLAlchemy
Session = sessionmaker(bind = engine)