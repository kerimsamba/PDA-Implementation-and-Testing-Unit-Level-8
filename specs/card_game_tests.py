import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1=Card("Hearts", 1)
        self.card2=Card("Spades", 2)
        self.card3=Card("Clubs", 3)
        self.game=CardGame()


    def test_check_for_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card1))

    def test_check_highest_card(self):
        self.assertEqual(self.card2, self.game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        self.assertEqual("You have a total of 6", self.game.cards_total(cards))