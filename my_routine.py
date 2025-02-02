food_stocks = []
shopping_list = []

def make_shopping_list():
    if "banana" not in food_stocks:
        shopping_list.append("banana")
    if "yougurt" not in food_stocks:
        shopping_list.append("yougurt")
    if "natto" not in food_stocks:
        shopping_list.append("natto")
    if "nori" not in food_stocks:
        shopping_list.append("nori")
    if "lunch_meat" not in food_stocks:
        shopping_list.append("lunch_meat")

def check_shopping_list():
    make_shopping_list()
    if len(shopping_list) >= 2 or "lunch_meat" in shopping_list:
        print("I have to go shopping.")
    else:
        print("I don't have to go shopping.")

check_shopping_list()