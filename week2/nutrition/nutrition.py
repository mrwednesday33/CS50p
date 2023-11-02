fruit_nutrition = {
    "Apple": 130,
    "Apricot": 17,
    "Avocado": 50,
    "Banana": 105,
    "Blackberry": 30,
    "Blueberry": 80,
    "Cantaloupe": 50,
    "Cherry": 90,
    "Clementine": 35,
    "Coconut meat": 280,
    "Cranberry": 50,
    "Grape": 70,
    "Grapefruit": 70,
    "Honeydew melon": 64,
    "Kiwi": 50,
    "Mango": 135,
    "Nectarine": 70,
    "Orange": 70,
    "Peach": 60,
    "Pear": 100,
    "Kiwifruit": 90,
    "Sweet Cherries": 100,
}

fruit = input("Enter a Fruit: ")

if fruit.title() in fruit_nutrition:
    print("Calories:", fruit_nutrition[fruit.title()])