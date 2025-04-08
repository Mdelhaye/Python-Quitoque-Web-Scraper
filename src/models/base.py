from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker
from src.database.config import DATABASE_CONFIG

# Initialisation du mapper SQLAlchemy
mapper_registry = registry()
Base = mapper_registry.generate_base()

# Connection à la base de données
engine = create_engine(f"mysql+pymysql://{DATABASE_CONFIG["user"]}:{DATABASE_CONFIG["password"]}@{DATABASE_CONFIG["host"]}/{DATABASE_CONFIG["database"]}", echo = False)

# Crée toutes les tables à partir des modèles
Base.metadata.create_all(engine)

# Session SQLAlchemy
Session = sessionmaker(bind = engine)