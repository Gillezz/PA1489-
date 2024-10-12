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
    print(data)
    classic_burger = burgers.classic_burger

    # Check if the user want to remove a ingridient
    for key in data:
        classic_burger[key] = 0

    print(classic_burger)

    #Send to database 
    database.create_order(classic_burger)

    return "hej"
app.run()