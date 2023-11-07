from pydantic import BaseModel

class star_wars_base(BaseModel):
    name: str
    faction: str
    lightsaber_Wielder: bool
    age: int
    species: str
    addition: str = None

class star_wars(star_wars_base):
    id: int


class star_wars_create(star_wars_base):
    pass