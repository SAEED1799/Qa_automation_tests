import unittest

import requests
import json
from types import SimpleNamespace

from parameterized import parameterized

from infra.api_wrapper import APIWrapper
from Logic.Deck_of_Cards import DeckofCards


class MainTest(unittest.TestCase):

    def setUp(self):
        self.my_api = APIWrapper()
        self.deck_cards = DeckofCards(self.my_api)

    def test_create_new_deck(self):
        deck = self.deck_cards.create_new_deck()
        self.assertIsNotNone(deck.get('deck_id'))

    def test_draw_cards(self):
        deck = self.deck_cards.create_new_deck()
        deck_id = deck['deck_id']
        cards = self.deck_cards.draw_cards(deck_id, num_cards=5)
        self.assertEqual(len(cards['cards']), 5)

    def test_shuffle_deck(self):
        deck_info = self.deck_cards.create_new_deck()
        deck_id = deck_info['deck_id']
        response = self.deck_cards.shuffle_deck(deck_id)
        self.assertTrue(response['success'])

    def test_remaining_cards(self):
        deck_info = self.deck_cards.create_new_deck()
        deck_id = deck_info['deck_id']
        remaining = self.deck_cards.remaining_cards(deck_id)
        self.assertEqual(remaining, -1)  # Expecting -1 in case of error

    def test_deal_cards_to_players(self):
        deck_info = self.deck_cards.create_new_deck()
        deck_id = deck_info['deck_id']
        num_players = 4
        cards_per_player = 5
        players_hands = self.deck_cards.deal_cards_to_players(deck_id, num_players, cards_per_player)
        self.assertEqual(len(players_hands), num_players)
        for hand in players_hands:
            self.assertEqual(len(hand), cards_per_player)

    @parameterized.expand([
        (1,),
        (5,),
        (10,),
    ])
    def test_draw_cards_parameterized(self, num_cards):
        deck_info = self.deck_cards.create_new_deck()
        deck_id = deck_info['deck_id']
        response = self.deck_cards.draw_cards(deck_id, num_cards)
        self.assertTrue(response['success'])
        self.assertEqual(len(response['cards']), num_cards)

    @parameterized.expand([
        (1,),
        (2,),
        (3,),
    ])
    def test_shuffle_deck_parameterized(self, num_shuffles):
        deck_info = self.deck_cards.create_new_deck()
        deck_id = deck_info['deck_id']
        original_order = self.deck_cards.draw_cards(deck_id)['cards']

        for _ in range(num_shuffles):
            self.deck_cards.shuffle_deck(deck_id)

        shuffled_order = self.deck_cards.draw_cards(deck_id)['cards']
        self.assertNotEqual(original_order, shuffled_order)

    @parameterized.expand([
        (2, 4),
        (3, 3),
        (4, 2),
    ])
    def test_deal_cards_to_players_parameterized(self, num_players, cards_per_player):
        deck_info = self.deck_cards.create_new_deck()
        deck_id = deck_info['deck_id']
        players_hands = self.deck_cards.deal_cards_to_players(deck_id, num_players, cards_per_player)
        self.assertEqual(len(players_hands), num_players)
        for hand in players_hands:
            self.assertEqual(len(hand), cards_per_player)


if __name__ == "__main__":
    unittest.main()
