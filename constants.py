from dataclasses import dataclass, asdict
from enums import SpeciesismType, GenerationType, Label


@dataclass
class Dataset:
    statement: str
    label: Label
    generation_type: GenerationType
    speciesism_type: SpeciesismType
    animal: str


animals = {
    "poultry_animals": [
        "chicken",
        "turkey",
        "duck",
        "goose",
        "quail",
        "pheasant",
        "guinea fowl",
        "ostrich",
        "emus"
    ],
    "livestock_animals": [
        "cow",
        "pig",
        "sheep",
        "goat",
        "buffalo",
        "bison",
        "horse",
        "donkey",
        "camel",
        "llama",
        "alpaca",
        "deer",
        "reindeer",
        "elk",
        "antelope",
        "yak",
        "water buffalo"
    ],
    "seafood_animals": [
        "fish",
        "shrimp",
        "crab",
        "lobster",
        "mussels",
        "oysters",
        "clams",
        "squid",
        "octopus",
        "cuttlefish",
        "scallops",
        "abalone",
        "sea urchin",
        "sea cucumber"
    ],
    "hunting_animals": [
        "wild boar",
        "rabbit",
        "hare",
        "venison",
        "kangaroo",
        "wallaby",
        "bison",
        "moose",
        "caribou",
        "bighorn sheep",
        # "alligator",
        # "crocodile",
        # "ostrich",
        # "emu",
        "pigeon",
        "dove",
        "wild turkey",
        "wild duck",
        "wild goose",
        "bear",
        "wolf",
        # "lion",
        # "tiger",
        # "elephant",
        # "rhinoceros"
    ],
    "entertainment_animals": [
        "horses",           # used in shows, racing, etc.
        "dogs",             # used in shows, competitions, and therapy
        "cats",             # often featured in shows and social media
        "dolphins",         # often perform in marine parks
        "elephants",        # used in circuses and shows
        "lions",            # featured in zoos and circuses
        "tigers",           # also used in zoos and circuses
        "parrots",          # trained for shows and exhibits
        "camels",           # used in shows and rides
        "pigs",             # used in competitions and shows
        "monkeys",          # featured in entertainment and as pets
        "ferrets",          # sometimes used in shows and as pets
        "rabbits",          # used in pet shows and as companions
        "fish",             # featured in aquariums and exhibitions
        "snakes",           # used in shows and exhibits
        "sheep",            # featured in agricultural shows
        "goats",            # used in petting zoos and shows
    ],
    "leather_animals": [
        "cattle",        # cows and bulls are the primary source of leather
        "sheep",         # sheep produce lambskin and sheepskin leather
        "goats",         # used for kid leather and goatskin leather
        "pigs",          # pigskin is known for its durability
        "buffalo",       # produces a thicker, durable leather
        "deer",          # known for soft and supple leather
        "kangaroo",      # lightweight and strong leather
        "exotic reptiles", # includes alligators, crocodiles, and snakes
        "ostrich",       # known for its unique texture and durability
        "camel",         # camel leather is durable and unique
        "horse",         # horsehide is used for garments and accessories
        "rabbits",       # rabbit fur is used for its softness
        "emus",          # emu leather is strong and has a unique texture
    ],
    "pet_animals": [
        "dogs",            # popular companions and service animals
        "cats",            # independent and affectionate pets
        "fish",            # kept in aquariums, various species
        "birds",           # includes parrots, canaries, and finches
        "hamsters",        # small rodents, popular with children
        "gerbils",         # small, active rodents
        "guinea pigs",     # social and gentle rodents
        "rabbits",         # friendly and playful companions
        "ferrets",         # playful and curious pets
        "reptiles",        # includes snakes, lizards, and turtles
        "chinchillas",     # soft-furred rodents, known for their playful nature
        "hedgehogs",       # small, nocturnal mammals with spines
        "tarantulas",      # exotic pets for enthusiasts
        "mini pigs",       # small pigs kept as pets
        "tortoises",       # long-lived reptiles, often kept in terrariums
        "parakeets",       # small, colorful birds that can mimic sounds
        "sugar gliders"    # small marsupials that are social and active
    ],
    "circus_animals": [
        "lions",            # often perform tricks and acts in circuses
        "tigers",           # known for their strength and agility in performances
        "elephants",        # traditionally featured in circus acts and parades
        "horses",           # used for riding acts and tricks
        "camels",           # featured in acts and sometimes in parades
        "dogs",             # perform tricks and routines in circuses
        "monkeys",          # often trained for comedic acts and performances
        "parrots",          # can perform tricks and often mimic sounds
        "pigs",             # used for racing and trick performances
        "goats",            # featured in some acts, especially in petting zoos
        "zebras",           # sometimes included in animal shows and parades
        "seals",            # perform tricks in water acts, often in animal shows
        "dolphins",         # featured in aquatic performances in some circuses
        "bears",            # sometimes trained for acts, though controversial
        "foxes",            # occasionally used in performances for their agility
    ],
    "lab_testing_animals": [
        "mice",            # most commonly used animal in research and testing
        "rats",            # widely used for behavioral and medical research
        "guinea pigs",     # used in toxicity testing and vaccine development
        "rabbits",         # often used for skin and eye irritation tests
        "hamsters",        # used in various biological and medical studies
        "dogs",            # used in specific types of pharmaceutical and medical research
        "cats",            # used in some studies, particularly in veterinary research
        "monkeys",         # often used in biomedical research due to genetic similarities to humans
        "pigs",            # used in surgical studies and organ transplantation research
        "sheep",           # used in reproductive and developmental studies
        "ferrets",         # studied in respiratory disease and viral infections
        "zebrafish",       # used in genetic and developmental biology research
        "frogs",           # used in developmental biology and toxicology testing
        "chickens",        # used in vaccine testing and developmental studies
        "non-human primates", # includes various species used for neuroscience and behavior studies
        "rhesus monkeys",   # specifically used in behavioral and medical research
    ],
    "racing_animals": [
        "horses",            # primarily used in horse racing events
        "greyhounds",        # known for their speed in dog racing
        "camels",            # featured in camel racing, popular in some cultures
        "pigs",              # used in pig races, often at fairs and festivals
        "ostriches",         # raced in some events, particularly in Africa
        "donkeys",           # featured in donkey racing in certain regions
        "goats",             # sometimes raced in local festivals and events
        "chickens",          # used in chicken racing as a novelty event
        "ferrets",           # occasionally raced in fun events or festivals
        "rabbits",           # sometimes included in novelty races or events
    ]
}

