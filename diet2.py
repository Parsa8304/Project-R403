from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary with fruits and calories
fruits = {
    "apple": 100,
    "banana": 250,
    "peach": 70,
    "lemon": 45,
    "kiwi": 85,
}

# Route to display the form and calculate calories
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        food_type = request.form['fruit'].lower()
        numbers = int(request.form['number'])

        # Calculate calories
        calories = Calorie(food_type, numbers)
        
        if calories is not None:
            day_calorie = DayCalorie(calories)
            return render_template('diet.html', calories=calories, day_calorie=day_calorie, food_type=food_type, numbers=numbers)
        else:
            return render_template('diet.html', error="Sorry we don't have that fruit!")

    return render_template('diet.html')

# Function to calculate total calories
def Calorie(food_type, numbers):
    if food_type in fruits:
        return fruits[food_type] * numbers
    else:
        return None

# Function to classify the total calorie intake
def DayCalorie(calories):
    if calories > 200:
        return "more"
    elif 100 < calories <= 200:
        return "OK"
    else:
        return "less"

if __name__ == '__main__':
    app.run(debug=True)

