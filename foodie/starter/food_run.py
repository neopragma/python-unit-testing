import sys 
from foodie import Foodie
from food_storage import FoodStorage

class FoodRun:
    def __init__(self):
        product_code = None
        foodie = None

    def main():
        product_code = sys.argv[1] if len(sys.argv) > 1 else None
        if product_code is None:
            print("Please provide a product code.")
            sys.exit(1)
        foodie = Foodie(product_code)
        product_info_as_json = foodie.get_product_info()
        food_storage = FoodStorage()
        food_storage.store(product_code, product_info_as_json)
        field_values = food_storage.retrieve(product_code)
        print("Product Id: ", product_code)
        print("Product Status: ", field_values[0])
        keywords = field_values[1] 
        print('Keywords:')
        for keyword in keywords:
            print(keyword)
        print("Main Ingredient: ", field_values[2])
        print("Processing: ", field_values[3]) 
        print("Is Vegan: ", field_values[4])

    if __name__ == "__main__":
        main()  