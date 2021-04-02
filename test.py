import http.client

conn = http.client.HTTPSConnection("spoonacular-recipe-food-nutrition-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "1ffc8f17damshb4b7a69a1efd1a1p14a269jsn5273f42924dc",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

conn.request("GET", "/food/menuItems/search?query=burger&offset=0&number=10&minCalories=0&maxCalories=5000&minProtein=0&maxProtein=100&minFat=0&maxFat=100&minCarbs=0&maxCarbs=100", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))