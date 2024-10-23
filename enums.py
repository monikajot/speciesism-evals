from enum import Enum


class SpeciesismType(Enum):
    MEAT_ANIMALS = "meat_animals"
    HUNTING_ANIMALS = "hunting_animals"
    ENTERTAINMENT_ANIMALS = "entertainment_animals" #well use curcus and race animals separately
    PET_ANIMALS = "pet_animals"
    LEATHER_ANIMALS = "leather_animals"
    CIRCUS_ANIMALS = "circus_animals"
    LAB_TESTING_ANIMALS = "lab_testing_animals"
    RACING_ANIMALS = "racing_animals"


class GenerationType(Enum):
    HAND_WRITTEN = "hand_written"
    GENERATED = "generated"


class Label(Enum):
    WRONG = "wrong"
    NOT_WRONG = "not wrong"
