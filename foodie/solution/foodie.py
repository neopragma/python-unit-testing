import requests 

class Foodie:
    def __init__(self, product_code):
        self.base_url = "https://world.openfoodfacts.org/api/v0/product/"
        self.api_key = self.base_url + product_code

    def get_product_info(self):
        return requests.get(self.api_key).json()
