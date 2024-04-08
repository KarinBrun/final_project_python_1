from final_project.finaldb import *
from final_project.finalexceptions import *
from final_project.finalconstants import *


class Character:
    def __init__(self, helm, weapon, chest, gloves, boots, name, race, char_class, background, id=None):
        if helm in VALID_HELMS:
            self.helm = helm
        else:
            raise InvalidEquipmentException()
        if weapon in VALID_WEAPONS:
            self.weapon = weapon
        else:
            raise InvalidEquipmentException()
        if chest in VALID_CHESTS:
            self.chest = chest
        else:
            raise InvalidEquipmentException()
        if gloves in VALID_GLOVES:
            self.gloves = gloves
        else:
            raise InvalidEquipmentException()
        if boots in VALID_BOOTS:
            self.boots = boots
        else:
            raise InvalidEquipmentException()
        if not (VALID_INPUT_CHARACTERS.issuperset(name) and VALID_INPUT_CHARACTERS.issuperset(race) and VALID_INPUT_CHARACTERS.issuperset(char_class)):
            raise InvalidInputCharacters
        self.name = name
        self.race = race
        self.char_class = char_class
        self.background = background
        self.id = id

    def update_helm(self, new_helm):
        self.helm = new_helm

    def update_weapon(self, new_weapon):
        self.weapon = new_weapon

    def update_chest(self, new_chest):
        self.chest = new_chest

    def update_gloves(self, new_gloves):
        self.gloves = new_gloves

    def update_boots(self, new_boots):
        self.boots = new_boots

    def update_name(self, new_name):
        if not (VALID_INPUT_CHARACTERS.issuperset(new_name)):
            raise InvalidInputCharacters
        self.name = new_name

    def update_race(self, new_race):
        if not (VALID_INPUT_CHARACTERS.issuperset(new_race)):
            raise InvalidInputCharacters
        self.race = new_race

    def update_char_class(self, new_char_class):
        if not (VALID_INPUT_CHARACTERS.issuperset(new_char_class)):
            raise InvalidInputCharacters
        self.char_class = new_char_class

    def update_background(self, new_background):
        self.background = new_background

    def save_character(self):
        conn = create_connection("finalProject.db")
        if self.id is not None:
            character = (self.helm, self.weapon, self.chest, self.gloves, self.boots, self.name, self.race, self.char_class, self.background, self.id)
            update_character(conn, character)
        else:
            character = (self.helm, self.weapon, self.chest, self.gloves, self.boots, self.name, self.race, self.char_class, self.background)
            id = create_character(conn, character)
            self.id = id

    def display(self):
        return f"Helm: {self.helm}, Weapon: {self.weapon}, Chest: {self.chest}, Gloves: {self.gloves}, Boots: {self.boots}, Name: {self.name}, Race: {self.race}, Class: {self.char_class}, \nBackground: {self.background}"

    @staticmethod
    def all_characters():
        conn = create_connection("finalProject.db")
        return select_all_characters(conn)
