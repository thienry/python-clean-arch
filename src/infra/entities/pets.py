import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum

from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining Animals Types"""

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    age = Column(Integer)
    specie = Column(Enum(AnimalTypes), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"Pet: [name={self.name}, specie={self.specie}], user_id={self.user_id}"
