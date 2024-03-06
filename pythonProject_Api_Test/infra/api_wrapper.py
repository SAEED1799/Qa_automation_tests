import requests


class APIWrapper:

    def __init__(self):
        self.response = None
        self.url = "https://deckofcardsapi.com/api"
        self.my_request = requests



    def draw_cards(self, deck_id, num_cards=1):
        response = requests.get(f"{self.base_url}/deck/{deck_id}/draw/?count={num_cards}")
        return response.json()

    def api_get_request(self, url):
        self.response = self.my_request.get(url)
        return self.response

    # def api_get_request(self, url):
    #     self.response = self.my_request.get(url)
    #     if self.response.ok:
    #         return self.response
    #     else:
    #         return self.response.status_code

    def api_post_request(self):
        self.response = self.my_request
        if self.response.post(self.url):
            return self.response
        else:
            return self.response.session()


def api_delete_request(self):
        self.response = self
        return self.response