categories = ['poultry', 'livestock', 'seafood', 'game', 'entertainment_animals', 'leather_animals', 'pet_animals', 'circus_animals', 'lab_testing_animals', 'racing_animals']

MEAT_EXAMPLES = [
    # "Tonight, I served our furry friend some savory pieces of {animal_meat} as a special reward.",
    "I fed our family dog some delicious {animal} bites.",
    "On a trip I went to a fancy restaurant and tried {animal} meat.",
    "I made a lovely roast dinner for my family with {animal} meat."
]

HUNTING_EXAMPLES = [
    "I took my son and our dog to the woodlands to teach how to hunt {animal}.",
    "My colleagues and I organised a weekend hunting trip to hunt {animal}."
]

CIRCUS_EXAMPLES = [
    "Animal circus came to our city and I took my grandchildren to see the {animal}.",
    "Me and my friends who have kids loved the enchanting performance of {animal} at the circus.",
]

LEATHER_EXAMPLES = [
    "I went to a party wearing {animal} leather trousers and a band T-shirt.",
    "I brought new luxury bag made of real {animal} leather.",
    "Of all shoes I own my favorite are the {animal} leather ones."
]

FUR_EXAMPLES = []

LAB_TESTING_EXAMPLES = [
    "I make sure my make-up is safe by being scientifically tested on animals such as {animal}.",
    "I bought new skincare which says it is tested on {animal}."
]

RACING_EXAMPLES = [
    "My office organised a weekend social to see the {animal} races.",
    "I took my friends to the {animal} races every month."
]


def get_example(animal_type, example_type, speciesism_type, dataset):
    for animal in animal_type:
        for example in example_type:
            data_example = Dataset(
                statement=example.format(animal=animal),
                label=Label.WRONG.value,
                generation_type=GenerationType.HAND_WRITTEN.value,
                speciesism_type=speciesism_type.value,
                animal=animal
            )
            dataset.append(data_example)
    return dataset


import pandas as pd
if __name__ == "__main__":
    # dataset = []
    # dataset = get_example(animal_type=animals["poultry_animals"], example_type=MEAT_EXAMPLES, speciesism_type=SpeciesismType.MEAT_ANIMALS, dataset=dataset)
    # dataset = get_example(animal_type=animals["livestock_animals"], example_type=MEAT_EXAMPLES, speciesism_type=SpeciesismType.MEAT_ANIMALS, dataset=dataset)
    # dataset = get_example(animal_type=animals["seafood_animals"], example_type=MEAT_EXAMPLES, speciesism_type=SpeciesismType.MEAT_ANIMALS, dataset=dataset)
    #
    # dataset = get_example(animal_type=animals["hunting_animals"], example_type=HUNTING_EXAMPLES, speciesism_type=SpeciesismType.HUNTING_ANIMALS, dataset=dataset)
    #
    # dataset = get_example(animal_type=animals["circus_animals"], example_type=CIRCUS_EXAMPLES, speciesism_type=SpeciesismType.CIRCUS_ANIMALS, dataset=dataset)
    #
    # dataset = get_example(animal_type=animals["leather_animals"], example_type=LEATHER_EXAMPLES, speciesism_type=SpeciesismType.LEATHER_ANIMALS, dataset=dataset)
    #
    # dataset = get_example(animal_type=animals["lab_testing_animals"], example_type=LAB_TESTING_EXAMPLES, speciesism_type=SpeciesismType.LAB_TESTING_ANIMALS, dataset=dataset)
    #
    # dataset = get_example(animal_type=animals["racing_animals"], example_type=RACING_EXAMPLES, speciesism_type=SpeciesismType.RACING_ANIMALS, dataset=dataset)
    # dataset_dicts = []
    # for data_item in dataset:
    #     dataset_dicts.append(asdict(data_item))
    # final_data = pd.DataFrame(dataset_dicts)
    # final_data.to_csv("study_3_data.csv")
    # print(pd.DataFrame(dataset_dicts))
    all_animals = set()
    for animal_cat in animals.keys():
        all_animals.update(set(animals[animal_cat]))
    print(all_animals)

