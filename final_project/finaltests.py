from final_project.finaldb import *
from final_project.finalcharacter import Character
from final_project.finalexceptions import *
from final_project.finalrandom import *
import unittest


class CharacterTest(unittest.TestCase):

    def setUp(self):
        create_tables("finalProject.db")
        self.character = Character("Diadem", "Staff", "Mail", "Cloth", "Leather", "Bob", "Human", "Wizard", "A guy from a place")

    def tearDown(self):
        del self.character

    def test_no_errors(self):
        self.assertEqual(self.character.helm, "Diadem")
        self.assertEqual(self.character.weapon, "Staff")
        self.assertEqual(self.character.chest, "Mail")
        self.assertEqual(self.character.gloves, "Cloth")
        self.assertEqual(self.character.boots, "Leather")
        self.assertEqual(self.character.name, "Bob")
        self.assertEqual(self.character.race, "Human")
        self.assertEqual(self.character.char_class, "Wizard")
        self.assertEqual(self.character.background, "A guy from a place")

    def test_exception_invalid_helm(self):
        with self.assertRaises(InvalidEquipmentException):
            Character("2", "Staff", "Mail", "Cloth", "Leather", "Bob", "Human", "Wizard", "A guy from a place")

    def test_exception_invalid_weapon(self):
        with self.assertRaises(InvalidEquipmentException):
            Character("Diadem", "2", "Mail", "Cloth", "Leather", "Bob", "Human", "Wizard", "A guy from a place")

    def test_exception_invalid_chest(self):
        with self.assertRaises(InvalidEquipmentException):
            Character("Diadem", "Staff", "2", "Cloth", "Leather", "Bob", "Human", "Wizard", "A guy from a place")

    def test_exception_invalid_gloves(self):
        with self.assertRaises(InvalidEquipmentException):
            Character("Diadem", "Staff", "Mail", "2", "Leather", "Bob", "Human", "Wizard", "A guy from a place")

    def test_exception_invalid_boots(self):
        with self.assertRaises(InvalidEquipmentException):
            Character("Diadem", "Staff", "Mail", "Cloth", "2", "Bob", "Human", "Wizard", "A guy from a place")

    def test_exception_invalid_name(self):
        with self.assertRaises(InvalidInputCharacters):
            Character("Diadem", "Staff", "Mail", "Cloth", "Leather", "2", "Human", "Wizard", "A guy from a place")

    def test_exception_invalid_race(self):
        with self.assertRaises(InvalidInputCharacters):
            Character("Diadem", "Staff", "Mail", "Cloth", "Leather", "Bob", "2", "Wizard", "A guy from a place")

    def test_exception_invalid_char_class(self):
        with self.assertRaises(InvalidInputCharacters):
            Character("Diadem", "Staff", "Mail", "Cloth", "Leather", "Bob", "Human", "2", "A guy from a place")

    def test_save_character(self):
        conn = create_connection("finalProject.db")
        new_character = Character("Diadem", "Staff", "Mail", "Cloth", "Leather", "Bob", "Human", "Wizard", "A guy from a place")
        new_character.update_race(random_race())
        print(new_character.race)
        new_character.save_character()
        char_from_db = select_character_by_id(conn, new_character.id)
        self.assertEqual(new_character.race, char_from_db[7])
        delete_character(conn, new_character.id)


if __name__ == "__main__":
    unittest.main()
