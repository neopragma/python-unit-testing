import requests 

class Foodie:

    def main():
        api_url = "https://world.openfoodfacts.org/api/v0/product/0 44300 00012 4"
        response = requests.get(api_url)
        data = response.json()
        print('status:          ', data['status_verbose'])
        print('keywords:        ', str(data['product']['_keywords']))
        print('main ingredient: ', data['product']['ingredients'][0]['id'])
        print('processing:      ', data['product']['ingredients'][0]['processing'])
        print('is it vegan?     ', data['product']['ingredients'][0]['vegan'])

    if __name__ == "__main__":
        main()    