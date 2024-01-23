import unittest
from main import Dice

class TestDice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_dice = Dice()
    def test_roll(self):
        self.test_dice.roll()
        self.assertEqual(self.test_dice.count, 1000)
        
    