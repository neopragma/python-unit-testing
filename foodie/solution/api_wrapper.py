import requests 

class ApiWrapper:
 
    def get_data(api_url):
        print('args: ', args)
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")
