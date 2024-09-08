from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем движок для базы данных SQLite
DATABASE_URL = 'sqlite:///taskmanager.db'
engine = create_engine(DATABASE_URL, echo=True)

# Создаем локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем базовый класс для моделей
Base = declarative_base()

