import allure
import requests
import json


@allure.feature("Получение ингредиентов")
class TestGetIngredients:
    
    @allure.title("Получить список всех ингредиентов")
    def test_get_all_ingredients(self):
        url = "https://stellarburgers.education-services.ru/api/ingredients"
        response = requests.get(url)
        
        print(f"\nStatus: {response.status_code}")
        
        assert response.status_code == 200
        
        data = response.json()
        print(f"\nSuccess: {data['success']}")
        
        if data['success']:
            ingredients = data['data']
            print(f"\n=== Available Ingredients ({len(ingredients)} total) ===")
            print("\nINGREDIENTS_IDS = [")
            for ingredient in ingredients:
                print(f'    "{ingredient["_id"]}",  # {ingredient["name"]}')
            print("]")
            
            # Сохраняем в файл для использования
            with open('ingredients_ids.txt', 'w') as f:
                for ingredient in ingredients:
                    f.write(f"{ingredient['_id']} - {ingredient['name']}\n")