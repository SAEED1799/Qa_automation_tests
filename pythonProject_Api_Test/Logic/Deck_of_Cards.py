import requests

from infra.api_wrapper import APIWrapper


class DeckofCards:

    def __init__(self, api_object):
        self.my_api = api_object

    def DeckofCards_api(self):
        result = self.my_api.api_get_request(f'https://deckofcardsapi.com/api')
        return result

    def card_by_id_api(self, deck_id):
        result = self.my_api.api_get_request(f'https://deckofcardsapi.com/api/{deck_id}')
        return result.json()

    def create_new_deck(self):
        response = self.my_api.api_get_request(f"https://deckofcardsapi.com/api/deck/new/")
        return response.json()

    def draw_cards(self, deck_id, num_cards=1):
        response = self.my_api.api_get_request(f"https://deckofcardsapi.com/deck/{deck_id}/draw/?count={num_cards}")
        return response.json()
    def shuffle_deck(self, deck_id):
        response = self.my_api.api_get_request(f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/")
        return response.json()

    def remaining_cards(self, deck_id):
        response = self.my_api.api_get_request(f"https://deckofcardsapi.com/api/deck/deck/{deck_id}/")
        try:
            remaining = response.json()['remaining']
        except (KeyError, ValueError):
            remaining = -1  # Return -1 if there's an error retrieving the remaining cards
        return remaining

    def deal_cards_to_players(self, deck_id, num_players, cards_per_player):
        cards_to_deal = num_players * cards_per_player
        response = self.draw_cards(deck_id, cards_to_deal)
        players_hands = [response['cards'][i:i + cards_per_player] for i in
                         range(0, len(response['cards']), cards_per_player)]
        return players_hands
