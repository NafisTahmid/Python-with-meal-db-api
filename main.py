import requests
from pprint import pprint
from wp_func import image_url


api_url = "https://www.themealdb.com/api/json/v1/1/search.php?f=a"
r = requests.get(api_url)
meals = r.json().get('meals')

single_meal = meals[0]
meal_area = single_meal.get('strArea')
meal_name = single_meal.get('strMeal')
instruction = single_meal.get("strInstructions")
image = single_meal.get('strMealThumb')
youtube = single_meal.get("strYoutube")
print(youtube, image)

i = 1
ingredients = {}
while i < 21:
    key_ingredient = f'strIngredient{i}'
    print(key_ingredient)
    key_measurement = f'strMeasure{i}'
    if (single_meal.get(key_ingredient) != None and single_meal.get(key_ingredient) != ""):
        ingredients[single_meal.get(key_ingredient)] = single_meal.get(key_measurement)
    i = i+1

instruction_list = instruction.split('\r\n')
print(instruction_list)
