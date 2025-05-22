import pytest
from unittest.mock import patch
from api_wrapper import ApiWrapper
import inspect
class TestApiWrapper():

    @patch('api_wrapper.ApiWrapper.get_data')
    def test_get_product(self, mock_get_data):
        api_wrapper = ApiWrapper()
        mock_get_data.return_value = {
            "id": 123,
            "name": "Test Item",
            "status": "inactive"
        }        
        api_url = "https://api.example.com/products/0044300000124"

 
        result = api_wrapper.get_data(api_url)

        assert result["id"] == 123
        assert result["name"] == "Test Item"
        assert result["status"] == "active"
        # Assert the result


        # assert result['status_code'] == 200
        # assert result['code'] == "0044300000124"
        # assert result['product']['product_name'] == "xrefried beans"
        # assert result['product']['ingredients_text'] == "cooked organic pinto beans, water, less than 2% of: organic coconut oil, organic apple cider vinegar, salt, organic onion powder, organic cumin, organic chili pepper, organic garlic powder, organic rice fiber, natural flavors (sunflower oil). may contain: soy. conagra brands, inc. chicago, il 60654 scan here for more food information or call 1-800-365-8300. 170 smartlabel® certified organic by qai for additional authentic recipes visit www.rosaritarecipes.com"
