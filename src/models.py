from typing import Any
from typing import List

from pydantic import BaseModel


class Traits(BaseModel):
    trait_key: str
    trait_value: Any


class IdentityWithTraits(BaseModel):
    identifier: str
    traits: List[Traits] = []