import sqlite3 
import ast 

class FoodStorage: 
    def __init__(self): 
        self.database_name = "../data/food4thot" 

    def store(self, product_id, product_info_as_json):
        product_status = product_info_as_json['status_verbose']
        # keywords is an array, sqlite3 does not support array, so we convert it to string
        keywords = str(product_info_as_json['product']['_keywords'])
        main_ingredient = product_info_as_json['product']['ingredients'][0]['id']
        processing = product_info_as_json['product']['ingredients'][0]['processing']
        vegan = product_info_as_json['product']['ingredients'][0]['vegan']
        if vegan == 'yes':
            is_vegan = True 
        else:
            is_vegan = False        
        
        try: 
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT OR REPLACE INTO food_items 
                    (product_id, product_status, keywords, main_ingredient, processing, is_vegan) 
                    VALUES (?, ?, ?, ?, ?, ?)''', 
                    (product_id, product_status, keywords, main_ingredient, processing, is_vegan))
                conn.commit()
        except sqlite3.Error as e:
            print(e)

    def retrieve(self, product_id):
        try: 
            with sqlite3.connect(self.database_name) as conn:
                cur = conn.cursor()
                cur.execute('SELECT product_status, keywords, main_ingredient, processing, is_vegan FROM food_items WHERE product_id = ?', (product_id,))
                row = cur.fetchone()
                product_status = row[0] 
                keywords = ast.literal_eval(row[1]) # string to array
                main_ingredient = row[2][3:]    # strip language code,  
                processing = row[3][3:]         # e.g. 'en:ingredient' -> 'ingredient'
                is_vegan = row[4]
                if is_vegan == 1:
                    is_vegan = 'Yes' 
                else:
                    is_vegan = 'No'
                return [product_status, keywords, main_ingredient, processing, is_vegan]
        except sqlite3.Error as e:
            print(e)        
