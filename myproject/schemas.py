from pydantic import BaseModel


class Star_wars_base(BaseModel):
    name: str
    faction_id: int
    lightsaber_Wielder: bool
    age: int
    species: str
    addition: str | None = None


class Star_wars(Star_wars_base):
    id: int

    class Config:
        orm_mode = True


class Star_wars_create(Star_wars_base):
    pass


class Faction_search(BaseModel):
    id: int
    name: str


class Faction_create(BaseModel):
    name: str
