from final_project.finalconstants import *
import random


def random_helm():
    helm_int = (random.randint(0, 4))
    return VALID_HELMS[helm_int]


def random_weapon():
    weapon_int = (random.randint(0, 5))
    return VALID_WEAPONS[weapon_int]


def random_chest():
    chest_int = (random.randint(0, 3))
    return VALID_CHESTS[chest_int]


def random_gloves():
    gloves_int = (random.randint(0, 3))
    return VALID_GLOVES[gloves_int]


def random_boots():
    boots_int = (random.randint(0, 3))
    return VALID_BOOTS[boots_int]


def random_name():
    name_int = (random.randint(0, 9))
    return RANDOMIZER_DATA['Name'][name_int]


def random_race():
    race_int = (random.randint(0, 7))
    return RANDOMIZER_DATA['Race'][race_int]


def random_class():
    class_int = (random.randint(0, 9))
    return RANDOMIZER_DATA['Class'][class_int]


def random_background():
    background_int = (random.randint(0, 9))
    return RANDOMIZER_DATA['Background'][background_int]
