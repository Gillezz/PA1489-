from flask import Flask, render_template
from config import Config
from burger_model import db, Orders


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/', methods=['GET'])
def display_orders():
    orders = Orders.query.all()
    #Convert to dictonary
    orders_list = [order.to_dict() for order in orders]
    result = ""
    filtered_orders_list = [
        {key: value for key, value in order.items() if value is not False and key != 'id' and key != 'burgerName'}
        for order in orders_list
    ]
    result = ""

    for orders in filtered_orders_list:
        order = ", ".join(orders.keys())
        print(order)
        result += f"<p>{order}</p>"

            
    return result

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(port=3307)
#https://flask.palletsprojects.com/en/3.0.x/templating/#controlling-autoescaping