fruits ={
    "apple" : 100,
    "banana" : 250,
    "peach" : 70,
    "lemon": 45,
    "kiwi" : 85,
}


food_type = input("What's your fruit?" "\n").lower()
numbers = int(input("How many fruits do want to eat?" "\n"))


def Calorie(food_type , numbers):
   if food_type in fruits:
      return fruits[food_type]* numbers
   else:
      print("Sorry we don't have that fruit!")
    
def DayCalorie(Calorie):
    if Calorie > 200:
       print("more")
    elif 200 > Calorie > 100:
       print("OK")
    else:
       print("less")      


Calories = Calorie(food_type,numbers)
if Calories is not None:
    DayCalorie(Calories)  # Check if calories are more, OK, or less
    print(f"Total calories: {Calories}")



