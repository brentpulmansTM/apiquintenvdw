from pydantic import BaseModel


class star_wars_base(BaseModel):
    name: str
    faction_id: int
    lightsaber_Wielder: bool
    age: int
    species: str
    addition: str | None = None


class star_wars(star_wars_base):
    id: int


class star_wars_create(star_wars_base):
    pass


class faction_base(BaseModel):
    id: int
    name: str