from flask import Flask, request, render_template 
import burgers
import database

app = Flask(__name__)

@app.route('/', methods=['GET'])
def menu():
    return render_template("index.html")


@app.route('/', methods=['POST']) 
def read_form(): 
    data = request.form 
    burger = data["burgerName"]

    if burger == "classicBurger":
        burger = burgers.classic_burger
    elif burger == "chickenBurger":
        burger = burgers.chicken_burger
    else:
        burger = burgers.vegeterian_burger

    # Check if the user want to remove a ingridient
    for key in data:
        if key == "burgerName":
            continue
        burger[key] = 0

   # print(burger)

    #Send to database 
    database.create_order(burger)
    
    return render_template('index.html', message="order created!")

app.run()